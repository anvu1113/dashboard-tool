<?php

use App\Http\Controllers\Api\AuthController;
use App\Http\Controllers\Api\HealthController;
use Illuminate\Support\Facades\Route;

Route::get('/health', [HealthController::class, 'check']);

// Public auth routes
Route::prefix('auth')->group(function () {
    Route::post('/register', [AuthController::class, 'register']);
    Route::post('/login', [AuthController::class, 'login']);
    Route::post('/forgot-password', [AuthController::class, 'forgotPassword']);
    Route::post('/reset-password', [AuthController::class, 'resetPassword']);
});

// Protected auth routes
Route::prefix('auth')->middleware('auth:sanctum')->group(function () {
    Route::post('/logout', [AuthController::class, 'logout']);
    Route::get('/me', [AuthController::class, 'me']);
});

// Extension Routes
Route::prefix('extension')->group(function () {
    Route::post('/auth', [AuthController::class, 'login']); 
    Route::post('/check-license', [App\Http\Controllers\Api\Extension\LicenseController::class, 'check']);
    Route::post('/feature/translate', [App\Http\Controllers\Api\Extension\FeatureController::class, 'translate']);
    Route::post('/feature/currency', [App\Http\Controllers\Api\Extension\FeatureController::class, 'currency']);
});

// Admin Routes
Route::prefix('admin')->middleware(['auth:sanctum', 'role:admin'])->group(function () {
    Route::apiResource('users', App\Http\Controllers\Api\Admin\UserController::class);
    Route::apiResource('licenses', App\Http\Controllers\Api\Admin\LicenseController::class);
    Route::get('/usage', [App\Http\Controllers\Api\Admin\UsageController::class, 'index']);
});

// File serving for FilePond (catch-all route for any file path)
Route::get('/files/{path}', [App\Http\Controllers\Api\ImageLoaderController::class, 'getFile'])->where('path', '.*');

// General protected routes
Route::middleware('auth:sanctum')->group(function () {
    Route::post('/upload', [App\Http\Controllers\Api\FileController::class, 'store']);
    Route::delete('/files/{id}', [App\Http\Controllers\Api\FileController::class, 'destroy']);
});
