<template>
  <div>
    <h1 class="text-3xl font-bold bg-gradient-to-r from-white to-gray-200 bg-clip-text text-transparent mb-6">Dashboard</h1>
    
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
      <!-- Order Stat -->
      <div class="bg-gradient-to-br from-gray-800/50 to-gray-700/50 backdrop-blur-xl p-6 rounded-lg shadow-xl border border-gray-700/50">
        <div class="flex items-center justify-between">
          <div>
            <h3 class="text-gray-400 text-sm font-semibold uppercase">Đơn hàng mới</h3>
            <p class="text-3xl font-bold text-white mt-2">12</p>
            <NuxtLink to="/admin/orders" class="text-sm text-blue-400 hover:text-blue-300 mt-2 inline-flex items-center gap-1 transition-colors">
              Xem tất cả
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
              </svg>
            </NuxtLink>
          </div>
          <div class="w-16 h-16 bg-orange-500/20 rounded-lg flex items-center justify-center">
            <svg class="w-8 h-8 text-orange-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
            </svg>
          </div>
        </div>
      </div>
      
      <!-- Product Stat -->
      <div class="bg-gradient-to-br from-gray-800/50 to-gray-700/50 backdrop-blur-xl p-6 rounded-lg shadow-xl border border-gray-700/50">
        <div class="flex items-center justify-between">
          <div>
            <h3 class="text-gray-400 text-sm font-semibold uppercase">Sản phẩm</h3>
            <p class="text-3xl font-bold text-white mt-2">45</p>
            <NuxtLink to="/admin/products" class="text-sm text-blue-400 hover:text-blue-300 mt-2 inline-flex items-center gap-1 transition-colors">
              Quản lý
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
              </svg>
            </NuxtLink>
          </div>
          <div class="w-16 h-16 bg-blue-500/20 rounded-lg flex items-center justify-center">
            <svg class="w-8 h-8 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4" />
            </svg>
          </div>
        </div>
      </div>

      <!-- Post Stat -->
      <div class="bg-gradient-to-br from-gray-800/50 to-gray-700/50 backdrop-blur-xl p-6 rounded-lg shadow-xl border border-gray-700/50">
        <div class="flex items-center justify-between">
          <div>
            <h3 class="text-gray-400 text-sm font-semibold uppercase">Bài viết</h3>
            <p class="text-3xl font-bold text-white mt-2">8</p>
            <NuxtLink to="/admin/posts" class="text-sm text-blue-400 hover:text-blue-300 mt-2 inline-flex items-center gap-1 transition-colors">
              Quản lý
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
              </svg>
            </NuxtLink>
          </div>
          <div class="w-16 h-16 bg-purple-500/20 rounded-lg flex items-center justify-center">
            <svg class="w-8 h-8 text-purple-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9M7 16h6M7 8h6v4H7V8z" />
            </svg>
          </div>
        </div>
      </div>
    </div>
    
    <div class="bg-gradient-to-br from-gray-800/50 to-gray-700/50 backdrop-blur-xl rounded-lg shadow-xl border border-gray-700/50 p-8">
        <div class="flex items-center gap-4 mb-4">
          <div class="w-12 h-12 bg-gradient-to-br from-primary to-primary-dark rounded-lg flex items-center justify-center">
            <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
            </svg>
          </div>
          <div>
            <h2 class="text-2xl font-bold text-white">Chào mừng trở lại!</h2>
            <p class="text-gray-400 mt-1">Hệ thống quản lý đơn hàng Taobao và sản phẩm ngách.</p>
          </div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mt-6">
          <div class="flex items-center gap-3 p-4 bg-gray-700/30 rounded-lg">
            <svg class="w-8 h-8 text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <div>
              <p class="text-sm text-gray-400">Hệ thống</p>
              <p class="text-white font-semibold">Hoạt động bình thường</p>
            </div>
          </div>
          <div class="flex items-center gap-3 p-4 bg-gray-700/30 rounded-lg">
            <svg class="w-8 h-8 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <div>
              <p class="text-sm text-gray-400">Cập nhật lần cuối</p>
              <p class="text-white font-semibold">Hôm nay</p>
            </div>
          </div>
        </div>
    </div>
  </div>
</template>

<script setup>
definePageMeta({
  layout: 'admin',
  middleware: 'auth'
})
</script>
