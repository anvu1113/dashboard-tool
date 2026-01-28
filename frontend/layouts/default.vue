<template>
  <div class="min-h-screen flex flex-col font-sans text-text">
    <!-- Navbar -->
    <nav class="border-b border-border-dark bg-bg-dark/80 backdrop-blur-md sticky top-0 z-50">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex items-center justify-between h-16">
          <div class="flex items-center">
            <NuxtLink to="/" class="text-2xl font-bold bg-gradient-to-r from-blue-400 to-blue-600 bg-clip-text text-transparent">
              ExtensionHub
            </NuxtLink>
            <div class="hidden md:block ml-10">
              <div class="flex items-baseline space-x-4">
                <NuxtLink to="/" active-class="text-white bg-gray-800" class="text-gray-300 hover:text-white hover:bg-gray-800 px-3 py-2 rounded-md text-sm font-medium transition-colors">Home</NuxtLink>
                <NuxtLink to="/features" active-class="text-white bg-gray-800" class="text-gray-300 hover:text-white hover:bg-gray-800 px-3 py-2 rounded-md text-sm font-medium transition-colors">Tính năng</NuxtLink>
                <NuxtLink to="/pricing" active-class="text-white bg-gray-800" class="text-gray-300 hover:text-white hover:bg-gray-800 px-3 py-2 rounded-md text-sm font-medium transition-colors">Bảng giá</NuxtLink>
                <NuxtLink to="/contact" active-class="text-white bg-gray-800" class="text-gray-300 hover:text-white hover:bg-gray-800 px-3 py-2 rounded-md text-sm font-medium transition-colors">Liên hệ</NuxtLink>
              </div>
            </div>
          </div>
          <div>
             <NuxtLink to="/admin/login" class="bg-primary hover:bg-primary-hover text-white px-4 py-2 rounded-lg text-sm font-medium transition-all shadow-lg hover:shadow-primary/50">
              Đăng nhập
            </NuxtLink>
          </div>
        </div>
      </div>
    </nav>

    <!-- Main Content -->
    <main class="flex-grow">
      <slot />
    </main>

    <!-- Footer -->
    <footer class="border-t border-border-dark bg-bg-dark pt-12 pb-8">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 md:grid-cols-4 gap-8 mb-8">
          <div class="col-span-1 md:col-span-2">
            <h3 class="text-xl font-bold text-white mb-4">ExtensionHub</h3>
            <p class="text-gray-400 max-w-sm">
              Giải pháp Chrome Extension toàn diện cho việc đặt hàng Taobao, 1688 nhanh chóng và chính xác.
            </p>
          </div>
          <div>
            <h4 class="text-white font-semibold mb-4">Sản phẩm</h4>
            <ul class="space-y-2">
              <li><NuxtLink to="/features" class="text-gray-400 hover:text-white transition-colors">Tính năng</NuxtLink></li>
              <li><NuxtLink to="/pricing" class="text-gray-400 hover:text-white transition-colors">Bảng giá</NuxtLink></li>
              <li><a href="#" class="text-gray-400 hover:text-white transition-colors">Hướng dẫn sử dụng</a></li>
            </ul>
          </div>
          <div>
            <h4 class="text-white font-semibold mb-4">Hỗ trợ</h4>
            <ul class="space-y-2">
              <li><NuxtLink to="/contact" class="text-gray-400 hover:text-white transition-colors">Liên hệ</NuxtLink></li>
              <li><a href="#" class="text-gray-400 hover:text-white transition-colors">Điều khoản</a></li>
              <li><a href="#" class="text-gray-400 hover:text-white transition-colors">Chính sách bảo mật</a></li>
            </ul>
          </div>
        </div>
        <div class="border-t border-gray-800 pt-8 flex flex-col md:flex-row justify-between items-center text-sm text-gray-500">
          <p>&copy; 2024 ExtensionHub. All rights reserved.</p>
        </div>
      </div>
    </footer>
  </div>
</template>
