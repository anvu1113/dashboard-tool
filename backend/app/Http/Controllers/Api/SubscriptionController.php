<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use App\Services\SubscriptionService;
use Illuminate\Http\Request;

class SubscriptionController extends Controller
{
    protected $subscriptionService;

    public function __construct(SubscriptionService $subscriptionService)
    {
        $this->subscriptionService = $subscriptionService;
    }

    public function me(Request $request)
    {
        $user = $request->user();
        if (!$user) {
             return response()->json(['message' => 'Unauthenticated'], 401);
        }

        $subscription = $this->subscriptionService->getActiveSubscription($user);

        if (!$subscription) {
            return response()->json([
                'plan' => 'none',
                'expires_at' => null,
                'features' => []
            ]);
        }

        // Transform features into key-value pairs
        $features = $subscription->plan->features->pluck('value', 'key');

        return response()->json([
            'plan' => $subscription->plan->code,
            'expires_at' => $subscription->ends_at ? $subscription->ends_at->toDateString() : null,
            'features' => $features,
        ]);
    }
}
