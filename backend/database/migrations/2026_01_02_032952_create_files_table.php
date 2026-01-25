<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create("files", function (Blueprint $table) {
            $table->id();
            $table->string("model_type")->nullable();
            $table->unsignedBigInteger("model_id")->nullable();
            
            $table->string("disk")->default("public"); // public, s3, etc.
            $table->string("path");
            $table->string("type")->nullable(); // image, document, video, etc.
            $table->unsignedBigInteger("size")->nullable(); // in bytes
            $table->string("mime_type")->nullable();

            $table->timestamps();
            
            $table->index(["model_type", "model_id"]);
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists("files");
    }
};
