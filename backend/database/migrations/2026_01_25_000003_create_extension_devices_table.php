<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('extension_devices', function (Blueprint $table) {
            $table->id();
            $table->foreignId('license_id')->constrained()->onDelete('cascade');
            $table->string('device_fingerprint'); // A unique hash from the client
            $table->string('user_agent')->nullable();
            $table->timestamp('last_active_at')->useCurrent();
            $table->timestamps();
            
            $table->unique(['license_id', 'device_fingerprint']);
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('extension_devices');
    }
};
