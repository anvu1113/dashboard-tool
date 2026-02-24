<template>
  <div>
    <!-- Header -->
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold bg-gradient-to-r from-white to-gray-200 bg-clip-text text-transparent">
        Nhật ký sử dụng (Usage Logs)
      </h1>
       <div class="flex gap-2">
         <input 
            v-model="dateFilter" 
            type="date" 
            class="bg-card-dark border border-gray-600 text-white rounded-lg px-3 py-2 outline-none focus:border-primary"
         >
         <button 
            @click="refresh" 
            class="bg-gray-700 hover:bg-gray-600 text-white px-4 py-2 rounded-lg transition-colors"
         >
            Lọc
         </button>
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
             <th class="px-6 py-4 text-left text-xs font-semibold text-gray-300 uppercase tracking-wider">Engine</th>
             <th class="px-6 py-4 text-left text-xs font-semibold text-gray-300 uppercase tracking-wider">Latency</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-gray-700/50">
          <tr v-if="pending">
             <td colspan="6" class="px-6 py-4 text-center text-gray-400">Đang tải...</td>
          </tr>
          <tr v-else-if="error">
             <td colspan="6" class="px-6 py-4 text-center text-red-400">Error: {{ error }}</td>
          </tr>
          <tr v-else-if="logItems && logItems.length === 0">
             <td colspan="6" class="px-6 py-4 text-center text-gray-400">Không có dữ liệu.</td>
          </tr>
          <tr v-for="log in logItems" :key="log.id" class="hover:bg-gray-700/30 transition-colors">
            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-400">
                {{ new Date(log.created_at).toLocaleString('vi-VN') }}
            </td>
            <td class="px-6 py-4 whitespace-nowrap text-sm text-white">
                {{ log.user_email }}
            </td>
            <td class="px-6 py-4 whitespace-nowrap text-sm text-blue-400">
                {{ log.action }}
            </td>
             <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-400 truncate max-w-xs">
                 <div class="flex flex-col text-xs">
                     <span>{{ log.source_lang }} -> {{ log.target_lang }}</span>
                     <span>Chars: {{ log.char_count }}</span>
                 </div>
             </td>
            <td class="px-6 py-4 whitespace-nowrap text-sm">
                <span class="px-2 py-1 bg-gray-700 text-gray-300 rounded-full text-xs font-semibold capitalize">{{ log.engine }}</span>
             </td>
             <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-400">
                 {{ log.latency_ms }}ms
             </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Pagination -->
    <div class="flex justify-between items-center mt-4 text-gray-400 text-sm">
      <span>Trang {{ page }} / {{ totalPages }}</span>
      <div class="flex gap-2">
        <button @click="page--" :disabled="page <= 1" class="px-3 py-1 border border-gray-700 rounded hover:bg-gray-800 disabled:opacity-50 disabled:cursor-not-allowed">Previous</button>
        <button @click="page++" :disabled="page >= totalPages" class="px-3 py-1 border border-gray-700 rounded hover:bg-gray-800 disabled:opacity-50 disabled:cursor-not-allowed">Next</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'

definePageMeta({
  layout: 'admin',
  permissions: ['usage.view']
})
useHead({
  title: 'Log sử dụng - Admin'
})

const config = useRuntimeConfig()
const page = ref(1)
const limit = ref(20)
const dateFilter = ref('')

const { token } = useAuth()

const { data: responseData, pending, refresh, error } = await useFetch('/api/admin/usage', {
    query: {
        page: page,
        limit: limit,
        date: dateFilter.value ? dateFilter.value : undefined // Send undefined if empty to avoid validation error
    },
    headers: {
        Authorization: `Bearer ${token.value}`
    },
    watch: [page], // Auto refresh only on page change, date changed by manual button or we can add it here
    server: false // Force client-side fetch to debug why SSR is failing (auth token?) or network
})

const logItems = computed(() => responseData.value?.data || [])
const totalPages = computed(() => responseData.value?.total_pages || 1)

// If we want manual button for date filter, we keep it as is.
// Or we can add dateFilter to watch list for auto-refresh.
// Current implementation: dateFilter is in query, so refresh() will pick it up. 
// Button calls refresh().

</script>
