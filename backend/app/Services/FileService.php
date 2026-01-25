<?php

namespace App\Services;

use App\Models\File;
use Illuminate\Http\UploadedFile;
use Illuminate\Support\Facades\Storage;
use Illuminate\Support\Str;

class FileService
{
    /**
     * Upload a file and save it to the database.
     *
     * @param UploadedFile $file
     * @param string $disk
     * @param string|null $type
     * @param string|null $modelType
     * @param int|null $modelId
     * @return File
     */
    public function upload(UploadedFile $file, string $disk = 'public', ?string $type = null, ?string $modelType = null, ?int $modelId = null): File
    {
        $fileName = Str::uuid() . '.' . $file->getClientOriginalExtension();
        $path = $file->storeAs('uploads', $fileName, $disk);

        $fileData = [
            'disk' => $disk,
            'path' => $path,
            'size' => $file->getSize(),
            'mime_type' => $file->getMimeType(),
            'type' => $type,
            'model_type' => $modelType,
            'model_id' => $modelId,
        ];

        return File::create($fileData);
    }

    /**
     * Delete a file from storage and database.
     * 
     * @param File $file
     * @return bool
     */
    public function delete(File $file): bool
    {
        Storage::disk($file->disk)->delete($file->path);
        return $file->delete();
    }
}
