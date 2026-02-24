<template>
  <div>
    <!-- Header -->
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold bg-gradient-to-r from-white to-gray-200 bg-clip-text text-transparent">
        Quản lý License
      </h1>
       <button class="bg-gradient-to-r from-blue-500 to-blue-600 text-white px-6 py-3 rounded-lg hover:shadow-lg hover:shadow-blue-500/50 transition-all duration-200 font-medium flex items-center gap-2">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" /></svg>
        Cấp License Mới
      </button>
    </div>

    <!-- Table -->
    <div class="bg-card-dark rounded-lg shadow-xl border border-gray-700/50 overflow-hidden">
      <table class="min-w-full divide-y divide-gray-700/50">
        <thead class="bg-gray-800/50">
          <tr>
            <th class="px-6 py-4 text-left text-xs font-semibold text-gray-300 uppercase tracking-wider">License Key</th>
            <th class="px-6 py-4 text-left text-xs font-semibold text-gray-300 uppercase tracking-wider">Người dùng</th>
            <th class="px-6 py-4 text-left text-xs font-semibold text-gray-300 uppercase tracking-wider">Loại</th>
            <th class="px-6 py-4 text-left text-xs font-semibold text-gray-300 uppercase tracking-wider">Ngày hết hạn</th>
            <th class="px-6 py-4 text-left text-xs font-semibold text-gray-300 uppercase tracking-wider">Trạng thái</th>
            <th class="px-6 py-4 text-right text-xs font-semibold text-gray-300 uppercase tracking-wider">Hành động</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-gray-700/50">
          <tr v-for="i in 5" :key="i" class="hover:bg-gray-700/30 transition-colors">
            <td class="px-6 py-4 whitespace-nowrap text-sm font-mono text-blue-400">XXXX-YYYY-ZZZZ-{{i}}</td>
            <td class="px-6 py-4 whitespace-nowrap text-sm text-white">user{{i}}@example.com</td>
            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-300">Pro 1 Tháng</td>
            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-400">2024-02-28</td>
             <td class="px-6 py-4 whitespace-nowrap text-sm">
                <span v-if="i === 3" class="px-2 py-1 bg-red-500/10 text-red-400 rounded-full text-xs font-semibold">Expired</span>
                <span v-else class="px-2 py-1 bg-green-500/10 text-green-400 rounded-full text-xs font-semibold">Active</span>
             </td>
            <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
              <button class="text-green-400 hover:text-green-300 mr-4 transition-colors">Gia hạn</button>
              <button class="text-red-400 hover:text-red-300 transition-colors">Thu hồi</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
definePageMeta({
  layout: 'admin',
  permissions: ['licenses.view']
})
useHead({
  title: 'Quản lý License - Admin'
})
</script>
