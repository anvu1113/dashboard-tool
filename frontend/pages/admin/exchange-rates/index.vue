<template>
  <div>
    <!-- Header -->
    <div class="flex justify-between items-center mb-6">
      <div>
        <h1 class="text-3xl font-bold bg-gradient-to-r from-white to-gray-200 bg-clip-text text-transparent">
          Quản lý Tỉ Giá Hối Đoái
        </h1>
        <p class="text-gray-400 text-sm mt-2" v-if="rates.length > 0">
          Cập nhật lần cuối: {{ formatDateTime(getLatestUpdate()) }}
        </p>
      </div>
      <div class="flex gap-3">
        <button 
          @click="syncRates" 
          :disabled="isSyncing"
          class="bg-gradient-to-r from-green-500 to-green-600 text-white px-6 py-3 rounded-lg hover:shadow-lg hover:shadow-green-500/50 transition-all duration-200 font-medium flex items-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed"
        >
          <svg v-if="!isSyncing" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" /></svg>
          <svg v-else class="w-5 h-5 animate-spin" fill="none" stroke="currentColor" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
          {{ isSyncing ? 'Đang đồng bộ...' : 'Đồng bộ từ Vietcombank' }}
        </button>
        <button 
          @click="openModal()" 
          class="bg-gradient-to-r from-blue-500 to-blue-600 text-white px-6 py-3 rounded-lg hover:shadow-lg hover:shadow-blue-500/50 transition-all duration-200 font-medium flex items-center gap-2"
        >
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" /></svg>
          Thêm Tỉ Giá
        </button>
      </div>
    </div>

    <!-- Exchange Rates Table -->
    <div class="bg-card-dark border border-gray-700/50 rounded-xl overflow-hidden shadow-xl">
      <div class="overflow-x-auto">
        <table class="w-full text-left border-collapse">
          <thead class="bg-gray-800/50 text-gray-400 uppercase text-xs">
            <tr>
              <th class="px-6 py-4 font-semibold tracking-wider">Mã tiền tệ</th>
              <th class="px-6 py-4 font-semibold tracking-wider">Tên tiền tệ</th>
              <th class="px-6 py-4 font-semibold tracking-wider text-right">Mua vào</th>
              <th class="px-6 py-4 font-semibold tracking-wider text-right">Chuyển khoản</th>
              <th class="px-6 py-4 font-semibold tracking-wider text-right">Bán ra</th>
              <th class="px-6 py-4 font-semibold tracking-wider">Cập nhật</th>
              <th class="px-6 py-4 font-semibold tracking-wider text-right">Hành động</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-700/50">
            <tr v-for="rate in rates" :key="rate.id" class="hover:bg-gray-700/20 transition-colors">
              <td class="px-6 py-4 font-bold text-blue-400">{{ rate.currency_code }}</td>
              <td class="px-6 py-4 text-white">{{ rate.currency_name }}</td>
              <td class="px-6 py-4 text-gray-300 text-sm text-right font-mono">
                {{ formatRate(rate.buy_rate) }}
              </td>
              <td class="px-6 py-4 text-gray-300 text-sm text-right font-mono">
                {{ formatRate(rate.transfer_rate) }}
              </td>
              <td class="px-6 py-4 text-gray-300 text-sm text-right font-mono">
                {{ formatRate(rate.sell_rate) }}
              </td>
              <td class="px-6 py-4 text-gray-400 text-xs">
                {{ formatDateTime(rate.updated_at) }}
              </td>
              <td class="px-6 py-4 text-right space-x-2">
                <button @click="editRate(rate)" class="text-blue-400 hover:text-blue-300 transition-colors">Sửa</button>
                <button @click="deleteRate(rate.id)" class="text-red-400 hover:text-red-300 transition-colors">Xóa</button>
              </td>
            </tr>
            <tr v-if="rates.length === 0 && !isLoading">
              <td colspan="7" class="px-6 py-8 text-center text-gray-500">
                Chưa có tỉ giá nào. Nhấn "Đồng bộ từ Vietcombank" để lấy dữ liệu.
              </td>
            </tr>
            <tr v-if="isLoading">
              <td colspan="7" class="px-6 py-8 text-center text-gray-500">
                <div class="flex items-center justify-center gap-2">
                  <svg class="w-5 h-5 animate-spin" fill="none" stroke="currentColor" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
                  Đang tải...
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- Modal Form -->
    <div v-if="showModal" class="fixed inset-0 z-50 flex items-center justify-center bg-black/50 backdrop-blur-sm">
      <div class="bg-card-dark border border-gray-700 w-full max-w-md p-6 rounded-xl shadow-2xl">
        <h2 class="text-xl font-bold text-white mb-4">{{ isEditing ? 'Cập nhật Tỉ Giá' : 'Thêm Tỉ Giá Mới' }}</h2>
        <form @submit.prevent="submitForm" class="space-y-4">
          <div>
            <label class="block text-sm text-gray-400 mb-1">Mã tiền tệ <span class="text-red-500">*</span></label>
            <input 
              v-model="form.currency_code" 
              :disabled="isEditing"
              class="w-full bg-bg-dark border border-gray-600 rounded p-2 text-white placeholder-gray-600 uppercase disabled:opacity-50" 
              placeholder="USD" 
              maxlength="10"
              required
            >
          </div>

          <div>
            <label class="block text-sm text-gray-400 mb-1">Tên tiền tệ <span class="text-red-500">*</span></label>
            <input 
              v-model="form.currency_name" 
              class="w-full bg-bg-dark border border-gray-600 rounded p-2 text-white placeholder-gray-600" 
              placeholder="Đô la Mỹ"
              required
            >
          </div>

          <div class="grid grid-cols-3 gap-4">
            <div>
              <label class="block text-sm text-gray-400 mb-1">Mua vào</label>
              <input 
                v-model.number="form.buy_rate" 
                type="number"
                step="0.01"
                class="w-full bg-bg-dark border border-gray-600 rounded p-2 text-white placeholder-gray-600" 
                placeholder="0.00"
              >
            </div>
            <div>
              <label class="block text-sm text-gray-400 mb-1">Chuyển khoản</label>
              <input 
                v-model.number="form.transfer_rate" 
                type="number"
                step="0.01"
                class="w-full bg-bg-dark border border-gray-600 rounded p-2 text-white placeholder-gray-600" 
                placeholder="0.00"
              >
            </div>
            <div>
              <label class="block text-sm text-gray-400 mb-1">Bán ra</label>
              <input 
                v-model.number="form.sell_rate" 
                type="number"
                step="0.01"
                class="w-full bg-bg-dark border border-gray-600 rounded p-2 text-white placeholder-gray-600" 
                placeholder="0.00"
              >
            </div>
          </div>

          <div class="flex justify-end gap-3 mt-6">
            <button type="button" @click="showModal = false" class="px-4 py-2 text-gray-400 hover:text-white transition-colors">Hủy</button>
            <button type="submit" class="px-6 py-2 bg-blue-600 hover:bg-blue-500 text-white rounded-lg transition-colors font-medium">Lưu</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
definePageMeta({
  layout: 'admin',
  permissions: ['exchange_rates.view']
})

const rates = ref([])
const showModal = ref(false)
const isEditing = ref(false)
const isLoading = ref(false)
const isSyncing = ref(false)

const form = ref({
  id: null,
  currency_code: '',
  currency_name: '',
  buy_rate: null,
  transfer_rate: null,
  sell_rate: null
})

const { token } = useAuth()
const toast = useToast()
const { confirmDelete, alert } = useConfirm()

const fetchRates = async () => {
  isLoading.value = true
  try {
    const data = await $fetch('/api/admin/exchange-rates/', {
      headers: {
        Authorization: `Bearer ${token.value}`
      }
    })
    rates.value = data
  } catch (e) {
    console.error('Fetch error:', e)
    if (e.response?.status === 401 || e.response?.status === 403) {
      await alert('Phiên đăng nhập hết hạn hoặc không có quyền. Vui lòng đăng nhập lại.', 'Lỗi Xác Thực')
      navigateTo('/admin/login')
    } else {
      toast.error('Không thể tải danh sách tỉ giá')
    }
  } finally {
    isLoading.value = false
  }
}

const formatRate = (rate) => {
  if (rate === null || rate === undefined) return '-'
  return new Intl.NumberFormat('vi-VN', {
    minimumFractionDigits: 0,
    maximumFractionDigits: 2
  }).format(rate)
}

const formatDateTime = (dateString) => {
  if (!dateString) return ''
  const date = new Date(dateString)
  return new Intl.DateTimeFormat('vi-VN', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit'
  }).format(date)
}

const getLatestUpdate = () => {
  if (rates.value.length === 0) return null
  return rates.value.reduce((latest, rate) => {
    return new Date(rate.updated_at) > new Date(latest) ? rate.updated_at : latest
  }, rates.value[0].updated_at)
}

const openModal = () => {
  isEditing.value = false
  form.value = {
    currency_code: '',
    currency_name: '',
    buy_rate: null,
    transfer_rate: null,
    sell_rate: null
  }
  showModal.value = true
}

const editRate = (rate) => {
  isEditing.value = true
  form.value = { ...rate }
  showModal.value = true
}

const submitForm = async () => {
  try {
    const headers = { Authorization: `Bearer ${token.value}` }
    
    // Clean up form data
    const payload = {
      ...form.value,
      buy_rate: form.value.buy_rate || null,
      transfer_rate: form.value.transfer_rate || null,
      sell_rate: form.value.sell_rate || null
    }
    
    if (isEditing.value) {
      await $fetch(`/api/admin/exchange-rates/${form.value.id}`, {
        method: 'PUT',
        body: payload,
        headers
      })
      toast.success('Cập nhật tỉ giá thành công')
    } else {
      await $fetch('/api/admin/exchange-rates/', {
        method: 'POST',
        body: payload,
        headers
      })
      toast.success('Thêm tỉ giá thành công')
    }
    
    showModal.value = false
    fetchRates()
  } catch (e) {
    toast.error('Có lỗi xảy ra: ' + (e.data?.detail || e.message))
  }
}

const deleteRate = async (id) => {
  const isConfirmed = await confirmDelete()
  if (isConfirmed) {
    try {
      await $fetch(`/api/admin/exchange-rates/${id}`, {
        method: 'DELETE',
        headers: { Authorization: `Bearer ${token.value}` }
      })
      toast.success('Xóa tỉ giá thành công')
      fetchRates()
    } catch (e) {
      toast.error('Có lỗi khi xóa: ' + (e.data?.detail || e.message))
    }
  }
}

const syncRates = async () => {
  isSyncing.value = true
  try {
    const result = await $fetch('/api/admin/exchange-rates/sync', {
      method: 'POST',
      headers: { Authorization: `Bearer ${token.value}` }
    })
    toast.success(result.message)
    fetchRates()
  } catch (e) {
    toast.error('Đồng bộ thất bại: ' + (e.data?.detail || e.message))
  } finally {
    isSyncing.value = false
  }
}

onMounted(() => {
  fetchRates()
})
</script>
