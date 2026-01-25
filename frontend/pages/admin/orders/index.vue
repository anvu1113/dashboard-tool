<template>
  <div>
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold bg-gradient-to-r from-white to-gray-200 bg-clip-text text-transparent">Quản lý đơn hàng</h1>
    </div>

    <div class="bg-gray-800/50 backdrop-blur-xl rounded-lg shadow-xl border border-gray-700/50 overflow-hidden">
        <div class="overflow-x-auto">
      <table class="min-w-full divide-y divide-gray-700/50">
        <thead class="bg-gray-700/30">
          <tr>
            <th class="px-6 py-4 text-left text-xs font-semibold text-gray-300 uppercase tracking-wider">ID</th>
            <th class="px-6 py-4 text-left text-xs font-semibold text-gray-300 uppercase tracking-wider">Khách hàng</th>
            <th class="px-6 py-4 text-left text-xs font-semibold text-gray-300 uppercase tracking-wider">Tổng tiền</th>
            <th class="px-6 py-4 text-left text-xs font-semibold text-gray-300 uppercase tracking-wider">Trạng thái</th>
            <th class="px-6 py-4 text-left text-xs font-semibold text-gray-300 uppercase tracking-wider">Ngày tạo</th>
            <th class="px-6 py-4 text-right text-xs font-semibold text-gray-300 uppercase tracking-wider">Thao tác</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-gray-700/50">
          <tr v-for="order in orders" :key="order.id" class="hover:bg-gray-700/30 transition-colors">
            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-400 font-mono">#{{ order.id }}</td>
            <td class="px-6 py-4 whitespace-nowrap text-sm">
                <div class="font-semibold text-white">{{ order.contact_name || order.user?.name || 'Khách lẻ' }}</div>
                <div class="text-xs text-gray-400">{{ order.contact_phone }}</div>
            </td>
            <td class="px-6 py-4 whitespace-nowrap text-sm text-primary font-semibold">
                {{ formatPrice(order.total_price) }}
            </td>
            <td class="px-6 py-4 whitespace-nowrap">
              <div class="flex flex-col gap-1">
                <span :class="getStatusClass(order.status)" class="px-3 py-1 inline-flex text-xs leading-5 font-semibold rounded-full border w-fit">
                  {{ order.status }}
                </span>
                <span :class="order.order_type === 'proxy' ? 'bg-orange-500/20 text-orange-400 border-orange-500/50' : 'bg-blue-500/20 text-blue-400 border-blue-500/50'" class="px-3 py-1 inline-flex text-xs leading-5 font-semibold rounded-full border w-fit">
                  {{ order.order_type === 'proxy' ? 'Order Hộ' : 'Mua Trực Tiếp' }}
                </span>
              </div>
            </td>
            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-400">
              {{ formatDate(order.created_at) }}
            </td>
            <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
              <button 
                @click="openOrder(order.id)" 
                class="inline-flex items-center gap-1 text-blue-400 hover:text-blue-300 transition-colors"
              >
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                </svg>
                Chi tiết
              </button>
            </td>
          </tr>
        </tbody>
      </table>
      </div>
      
      <div class="px-6 py-4 border-t border-gray-700/50 flex justify-end gap-2" v-if="totalPages > 1">
           <button @click="page--" :disabled="page <= 1" class="px-4 py-2 bg-gray-700 text-gray-300 rounded-lg disabled:opacity-50 hover:bg-gray-600 transition-colors">Prev</button>
           <button @click="page++" :disabled="page >= totalPages" class="px-4 py-2 bg-gray-700 text-gray-300 rounded-lg disabled:opacity-50 hover:bg-gray-600 transition-colors">Next</button>
      </div>
    </div>
  </div>
</template>

<script setup>
definePageMeta({
  layout: 'admin',
  middleware: 'auth'
})

const config = useRuntimeConfig()
const { token } = useAuth()
const orders = ref([])
const page = ref(1)
const totalPages = ref(1)

const loadOrders = async () => {
    try {
        const response = await $fetch(`${config.public.apiBase}/api/admin/orders?page=${page.value}`, {
            headers: { Authorization: `Bearer ${token.value}` }
        })
        orders.value = response.data
        totalPages.value = response.last_page
    } catch (e) {
        console.error(e)
    }
}

watch(page, loadOrders)
onMounted(loadOrders)

const formatPrice = (p) => new Intl.NumberFormat('vi-VN').format(p || 0) + ' VNĐ'
const formatDate = (d) => new Date(d).toLocaleDateString('vi-VN')

const getStatusClass = (status) => {
  const map = {
    'NEW': 'bg-yellow-500/20 text-yellow-400 border-yellow-500/50',
    'QUOTED': 'bg-blue-500/20 text-blue-400 border-blue-500/50',
    'CONFIRMED': 'bg-purple-500/20 text-purple-400 border-purple-500/50',
    'ORDERED': 'bg-indigo-500/20 text-indigo-400 border-indigo-500/50',
    'COMPLETED': 'bg-green-500/20 text-green-400 border-green-500/50',
    'CANCELED': 'bg-red-500/20 text-red-400 border-red-500/50'
  }
  return map[status] || 'bg-gray-600/20 text-gray-400 border-gray-600/50'
}

const openOrder = (id) => {
    navigateTo(`/admin/orders/${id}`)
}
</script>
