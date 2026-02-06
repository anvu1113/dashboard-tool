<template>
  <div>
    <!-- Header -->
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold bg-gradient-to-r from-white to-gray-200 bg-clip-text text-transparent">
        Quản lý Domain Hỗ trợ
      </h1>
      <button @click="openModal()" class="bg-gradient-to-r from-blue-500 to-blue-600 text-white px-6 py-3 rounded-lg hover:shadow-lg hover:shadow-blue-500/50 transition-all duration-200 font-medium flex items-center gap-2">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" /></svg>
        Thêm Domain
      </button>
    </div>

    <!-- Domain List -->
    <div class="bg-card-dark border border-gray-700/50 rounded-xl overflow-hidden shadow-xl">
      <table class="w-full text-left border-collapse">
        <thead class="bg-gray-800/50 text-gray-400 uppercase text-xs">
          <tr>
            <th class="px-6 py-4 font-semibold tracking-wider">Domain</th>
            <th class="px-6 py-4 font-semibold tracking-wider">Source Lang</th>
            <th class="px-6 py-4 font-semibold tracking-wider">Target Lang</th>
            <th class="px-6 py-4 font-semibold tracking-wider">Trạng thái</th>
            <th class="px-6 py-4 font-semibold tracking-wider">Ngày tạo</th>
            <th class="px-6 py-4 font-semibold tracking-wider text-right">Hành động</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-gray-700/50">
          <tr v-for="domain in domains" :key="domain.id" class="hover:bg-gray-700/20 transition-colors">
            <td class="px-6 py-4 font-medium text-white">{{ domain.domain }}</td>
            <td class="px-6 py-4 text-gray-300 text-sm">{{ domain.source_language || '-' }}</td>
            <td class="px-6 py-4 text-gray-300 text-sm">{{ domain.target_language || '-' }}</td>
            <td class="px-6 py-4">
              <span :class="domain.is_active ? 'bg-green-500/10 text-green-400' : 'bg-red-500/10 text-red-400'" class="px-2 py-1 rounded text-xs font-bold uppercase cursor-pointer" @click="toggleStatus(domain)">
                {{ domain.is_active ? 'Active' : 'Disabled' }}
              </span>
            </td>
            <td class="px-6 py-4 text-gray-400 text-sm">
                {{ formatDate(domain.created_at) }}
            </td>
            <td class="px-6 py-4 text-right space-x-2">
              <button @click="editDomain(domain)" class="text-blue-400 hover:text-blue-300 transition-colors">Sửa</button>
              <button @click="deleteDomain(domain.id)" class="text-red-400 hover:text-red-300 transition-colors">Xóa</button>
            </td>
          </tr>
          <tr v-if="domains.length === 0">
              <td colspan="6" class="px-6 py-8 text-center text-gray-500">Chưa có domain nào được cấu hình.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Modal Form -->
    <div v-if="showModal" class="fixed inset-0 z-50 flex items-center justify-center bg-black/50 backdrop-blur-sm">
      <div class="bg-card-dark border border-gray-700 w-full max-w-md p-6 rounded-xl shadow-2xl">
        <h2 class="text-xl font-bold text-white mb-4">{{ isEditing ? 'Cập nhật Domain' : 'Thêm Domain Mới' }}</h2>
        <form @submit.prevent="submitForm" class="space-y-4">
            <div>
              <label class="block text-sm text-gray-400 mb-1">Tên Domain</label>
              <input v-model="form.domain" class="w-full bg-bg-dark border border-gray-600 rounded p-2 text-white placeholder-gray-600" placeholder="example.com" required>
            </div>

            <div class="grid grid-cols-2 gap-4">
              <div>
                <label class="block text-sm text-gray-400 mb-1">Source Language</label>
                <input v-model="form.source_language" class="w-full bg-bg-dark border border-gray-600 rounded p-2 text-white placeholder-gray-600" placeholder="zh">
              </div>
              <div>
                <label class="block text-sm text-gray-400 mb-1">Target Language</label>
                <input v-model="form.target_language" class="w-full bg-bg-dark border border-gray-600 rounded p-2 text-white placeholder-gray-600" placeholder="vi">
              </div>
            </div>
            
           <div class="flex items-center gap-2">
             <input type="checkbox" v-model="form.is_active" id="active" class="w-4 h-4 rounded border-gray-600 bg-bg-dark text-blue-600 focus:ring-blue-500">
             <label for="active" class="text-white">Kích hoạt ngay</label>
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
})

const domains = ref([])
const showModal = ref(false)
const isEditing = ref(false)

const form = ref({
  id: null,
  domain: '',
  is_active: true,
  source_language: '',
  target_language: ''
})

// Use useFetch to interact with API
const { token } = useAuth()
const isLoading = ref(false)
const toast = useToast()
const { confirmDelete, alert } = useConfirm()

const fetchDomains = async () => {
    isLoading.value = true
    try {
        console.log('Fetching domains with token:', token.value)
        const data = await $fetch('/api/admin/supported-domains/', {
            headers: {
                Authorization: `Bearer ${token.value}`
            }
        })
        domains.value = data
    } catch (e) {
        console.error('Fetch error:', e)
        if (e.response?.status === 401 || e.response?.status === 403) {
             await alert('Phiên đăng nhập hết hạn hoặc không có quyền. Vui lòng đăng nhập lại.', 'Lỗi Xác Thực')
             navigateTo('/admin/login')
        } else {
            toast.error('Không thể tải danh sách domain')
        }
    } finally {
        isLoading.value = false
    }
}

const formatDate = (dateString) => {
    if (!dateString) return ''
    return new Date(dateString).toLocaleDateString('vi-VN')
}

const openModal = () => {
  isEditing.value = false
  form.value = { domain: '', is_active: true, source_language: '', target_language: '' }
  showModal.value = true
}

const editDomain = (domain) => {
  isEditing.value = true
  form.value = { ...domain }
  showModal.value = true
}

const submitForm = async () => {
  try {
     const headers = { Authorization: `Bearer ${token.value}` }
     if (isEditing.value) {
         await $fetch(`/api/admin/supported-domains/${form.value.id}`, {
             method: 'PUT',
             body: form.value,
             headers
         })
         toast.success('Cập nhật domain thành công')
     } else {
         await $fetch('/api/admin/supported-domains/', {
             method: 'POST',
             body: form.value,
             headers
         })
         toast.success('Thêm domain thành công')
     }
     
     showModal.value = false
     fetchDomains() // Refresh
  } catch (e) {
    toast.error('Có lỗi xảy ra: ' + (e.data?.detail || e.message))
  }
}

const deleteDomain = async (id) => {
  const isConfirmed = await confirmDelete()
  if(isConfirmed) {
    try {
        await $fetch(`/api/admin/supported-domains/${id}`, {
             method: 'DELETE',
             headers: { Authorization: `Bearer ${token.value}` }
         })
        toast.success('Xóa domain thành công')
        fetchDomains()
    } catch(e) {
        toast.error('Có lỗi khi xóa: ' + (e.data?.detail || e.message))
    }
  }
}

const toggleStatus = async (domain) => {
    const newStatus = !domain.is_active
    try {
         await $fetch(`/api/admin/supported-domains/${domain.id}`, {
             method: 'PUT',
             body: { is_active: newStatus },
             headers: { Authorization: `Bearer ${token.value}` }
         })
        toast.success('Cập nhật trạng thái thành công')
        fetchDomains()
    } catch(e) {
        toast.error('Có lỗi khi cập nhật: ' + (e.data?.detail || e.message))
    }
}

onMounted(() => {
  fetchDomains()
})
</script>
