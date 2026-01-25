<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Storage;

class ImageLoaderController extends Controller
{
    /**
     * Serve file from storage via API (for FilePond server.load)
     * Supports both path-based and ID-based access
     *
     * @param Request $request
     * @param string|null $path Path to file (e.g., "uploads/image.jpg")
     * @return \Symfony\Component\HttpFoundation\BinaryFileResponse|\Illuminate\Http\JsonResponse
     */
    public function getFile(Request $request, $path = null)
    {
        try {
            // If path is provided in URL parameter
            if (!$path && $request->has('path')) {
                $path = $request->input('path');
            }

            if (!$path) {
                return response()->json(['error' => 'File path is required'], 400);
            }

            // Remove leading /storage/ if present
            $path = ltrim($path, '/storage/');
            $path = ltrim($path, '/');

            // Security: prevent directory traversal
            if (strpos($path, '..') !== false || strpos($path, '//') !== false) {
                return response()->json(['error' => 'Invalid file path'], 400);
            }

            // Check if file exists in public storage
            $disk = Storage::disk('public');

            if (!$disk->exists($path)) {
                return response()->json(['error' => 'File not found'], 404);
            }

            // Get file path and mime type
            $filePath = $disk->path($path);

            // Get mime type using PHP's mime_content_type or finfo
            $mimeType = mime_content_type($filePath);
            if (!$mimeType) {
                // Fallback to common image types based on extension
                $extension = strtolower(pathinfo($path, PATHINFO_EXTENSION));
                $mimeType = match($extension) {
                    'jpg', 'jpeg' => 'image/jpeg',
                    'png' => 'image/png',
                    'gif' => 'image/gif',
                    'webp' => 'image/webp',
                    'svg' => 'image/svg+xml',
                    default => 'application/octet-stream',
                };
            }

            // Return file with proper headers
            return response()->file($filePath, [
                'Content-Type' => $mimeType,
                'Cache-Control' => 'public, max-age=31536000, immutable',
                'Access-Control-Allow-Origin' => '*',
                'Access-Control-Allow-Methods' => 'GET, OPTIONS',
                'Access-Control-Allow-Headers' => 'Content-Type, Accept',
            ]);
        } catch (\Exception $e) {
            return response()->json(['error' => 'Error loading file: ' . $e->getMessage()], 500);
        }
    }
}
