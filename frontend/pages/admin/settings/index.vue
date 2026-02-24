<template>
  <div class="max-w-4xl">
    <!-- Header -->
    <div class="mb-8">
      <h1 class="text-3xl font-bold bg-gradient-to-r from-white to-gray-200 bg-clip-text text-transparent">
        Cài đặt hệ thống
      </h1>
      <p class="text-gray-400 mt-2">Cấu hình các tham số toàn hệ thống</p>
    </div>

    <!-- Settings Forms -->
    <div class="space-y-8">
      <!-- General Config -->
      <div class="bg-card-dark rounded-lg shadow-xl border border-gray-700/50 p-6">
        <h2 class="text-xl font-bold text-white mb-6 flex items-center gap-2">
          <svg class="w-5 h-5 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" /><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" /></svg>
          Cấu hình chung
        </h2>
        <div class="grid gap-6">
          <div class="flex items-center justify-between p-4 bg-bg-dark rounded-lg border border-gray-700 transition-colors hover:border-blue-500/50">
             <div>
               <h4 class="text-white font-medium">Bảo trì hệ thống</h4>
               <p class="text-sm text-gray-400">Tạm ngưng tất cả truy cập từ extension</p>
             </div>
             <label class="relative inline-flex items-center cursor-pointer">
              <input type="checkbox" value="" class="sr-only peer">
              <div class="w-11 h-6 bg-gray-700 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-800 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-blue-600"></div>
            </label>
          </div>

           <div class="flex items-center justify-between p-4 bg-bg-dark rounded-lg border border-gray-700 transition-colors hover:border-blue-500/50">
             <div>
               <h4 class="text-white font-medium">Cho phép đăng ký mới</h4>
               <p class="text-sm text-gray-400">Người dùng có thể tự tạo tài khoản</p>
             </div>
             <label class="relative inline-flex items-center cursor-pointer">
              <input type="checkbox" value="" class="sr-only peer" checked>
              <div class="w-11 h-6 bg-gray-700 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-800 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-blue-600"></div>
            </label>
          </div>
        </div>
      </div>

      <!-- Quota Config -->
      <div class="bg-card-dark rounded-lg shadow-xl border border-gray-700/50 p-6">
        <h2 class="text-xl font-bold text-white mb-6 flex items-center gap-2">
           <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6" /></svg>
          Giới hạn dung lượng (Quota)
        </h2>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div>
            <label class="block text-sm font-medium text-gray-300 mb-2">Free Trial Request Limit (Daily)</label>
            <input type="number" class="block w-full bg-bg-dark border border-gray-600 text-white rounded-lg py-3 px-4 focus:ring-2 focus:ring-primary focus:border-transparent outline-none" value="50">
          </div>
          <div>
             <label class="block text-sm font-medium text-gray-300 mb-2">Pro Request Limit (Daily)</label>
            <input type="number" class="block w-full bg-bg-dark border border-gray-600 text-white rounded-lg py-3 px-4 focus:ring-2 focus:ring-primary focus:border-transparent outline-none" value="5000">
          </div>
           <div>
             <label class="block text-sm font-medium text-gray-300 mb-2">Thời gian dùng thử (Ngày)</label>
            <input type="number" class="block w-full bg-bg-dark border border-gray-600 text-white rounded-lg py-3 px-4 focus:ring-2 focus:ring-primary focus:border-transparent outline-none" value="3">
          </div>
        </div>
      </div>

      <div class="flex justify-end gap-4 pt-4 border-t border-gray-700">
        <button class="px-6 py-3 border-2 border-gray-600 text-gray-300 rounded-lg hover:border-gray-500 hover:text-white font-medium transition-colors">
          Hủy bỏ
        </button>
        <button class="inline-flex justify-center items-center gap-2 py-3 px-8 min-w-[150px] bg-gradient-to-r from-blue-500 to-blue-600 text-white rounded-lg shadow-lg hover:shadow-blue-500/50 font-medium transition-all">
          Lưu cài đặt
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
definePageMeta({
  layout: 'admin',
  permissions: ['settings.view']
})
useHead({
  title: 'Cài đặt - Admin'
})
</script>
