<template>
  <div class="bg-bg-dark py-20 min-h-screen">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-16">
        <h1 class="text-4xl font-bold text-white mb-4">Bảng giá</h1>
        <p class="text-xl text-gray-400">Chọn gói phù hợp với nhu cầu của bạn</p>
      </div>

      <div class="grid md:grid-cols-3 gap-8 max-w-5xl mx-auto">
        <!-- Free Plan -->
        <div class="bg-card-dark border border-gray-700 rounded-2xl p-8 flex flex-col">
          <div class="mb-8">
            <h3 class="text-xl font-bold text-white mb-2">Miễn phí</h3>
            <div class="text-3xl font-extrabold text-white">0đ<span class="text-xl font-medium text-gray-500">/tháng</span></div>
            <p class="text-gray-400 mt-4 text-sm">Dành cho người mới bắt đầu trải nghiệm</p>
          </div>
          <ul class="space-y-4 mb-8 flex-1">
            <li class="flex items-center gap-3 text-gray-300">
              <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
              Dịch thuật cơ bản (50 lần/ngày)
            </li>
            <li class="flex items-center gap-3 text-gray-300">
              <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
              Tính giá cơ bản
            </li>
            <li class="flex items-center gap-3 text-gray-500">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" /></svg>
              Phân tích Shop
            </li>
          </ul>
          <a href="#" class="block w-full text-center py-3 bg-gray-700 hover:bg-gray-600 text-white rounded-lg font-bold transition-colors">
            Đăng ký Free
          </a>
        </div>

        <!-- Pro Plan -->
        <div class="bg-card-dark border-2 border-primary rounded-2xl p-8 flex flex-col relative transform scale-105 shadow-2xl shadow-blue-900/20">
          <div class="absolute top-0 right-0 bg-primary text-white text-xs font-bold px-3 py-1 rounded-bl-lg rounded-tr-lg">
            POPULAR
          </div>
          <div class="mb-8">
            <h3 class="text-xl font-bold text-white mb-2">Pro</h3>
            <div class="text-3xl font-extrabold text-white">199k<span class="text-xl font-medium text-gray-500">/tháng</span></div>
            <p class="text-gray-400 mt-4 text-sm">Cho dân buôn chuyên nghiệp</p>
          </div>
          <ul class="space-y-4 mb-8 flex-1">
            <li class="flex items-center gap-3 text-white">
              <svg class="w-5 h-5 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
              Dịch thuật không giới hạn
            </li>
            <li class="flex items-center gap-3 text-white">
              <svg class="w-5 h-5 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
              Tính giá nâng cao
            </li>
            <li class="flex items-center gap-3 text-white">
              <svg class="w-5 h-5 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
              Phân tích Shop chi tiết
            </li>
            <li class="flex items-center gap-3 text-white">
              <svg class="w-5 h-5 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
              Hỗ trợ ưu tiên 24/7
            </li>
          </ul>
          <a href="#" class="block w-full text-center py-3 bg-primary hover:bg-primary-hover text-white rounded-lg font-bold transition-colors shadow-lg shadow-blue-500/30">
            Dùng thử 7 ngày
          </a>
        </div>

        <!-- Team Plan -->
        <div class="bg-card-dark border border-gray-700 rounded-2xl p-8 flex flex-col">
          <div class="mb-8">
            <h3 class="text-xl font-bold text-white mb-2">Team</h3>
            <div class="text-3xl font-extrabold text-white">499k<span class="text-xl font-medium text-gray-500">/tháng</span></div>
            <p class="text-gray-400 mt-4 text-sm">Cho đội nhóm và công ty</p>
          </div>
          <ul class="space-y-4 mb-8 flex-1">
            <li class="flex items-center gap-3 text-gray-300">
              <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
              5 Tài khoản Pro
            </li>
            <li class="flex items-center gap-3 text-gray-300">
              <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
              Quản lý thành viên
            </li>
             <li class="flex items-center gap-3 text-gray-300">
              <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
              Xuất báo cáo nhóm
            </li>
            <li class="flex items-center gap-3 text-gray-300">
              <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
              API Access
            </li>
          </ul>
          <a href="#" class="block w-full text-center py-3 bg-gray-700 hover:bg-gray-600 text-white rounded-lg font-bold transition-colors">
            Liên hệ báo giá
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
useHead({
  title: 'Bảng giá - ExtensionHub',
  meta: [
    { name: 'description', content: 'Các gói cước linh hoạt phù hợp với mọi nhu cầu sử dụng.' }
  ]
})
</script>
