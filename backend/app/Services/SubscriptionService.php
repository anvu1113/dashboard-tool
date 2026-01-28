<?php

namespace App\Services;

use App\Models\Plan;
use App\Models\Subscription;
use App\Models\UsageLog;
use Carbon\Carbon;
use Illuminate\Support\Facades\DB;

class SubscriptionService
{
    /**
     * Get or create a default free subscription for a user
     */
    public function getActiveSubscription($user)
    {
        $subscription = Subscription::with('plan.features')
            ->where('user_id', $user->id)
            ->where('status', 'active')
            ->where(function ($query) {
                $query->whereNull('ends_at')
                      ->orWhere('ends_at', '>', Carbon::now());
            })
            ->latest()
            ->first();

        if (!$subscription) {
            // Auto-assign Free plan if no active subscription exists
            $freePlan = Plan::where('code', 'free')->first();
            if ($freePlan) {
                $subscription = Subscription::create([
                    'user_id' => $user->id,
                    'plan_id' => $freePlan->id,
                    'starts_at' => Carbon::now(),
                    'ends_at' => null, // Lifetime free
                    'status' => 'active',
                ]);
                $subscription->load('plan.features');
            }
        }

        return $subscription;
    }

    /**
     * Check if user can use a specific feature based on daily limit
     */
    public function canUseFeature($user, $featureKey)
    {
        $subscription = $this->getActiveSubscription($user);
        if (!$subscription) {
            return false;
        }

        $feature = $subscription->plan->features->where('key', $featureKey)->first();
        
        // If feature not defined in plan, default to false/0
        if (!$feature) {
            return false;
        }

        // Boolean feature (e.g., export_excel)
        if ($feature->value === 'true') {
            return true;
        }
        
        if ($feature->value === 'false') {
            return false;
        }

        // Numeric limit feature (e.g., max_products_per_day)
        $limit = (int) $feature->value;
        if ($limit > 0) {
            $todayUsage = UsageLog::where('user_id', $user->id)
                ->where('feature_key', $featureKey)
                ->where('date', Carbon::today())
                ->value('count') ?? 0;

            return $todayUsage < $limit;
        }

        return true; // No limit if not numeric/boolean usually implies unlimited or handled elsewhere? 
                     // Assuming numeric value is a limit. If value is "unlimited", handle that logic.
    }

    /**
     * Log usage for a feature
     */
    public function incrementUsage($user, $featureKey)
    {
        $log = UsageLog::firstOrCreate(
            [
                'user_id' => $user->id,
                'feature_key' => $featureKey,
                'date' => Carbon::today(),
            ],
            ['count' => 0]
        );

        $log->increment('count');
        return $log->count;
    }
}
