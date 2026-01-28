<template>
  <div>
    <!-- Header -->
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold bg-gradient-to-r from-white to-gray-200 bg-clip-text text-transparent">
        Quản lý người dùng
      </h1>
      <button class="bg-gradient-to-r from-green-500 to-green-600 text-white px-6 py-3 rounded-lg hover:shadow-lg hover:shadow-green-500/50 transition-all duration-200 font-medium flex items-center gap-2">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
        </svg>
        Thêm mới
      </button>
    </div>

    <!-- Filters/Search -->
    <div class="mb-6 flex gap-4">
      <div class="relative flex-1 max-w-md">
        <input 
          type="text" 
          placeholder="Tìm kiếm theo email, tên..." 
          class="block w-full bg-card-dark border border-gray-600 text-white rounded-lg py-3 pl-10 pr-4 focus:ring-2 focus:ring-primary focus:border-transparent outline-none"
        >
        <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
          <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" /></svg>
        </div>
      </div>
       <select class="bg-card-dark border border-gray-600 text-white rounded-lg px-4 focus:ring-2 focus:ring-primary focus:border-transparent outline-none">
          <option>Tất cả trạng thái</option>
          <option>Active</option>
          <option>Disabled</option>
      </select>
    </div>

    <!-- Table -->
    <div class="bg-card-dark rounded-lg shadow-xl border border-gray-700/50 overflow-hidden">
      <table class="min-w-full divide-y divide-gray-700/50">
        <thead class="bg-gray-800/50">
          <tr>
            <th class="px-6 py-4 text-left text-xs font-semibold text-gray-300 uppercase tracking-wider">Email</th>
            <th class="px-6 py-4 text-left text-xs font-semibold text-gray-300 uppercase tracking-wider">Tên</th>
            <th class="px-6 py-4 text-left text-xs font-semibold text-gray-300 uppercase tracking-wider">Gói cước</th>
            <th class="px-6 py-4 text-left text-xs font-semibold text-gray-300 uppercase tracking-wider">Ngày tạo</th>
             <th class="px-6 py-4 text-left text-xs font-semibold text-gray-300 uppercase tracking-wider">Trạng thái</th>
            <th class="px-6 py-4 text-right text-xs font-semibold text-gray-300 uppercase tracking-wider">Hành động</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-gray-700/50">
          <tr v-for="i in 5" :key="i" class="hover:bg-gray-700/30 transition-colors">
            <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-white">user{{i}}@example.com</td>
            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-300">User {{ i }}</td>
             <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-300">
               <span v-if="i % 2 === 0" class="px-2 py-1 bg-yellow-500/10 text-yellow-400 rounded-full text-xs font-semibold">Pro</span>
               <span v-else class="px-2 py-1 bg-gray-700 text-gray-400 rounded-full text-xs font-semibold">Free</span>
             </td>
            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-400">2024-01-28</td>
             <td class="px-6 py-4 whitespace-nowrap text-sm">
                <span class="px-2 py-1 bg-green-500/10 text-green-400 rounded-full text-xs font-semibold">Active</span>
             </td>
            <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
              <button class="text-blue-400 hover:text-blue-300 mr-4 transition-colors">Chi tiết</button>
              <button class="text-red-400 hover:text-red-300 transition-colors">Khóa</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    
     <!-- Pagination placeholder -->
    <div class="flex justify-between items-center mt-4 text-gray-400 text-sm">
      <span>Hiển thị 1-5 của 120 kết quả</span>
      <div class="flex gap-2">
        <button class="px-3 py-1 border border-gray-700 rounded hover:bg-gray-800 disabled:opacity-50" disabled>Previous</button>
        <button class="px-3 py-1 border border-gray-700 rounded hover:bg-gray-800">Next</button>
      </div>
    </div>
  </div>
</template>

<script setup>
definePageMeta({
  layout: 'admin'
})
useHead({
  title: 'Quản lý người dùng - Admin'
})
</script>
