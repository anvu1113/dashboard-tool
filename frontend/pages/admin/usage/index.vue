<template>
  <div>
    <!-- Header -->
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold bg-gradient-to-r from-white to-gray-200 bg-clip-text text-transparent">
        Nhật ký sử dụng (Usage Logs)
      </h1>
       <div class="flex gap-2">
         <input type="date" class="bg-card-dark border border-gray-600 text-white rounded-lg px-3 py-2 outline-none focus:border-primary">
         <button class="bg-gray-700 hover:bg-gray-600 text-white px-4 py-2 rounded-lg transition-colors">Lọc</button>
       </div>
    </div>

    <!-- Table -->
    <div class="bg-card-dark rounded-lg shadow-xl border border-gray-700/50 overflow-hidden">
      <table class="min-w-full divide-y divide-gray-700/50">
        <thead class="bg-gray-800/50">
          <tr>
            <th class="px-6 py-4 text-left text-xs font-semibold text-gray-300 uppercase tracking-wider">Thời gian</th>
            <th class="px-6 py-4 text-left text-xs font-semibold text-gray-300 uppercase tracking-wider">User</th>
            <th class="px-6 py-4 text-left text-xs font-semibold text-gray-300 uppercase tracking-wider">Action</th>
            <th class="px-6 py-4 text-left text-xs font-semibold text-gray-300 uppercase tracking-wider">Chi tiết</th>
             <th class="px-6 py-4 text-left text-xs font-semibold text-gray-300 uppercase tracking-wider">Status</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-gray-700/50">
          <tr v-for="i in 10" :key="i" class="hover:bg-gray-700/30 transition-colors">
            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-400">2024-01-28 10:30:{{i}}</td>
            <td class="px-6 py-4 whitespace-nowrap text-sm text-white">user{{i}}@example.com</td>
            <td class="px-6 py-4 whitespace-nowrap text-sm text-blue-400">Translate Text</td>
             <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-400 truncate max-w-xs">{ "text": "...", "lang": "vi" }</td>
            <td class="px-6 py-4 whitespace-nowrap text-sm">
                <span class="px-2 py-1 bg-green-500/10 text-green-400 rounded-full text-xs font-semibold">200 OK</span>
             </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
definePageMeta({
  layout: 'admin'
})
useHead({
  title: 'Log sử dụng - Admin'
})
</script>
