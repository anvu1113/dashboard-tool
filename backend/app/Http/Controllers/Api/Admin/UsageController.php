<?php

namespace App\Http\Controllers\Api\Admin;

use App\Http\Controllers\Controller;
use App\Models\UsageLog;
use Illuminate\Http\Request;

class UsageController extends Controller
{
    public function index()
    {
        return UsageLog::with('license.user')->latest()->paginate(20);
    }
}
