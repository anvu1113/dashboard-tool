<template>
  <div>
    <!-- Header -->
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold bg-gradient-to-r from-white to-gray-200 bg-clip-text text-transparent">
        Quản lý Gói cước (Plans)
      </h1>
      <button @click="openModal()" class="bg-gradient-to-r from-blue-500 to-blue-600 text-white px-6 py-3 rounded-lg hover:shadow-lg hover:shadow-blue-500/50 transition-all duration-200 font-medium flex items-center gap-2">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" /></svg>
        Thêm gói mới
      </button>
    </div>

    <!-- Plans Grid -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      <div v-for="plan in plans" :key="plan.id" class="bg-card-dark border border-gray-700/50 rounded-xl p-6 shadow-xl relative group hover:border-blue-500/50 transition-colors">
        <div class="flex justify-between items-start mb-4">
          <div>
            <h3 class="text-xl font-bold text-white">{{ plan.name }}</h3>
             <span class="text-xs font-mono text-gray-500 uppercase">{{ plan.code }}</span>
          </div>
          <span :class="plan.is_active ? 'bg-green-500/10 text-green-400' : 'bg-red-500/10 text-red-400'" class="px-2 py-1 rounded text-xs font-bold uppercase">
            {{ plan.is_active ? 'Active' : 'Disabled' }}
          </span>
        </div>
        
        <div class="text-3xl font-bold text-white mb-6">
          {{ formatPrice(plan.price) }} <span class="text-sm font-normal text-gray-400">/ {{ plan.billing_cycle }}</span>
        </div>

        <div class="space-y-2 mb-6 h-32 overflow-y-auto custom-scrollbar">
          <div v-for="feature in plan.features" :key="feature.id" class="flex justify-between text-sm">
            <span class="text-gray-400">{{ feature.key }}</span>
            <span class="text-white font-mono">{{ feature.value }}</span>
          </div>
        </div>

        <div class="flex gap-2">
          <button @click="editPlan(plan)" class="flex-1 bg-gray-700 hover:bg-gray-600 text-white py-2 rounded-lg transition-colors">Sửa</button>
          <button @click="deletePlan(plan.id)" class="px-3 bg-red-500/10 hover:bg-red-500/20 text-red-500 rounded-lg transition-colors">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" /></svg>
          </button>
        </div>
      </div>
    </div>

    <!-- Modal Form (Simplified) -->
    <div v-if="showModal" class="fixed inset-0 z-50 flex items-center justify-center bg-black/50 backdrop-blur-sm">
      <div class="bg-card-dark border border-gray-700 w-full max-w-lg p-6 rounded-xl shadow-2xl">
        <h2 class="text-xl font-bold text-white mb-4">{{ isEditing ? 'Cập nhật gói' : 'Tạo gói mới' }}</h2>
        <form @submit.prevent="submitForm" class="space-y-4">
          <div class="grid grid-cols-2 gap-4">
             <div>
              <label class="block text-sm text-gray-400 mb-1">Tên gói</label>
              <input v-model="form.name" class="w-full bg-bg-dark border border-gray-600 rounded p-2 text-white" required>
            </div>
            <div>
              <label class="block text-sm text-gray-400 mb-1">Mã (Code)</label>
              <input v-model="form.code" class="w-full bg-bg-dark border border-gray-600 rounded p-2 text-white" required :disabled="isEditing">
            </div>
          </div>
           <div class="grid grid-cols-2 gap-4">
             <div>
              <label class="block text-sm text-gray-400 mb-1">Giá (VND)</label>
              <input v-model.number="form.price" type="number" class="w-full bg-bg-dark border border-gray-600 rounded p-2 text-white" required>
            </div>
            <div>
              <label class="block text-sm text-gray-400 mb-1">Chu kỳ</label>
              <select v-model="form.billing_cycle" class="w-full bg-bg-dark border border-gray-600 rounded p-2 text-white">
                <option value="monthly">Monthly</option>
                <option value="yearly">Yearly</option>
              </select>
            </div>
          </div>
          
           <!-- Features Editor (Simple Text Area for JSON) -->
           <div>
             <label class="block text-sm text-gray-400 mb-1">Features (JSON)</label>
             <textarea v-model="featuresJson" rows="4" class="w-full bg-bg-dark border border-gray-600 rounded p-2 text-white font-mono text-sm" placeholder='[{"key": "max_products", "value": "10"}]'></textarea>
             <p class="text-xs text-gray-500 mt-1">Nhập JSON array các feature.</p>
           </div>

           <div class="flex items-center gap-2">
             <input type="checkbox" v-model="form.is_active" id="active">
             <label for="active" class="text-white">Kích hoạt</label>
           </div>

          <div class="flex justify-end gap-3 mt-6">
            <button type="button" @click="showModal = false" class="px-4 py-2 text-gray-400 hover:text-white">Hủy</button>
            <button type="submit" class="px-6 py-2 bg-blue-600 hover:bg-blue-500 text-white rounded-lg">Lưu</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
definePageMeta({
  layout: 'admin',
  permissions: ['plans.view']
  // middleware: 'auth'
})

const plans = ref([])
const showModal = ref(false)
const isEditing = ref(false)
const featuresJson = ref('[]')

const form = ref({
  id: null,
  name: '',
  code: '',
  price: 0,
  billing_cycle: 'monthly',
  is_active: true
})

// Fetch Plans
const fetchPlans = async () => {
  // In real implementation: const { data } = await useFetch('/api/admin/plans')
  // plans.value = data.value
  
  // Mock Data
  plans.value = [
    { 
      id: 1, name: 'Free Plan', code: 'free', price: 0, billing_cycle: 'monthly', is_active: true, 
      features: [{ id:1, key: 'max_daily_requests', value: '10' }, { id:2, key: 'export_excel', value: 'false' }] 
    },
    { 
      id: 2, name: 'Pro Plan', code: 'pro', price: 199000, billing_cycle: 'monthly', is_active: true,
       features: [{ id:3, key: 'max_daily_requests', value: '500' }, { id:4, key: 'export_excel', value: 'true' }] 
    }
  ]
}

const formatPrice = (price) => {
  return new Intl.NumberFormat('vi-VN', { style: 'currency', currency: 'VND' }).format(price)
}

const openModal = () => {
  isEditing.value = false
  form.value = { name: '', code: '', price: 0, billing_cycle: 'monthly', is_active: true }
  featuresJson.value = '[]'
  showModal.value = true
}

const editPlan = (plan) => {
  isEditing.value = true
  form.value = { ...plan }
  // Transform features back to simplified JSON struct for editing
  const simplifiedFeatures = plan.features.map(f => ({ key: f.key, value: f.value }))
  featuresJson.value = JSON.stringify(simplifiedFeatures, null, 2)
  showModal.value = true
}

const submitForm = async () => {
  try {
     const features = JSON.parse(featuresJson.value)
     const payload = { ...form.value, features }
     
     console.log('Submitting:', payload)
     // await $fetch(...) 
     
     showModal.value = false
     fetchPlans() // Refresh
  } catch (e) {
    alert('Invalid JSON in features or Server Error')
  }
}

const deletePlan = (id) => {
  if(confirm('Bạn có chắc chắn muốn xóa gói này?')) {
    console.log('Delete', id)
  }
}

onMounted(() => {
  fetchPlans()
})
</script>
