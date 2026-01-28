<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        // Drop old table if exists to ensure new structure
        Schema::dropIfExists('usage_logs');

        Schema::create('usage_logs', function (Blueprint $table) {
            $table->id();
            $table->foreignId('user_id')->constrained()->cascadeOnDelete();
            $table->string('feature_key');
            $table->integer('count')->default(0);
            $table->date('date');
            $table->timestamps();

            // Unique constraint to track usage per user per feature per day
            $table->unique(['user_id', 'feature_key', 'date']);
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('usage_logs');
    }
};
