<?php

namespace Database\Seeders;

use Illuminate\Database\Seeder;
use App\Models\Category;
use App\Models\Product;
use Illuminate\Support\Str;

class UpdateProductInventorySeeder extends Seeder
{
    /**
     * Run the database seeds - Update existing products with inventory data
     */
    public function run(): void
    {
        $this->command->info('Updating products with inventory data...');
        
        // Update all products with sample inventory data
        $products = Product::all();
        
        foreach ($products as $product) {
            // Calculate random but realistic inventory data
            $costPrice = $product->selling_price ? round($product->selling_price * 0.6) : 100000; // 40% margin
            $stockQty = rand(10, 100);
            $soldQty = rand(5, 50);
            
            $product->update([
                'cost_price' => $costPrice,
                'stock_quantity' => $stockQty,
                'sold_quantity' => $soldQty,
                'reorder_level' => 10,
                'sku' => strtoupper(Str::slug($product->name, '-'))
            ]);
        }
        
        $this->command->info('✅ Updated ' . $products->count() . ' products with inventory data');
        $this->command->info('🎉 Inventory data seeding complete!');
    }
}
