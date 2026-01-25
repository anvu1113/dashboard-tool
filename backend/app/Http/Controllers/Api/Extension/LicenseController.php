<?php

namespace App\Http\Controllers\Api\Extension;

use App\Http\Controllers\Controller;
use App\Models\License;
use Illuminate\Http\Request;

class LicenseController extends Controller
{
    public function check(Request $request)
    {
        $request->validate([
            'license_key' => 'required|string',
            'device_fingerprint' => 'required|string',
        ]);

        $license = License::where('key', $request->license_key)->first();

        if (!$license) {
            return response()->json(['valid' => false, 'message' => 'Invalid license key'], 404);
        }

        if ($license->status !== 'active') {
            return response()->json(['valid' => false, 'message' => 'License is ' . $license->status], 403);
        }

        if ($license->expires_at && $license->expires_at->isPast()) {
            return response()->json(['valid' => false, 'message' => 'License expired'], 403);
        }

        // Log device or check device limit here
        $license->devices()->updateOrCreate(
            ['device_fingerprint' => $request->device_fingerprint],
            ['last_active_at' => now()]
        );

        return response()->json([
            'valid' => true,
            'type' => $license->type,
            'expires_at' => $license->expires_at,
        ]);
    }
}
