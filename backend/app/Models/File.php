<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Support\Facades\Storage;

class File extends Model
{
    protected $fillable = [
        'model_type',
        'model_id',
        'disk',
        'path',
        'type',
        'size',
        'mime_type'
    ];

    protected $appends = ['url'];

    public function model()
    {
        return $this->morphTo();
    }

    public function getUrlAttribute()
    {
        return Storage::disk($this->disk)->url($this->path);
    }
}
