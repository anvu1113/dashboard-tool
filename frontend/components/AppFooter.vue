<template>
  <footer class="bg-white border-t border-gray-light mt-auto">
    <div class="container mx-auto px-4 py-8">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
        <!-- Thông tin shop -->
        <div>
          <h3 class="font-semibold text-primary mb-4">Thông tin shop</h3>
          <p class="text-gray-dark text-sm mb-2">Clothes Store</p>
          <p class="text-gray-dark text-sm">Thời trang chất lượng, giá tốt nhất</p>
        </div>

        <!-- Liên hệ -->
        <div>
          <h3 class="font-semibold text-primary mb-4">Liên hệ</h3>
          <div class="space-y-3 text-sm">
            <a href="tel:" class="text-gray-dark hover:text-primary block flex items-center gap-2">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
              </svg>
              <span>Hotline: [Số điện thoại]</span>
            </a>
            
            <!-- Social Media Icons -->
            <div class="flex items-center gap-3 pt-2">
              <a 
                href="#" 
                target="_blank"
                rel="noopener noreferrer"
                class="text-gray-dark hover:text-[#0068FF] transition-colors"
                aria-label="Zalo"
                title="Zalo"
              >
                <!-- Zalo Icon - Chữ Z trong hình tròn -->
                <svg class="w-7 h-7" viewBox="0 0 24 24" fill="none">
                  <circle cx="12" cy="12" r="10" fill="currentColor" opacity="0.1" class="hover:opacity-0.2"/>
                  <path d="M8 7h8l-6 6h6l-6 6" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
                </svg>
              </a>
              
              <a 
                href="#" 
                target="_blank"
                rel="noopener noreferrer"
                class="text-gray-dark hover:text-[#1877F2] transition-colors"
                aria-label="Facebook"
                title="Facebook"
              >
                <!-- Facebook Icon -->
                <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/>
                </svg>
              </a>
              
              <a 
                href="#" 
                target="_blank"
                rel="noopener noreferrer"
                class="text-gray-dark hover:text-[#E4405F] transition-colors"
                aria-label="Instagram"
                title="Instagram"
              >
                <!-- Instagram Icon -->
                <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/>
                </svg>
              </a>
            </div>
          </div>
        </div>

        <!-- Chính sách -->
        <div>
          <h3 class="font-semibold text-primary mb-4">Chính sách</h3>
          <div class="space-y-2 text-sm">
            <a href="#" class="text-gray-dark hover:text-primary block">
              Chính sách đổi trả
            </a>
            <a href="#" class="text-gray-dark hover:text-primary block">
              Chính sách vận chuyển
            </a>
            <a href="#" class="text-gray-dark hover:text-primary block">
              Quy trình đặt hàng
            </a>
          </div>
        </div>

        <!-- Tin tức -->
        <div>
          <h3 class="font-semibold text-primary mb-4">Tin tức</h3>
          <div class="space-y-2 text-sm">
            <NuxtLink to="/news" class="text-gray-dark hover:text-primary block">
              Tất cả bài viết
            </NuxtLink>
            <NuxtLink to="/news?category=decor" class="text-gray-dark hover:text-primary block">
              Decor & Nội thất
            </NuxtLink>
            <NuxtLink to="/news?category=fashion" class="text-gray-dark hover:text-primary block">
              Thời trang
            </NuxtLink>
            <NuxtLink to="/news?category=tips" class="text-gray-dark hover:text-primary block">
              Mẹo vặt
            </NuxtLink>
          </div>
        </div>
      </div>

      <div class="mt-8 pt-8 border-t border-gray-light text-center text-sm text-gray-dark">
        <p>&copy; {{ new Date().getFullYear() }} Clothes Store. All rights reserved.</p>
      </div>
    </div>
  </footer>
</template>

<script setup>
</script>



