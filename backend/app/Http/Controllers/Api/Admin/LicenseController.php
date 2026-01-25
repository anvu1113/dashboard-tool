<?php

namespace App\Http\Controllers\Api\Admin;

use App\Http\Controllers\Controller;
use App\Models\License;
use Illuminate\Http\Request;
use Illuminate\Support\Str;

class LicenseController extends Controller
{
    public function index()
    {
        return License::with('user')->paginate(10);
    }

    public function store(Request $request)
    {
        $validated = $request->validate([
            'user_id' => 'required|exists:users,id',
            'type' => 'required|in:trial,pro,enterprise',
            'expires_at' => 'nullable|date',
        ]);

        $license = License::create([
            'user_id' => $validated['user_id'],
            'key' => strtoupper(Str::random(16)),
            'type' => $validated['type'],
            'status' => 'active',
            'expires_at' => $validated['expires_at'],
        ]);

        return $license;
    }

    public function show(License $license)
    {
        return $license->load('usageLogs', 'devices');
    }

    public function update(Request $request, License $license)
    {
        $validated = $request->validate([
            'status' => 'sometimes|in:active,suspended,expired',
            'type' => 'sometimes|in:trial,pro,enterprise',
            'expires_at' => 'nullable|date',
        ]);

        $license->update($validated);

        return $license;
    }

    public function destroy(License $license)
    {
        $license->delete();
        return response()->noContent();
    }
}
