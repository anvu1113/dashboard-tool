<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use App\Services\FileService;
use Illuminate\Http\Request;

class FileController extends Controller
{
    protected $fileService;

    public function __construct(FileService $fileService)
    {
        $this->fileService = $fileService;
    }

    public function store(Request $request)
    {
        $request->validate([
            'file' => 'required|file',
            'model_type' => 'nullable|string',
            'model_id' => 'nullable|integer',
            'type' => 'nullable|string'
        ]);

        $disk = $request->input('disk', 'public');

        $file = $this->fileService->upload(
            $request->file('file'),
            $disk,
            $request->input('type'),
            $request->input('model_type'),
            $request->input('model_id')
        );

        return response()->json([
            'success' => true,
            'path' => $file->path,
            'data' => $file
        ]);
    }

    public function destroy($id)
    {
        $file = \App\Models\File::findOrFail($id);
        
        // Delete physical file
        \Illuminate\Support\Facades\Storage::disk($file->disk)->delete($file->path);
        
        // Delete database record
        $file->delete();

        return response()->json([
            'success' => true,
            'message' => 'File deleted successfully'
        ]);
    }
}
