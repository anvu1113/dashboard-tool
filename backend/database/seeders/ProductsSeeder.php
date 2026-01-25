<?php

namespace Database\Seeders;

use Illuminate\Database\Seeder;
use App\Models\Category;
use App\Models\Product;
use Illuminate\Support\Str;

class ProductsSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        // Create or find Categories
        $categories = [
            [
                'name' => 'Áo Thun Nữ',
                'slug' => 'ao-thun-nu',
                'description' => 'Áo thun nữ thời trang, phong cách trẻ trung, năng động'
            ],
            [
                'name' => 'Túi Xách',
                'slug' => 'tui-xach',
                'description' => 'Túi xách nữ cao cấp, phong cách sang trọng'
            ],
            [
                'name' => 'Nón',
                'slug' => 'non',
                'description' => 'Nón thời trang, phụ kiện không thể thiếu'
            ]
        ];

        $createdCategories = [];
        foreach ($categories as $categoryData) {
            $category = Category::firstOrCreate(
                ['slug' => $categoryData['slug']], // Find by slug
                $categoryData // Create with all data
            );
            $createdCategories[$categoryData['slug']] = $category;
        }

        // Products for "Áo Thun Nữ"
        $aoThunProducts = [
            [
                'name' => 'Áo Thun Nữ Basic Trắng',
                'description' => 'Áo thun nữ basic màu trắng, chất liệu cotton 100%, thoáng mát, dễ phối đồ. Form dáng suông nhẹ, phù hợp mọi vóc dáng.',
                'price' => 150000,
                'image' => 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=800&q=80'
            ],
            [
                'name' => 'Áo Thun Nữ Croptop Đen',
                'description' => 'Áo thun croptop màu đen, thiết kế ôm body, tôn dáng. Chất liệu co giãn 4 chiều, thoải mái vận động.',
                'price' => 180000,
                'image' => 'https://images.unsplash.com/photo-1583743814966-8936f5b7be1a?w=800&q=80'
            ],
            [
                'name' => 'Áo Thun Nữ Oversize Hồng',
                'description' => 'Áo thun oversize màu hồng pastel, phong cách Hàn Quốc. Form rộng thoải mái, phù hợp đi chơi, dạo phố.',
                'price' => 200000,
                'image' => 'https://images.unsplash.com/photo-1525507119028-ed4c629a60a3?w=800&q=80'
            ],
            [
                'name' => 'Áo Thun Nữ Có Cổ Xanh Navy',
                'description' => 'Áo thun có cổ màu xanh navy, phong cách thanh lịch. Phù hợp đi làm hoặc đi học.',
                'price' => 220000,
                'image' => 'https://images.unsplash.com/photo-1618354691373-d851c5c3a990?w=800&q=80'
            ],
            [
                'name' => 'Áo Thun Nữ Tay Dài Be',
                'description' => 'Áo thun tay dài màu be, chất liệu mềm mại. Form suông nhẹ, phù hợp mùa thu đông.',
                'price' => 250000,
                'image' => 'https://images.unsplash.com/photo-1576566588028-4147f3842f27?w=800&q=80'
            ]
        ];

        foreach ($aoThunProducts as $productData) {
            $productData['category_id'] = $createdCategories['ao-thun-nu']->id;
            $productData['slug'] = Str::slug($productData['name']);
            Product::create($productData);
        }

        // Products for "Túi Xách"
        $tuiXachProducts = [
            [
                'name' => 'Túi Xách Tote Canvas Đen',
                'description' => 'Túi tote canvas màu đen, thiết kế tối giản. Chất liệu canvas bền đẹp, có ngăn phụ bên trong. Phù hợp đi làm, đi học.',
                'price' => 350000,
                'image' => 'https://images.unsplash.com/photo-1590874103328-eac38a683ce7?w=800&q=80'
            ],
            [
                'name' => 'Túi Xách Da Mini Nâu',
                'description' => 'Túi xách da mini màu nâu, thiết kế sang trọng. Quai xách vàng gold, có dây đeo vai. Size nhỏ gọn, tiện lợi.',
                'price' => 450000,
                'image' => 'https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=800&q=80'
            ],
            [
                'name' => 'Túi Xách Đeo Chéo Trắng',
                'description' => 'Túi đeo chéo màu trắng, phong cách trẻ trung. Chất liệu PU cao cấp, dây đeo điều chỉnh được.',
                'price' => 280000,
                'image' => 'https://images.unsplash.com/photo-1566150905458-1bf1fc113f0d?w=800&q=80'
            ],
            [
                'name' => 'Túi Xách Công Sở Đen',
                'description' => 'Túi xách công sở màu đen, thiết kế chuyên nghiệp. Nhiều ngăn tiện dụng, đựng được laptop 14 inch.',
                'price' => 550000,
                'image' => 'https://images.unsplash.com/photo-1548036328-c9fa89d128fa?w=800&q=80'
            ]
        ];

        foreach ($tuiXachProducts as $productData) {
            $productData['category_id'] = $createdCategories['tui-xach']->id;
            $productData['slug'] = Str::slug($productData['name']);
            Product::create($productData);
        }

        // Products for "Nón"
        $nonProducts = [
            [
                'name' => 'Nón Bucket Đen Unisex',
                'description' => 'Nón bucket màu đen, phong cách streetwear. Chất vải cotton mềm mại, thoáng khí. Phù hợp cả nam và nữ.',
                'price' => 120000,
                'image' => 'https://images.unsplash.com/photo-1588850561407-ed78c282e89b?w=800&q=80'
            ],
            [
                'name' => 'Nón Snapback MLB Yankees',
                'description' => 'Nón snapback MLB New York Yankees, chính hãng. Logo thêu nổi, vành nón cứng. Phong cách thể thao, khỏe khoắn.',
                'price' => 380000,
                'image' => 'https://images.unsplash.com/photo-1575428652377-a2d80e2277fc?w=800&q=80'
            ],
            [
                'name' => 'Nón Lưỡi Trai Be Pastel',
                'description' => 'Nón lưỡi trai màu be pastel, phong cách Hàn Quốc. Chất vải nhung mềm, vành nón cong. Phù hợp nữ giới.',
                'price' => 150000,
                'image' => 'https://images.unsplash.com/photo-1521369909029-2afed882baee?w=800&q=80'
            ],
            [
                'name' => 'Nón Rộng Vành Cói',
                'description' => 'Nón rộng vành chất liệu cói, phong cách resort. Bảo vệ da khỏi ánh nắng, phù hợp đi biển, du lịch.',
                'price' => 200000,
                'image' => 'https://images.unsplash.com/photo-1529958030586-3aae4ca485ff?w=800&q=80'
            ],
            [
                'name' => 'Nón Len Beanie Nâu',
                'description' => 'Nón len beanie màu nâu, giữ ấm mùa đông. Chất len mềm, co giãn tốt. Phong cách đơn giản, dễ phối đồ.',
                'price' => 100000,
                'image' => 'https://images.unsplash.com/photo-1576871337622-98d48d1cf531?w=800&q=80'
            ]
        ];

        foreach ($nonProducts as $productData) {
            $productData['category_id'] = $createdCategories['non']->id;
            $productData['slug'] = Str::slug($productData['name']);
            Product::create($productData);
        }

        $this->command->info('✅ Đã tạo ' . count($categories) . ' categories');
        $this->command->info('✅ Đã tạo ' . (count($aoThunProducts) + count($tuiXachProducts) + count($nonProducts)) . ' products');
        $this->command->info('🎉 Seeding hoàn tất!');
    }
}
