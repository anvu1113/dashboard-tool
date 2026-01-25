<?php

namespace App\Http\Controllers\Api\Extension;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;

class FeatureController extends Controller
{
    public function translate(Request $request)
    {
        // Placeholder for translation logic
        return response()->json(['translated_text' => 'Translated: ' . $request->input('text')]);
    }

    public function currency(Request $request)
    {
        // Placeholder for currency conversion logic
        return response()->json(['converted_amount' => $request->input('amount') * 25000]);
    }
}
