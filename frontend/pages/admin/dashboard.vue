<template>
  <div class="space-y-6">
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold bg-gradient-to-r from-white to-gray-200 bg-clip-text text-transparent">
        Dashboard
      </h1>
      <div class="flex items-center gap-2 text-sm text-gray-400">
        <span>Last updated: just now</span>
        <button class="p-1 hover:text-white transition-colors">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" /></svg>
        </button>
      </div>
    </div>

    <!-- Stats Grid -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      <div class="bg-card-dark border border-gray-700/50 rounded-xl p-6 shadow-xl relative overflow-hidden group">
        <div class="absolute top-0 right-0 p-4 opacity-10 group-hover:opacity-20 transition-opacity">
           <svg class="w-16 h-16 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z" /></svg>
        </div>
        <h3 class="text-gray-400 font-medium mb-2">Tổng người dùng</h3>
        <p class="text-3xl font-bold text-white mb-2">1,234</p>
        <div class="flex items-center text-sm text-green-400">
           <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6" /></svg>
           +12% so với tháng trước
        </div>
      </div>

       <div class="bg-card-dark border border-gray-700/50 rounded-xl p-6 shadow-xl relative overflow-hidden group">
        <div class="absolute top-0 right-0 p-4 opacity-10 group-hover:opacity-20 transition-opacity">
           <svg class="w-16 h-16 text-purple-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" /></svg>
        </div>
        <h3 class="text-gray-400 font-medium mb-2">Request hôm nay</h3>
        <p class="text-3xl font-bold text-white mb-2">45,678</p>
        <div class="flex items-center text-sm text-green-400">
           <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6" /></svg>
           +5% so với hôm qua
        </div>
      </div>

       <div class="bg-card-dark border border-gray-700/50 rounded-xl p-6 shadow-xl relative overflow-hidden group">
        <div class="absolute top-0 right-0 p-4 opacity-10 group-hover:opacity-20 transition-opacity">
           <svg class="w-16 h-16 text-red-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
        </div>
        <h3 class="text-gray-400 font-medium mb-2">License sắp hết hạn</h3>
        <p class="text-3xl font-bold text-white mb-2">23</p>
        <div class="flex items-center text-sm text-red-400">
           Cần chú ý
        </div>
      </div>
    </div>

    <!-- Recent Activity Table -->
    <div class="bg-card-dark rounded-xl border border-gray-700/50 shadow-xl overflow-hidden mt-8">
      <div class="p-6 border-b border-gray-700/50 flex justify-between items-center">
        <h3 class="text-lg font-bold text-white">Hoạt động gần đây</h3>
        <NuxtLink to="/admin/usage" class="text-primary hover:text-primary-hover text-sm font-medium">Xem tất cả</NuxtLink>
      </div>
      <div class="overflow-x-auto">
        <table class="w-full text-left">
          <thead class="bg-gray-800/50 text-gray-400 text-xs uppercase">
            <tr>
              <th class="px-6 py-4 font-semibold">User</th>
              <th class="px-6 py-4 font-semibold">Action</th>
              <th class="px-6 py-4 font-semibold">Time</th>
              <th class="px-6 py-4 font-semibold">Status</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-700/50 text-sm">
            <tr class="hover:bg-gray-700/30 transition-colors">
              <td class="px-6 py-4 font-medium text-white">nguyenvana</td>
              <td class="px-6 py-4 text-gray-300">Translate Product</td>
              <td class="px-6 py-4 text-gray-400">2 mins ago</td>
              <td class="px-6 py-4"><span class="px-2 py-1 bg-green-500/10 text-green-400 rounded-full text-xs font-semibold">Success</span></td>
            </tr>
             <tr class="hover:bg-gray-700/30 transition-colors">
              <td class="px-6 py-4 font-medium text-white">tranthib</td>
              <td class="px-6 py-4 text-gray-300">Get Exchange Rate</td>
              <td class="px-6 py-4 text-gray-400">5 mins ago</td>
              <td class="px-6 py-4"><span class="px-2 py-1 bg-green-500/10 text-green-400 rounded-full text-xs font-semibold">Success</span></td>
            </tr>
             <tr class="hover:bg-gray-700/30 transition-colors">
              <td class="px-6 py-4 font-medium text-white">lethic</td>
              <td class="px-6 py-4 text-gray-300">Analyze Shop</td>
              <td class="px-6 py-4 text-gray-400">12 mins ago</td>
              <td class="px-6 py-4"><span class="px-2 py-1 bg-red-500/10 text-red-400 rounded-full text-xs font-semibold">Failed</span></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script setup>
definePageMeta({
  layout: 'admin',
  // middleware: 'admin-auth' // Uncomment when middleware is ready
})

useHead({
  title: 'Dashboard - Admin Panel'
})
</script>
