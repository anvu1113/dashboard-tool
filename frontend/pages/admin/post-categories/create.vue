<template>
  <div>
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold bg-gradient-to-r from-white to-gray-200 bg-clip-text text-transparent">Thêm loại tin tức mới</h1>
      <NuxtLink to="/admin/post-categories" class="inline-flex items-center gap-2 text-blue-400 hover:text-blue-300 font-medium transition-colors">
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
        </svg>
        Quay lại
      </NuxtLink>
    </div>

    <div class="bg-gray-800/50 backdrop-blur-xl rounded-lg shadow-xl border border-gray-700/50 p-6">
      <form @submit.prevent="submit" class="space-y-6">
        <div>
          <label class="block text-sm font-semibold text-gray-200 mb-2">Tên loại tin tức *</label>
          <input 
            v-model="form.name" 
            type="text" 
            required 
            class="block w-full bg-gray-700/50 border border-gray-600 text-white rounded-lg shadow-sm py-3 px-4 focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent placeholder-gray-400" 
            placeholder="Nhập tên loại tin tức"
          />
        </div>

        <div>
          <label class="block text-sm font-semibold text-gray-200 mb-2">Mô tả</label>
          <textarea 
            v-model="form.description" 
            rows="4" 
            class="block w-full bg-gray-700/50 border border-gray-600 text-white rounded-lg shadow-sm py-3 px-4 focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent placeholder-gray-400"
            placeholder="Nhập mô tả cho loại tin tức này"
          ></textarea>
        </div>

        <div class="pt-6 flex gap-3 justify-end">
          <button 
            type="submit" 
            :disabled="loading" 
            class="inline-flex justify-center items-center gap-2 py-3 px-8 min-w-[200px] bg-gradient-to-r from-blue-500 to-blue-600 text-white rounded-lg shadow-lg hover:shadow-blue-500/50 font-medium focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary disabled:opacity-50 transition-all"
          >
            <svg v-if="!loading" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
            </svg>
            <svg v-else class="animate-spin w-5 h-5" fill="none" viewBox="0 0 24 24">
              <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
              <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
            </svg>
            {{ loading ? 'Đang lưu...' : 'Tạo mới' }}
          </button>
          <NuxtLink 
            to="/admin/post-categories"
            class="px-6 py-3 border-2 border-gray-600 text-gray-300 rounded-lg hover:border-gray-500 hover:text-white font-medium transition-colors"
          >
            Hủy
          </NuxtLink>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
definePageMeta({
  layout: 'admin',
  middleware: 'admin-auth'
})

const { token } = useAuth()
const config = useRuntimeConfig()
const router = useRouter()
const loading = ref(false)

const form = reactive({
  name: '',
  description: ''
})

const submit = async () => {
  loading.value = true
  try {
    await $fetch(`${config.public.apiBase}/api/admin/post-categories`, {
      method: 'POST',
      body: form,
      headers: { Authorization: `Bearer ${token.value}` }
    })

    const toast = useToast()
    toast.success('Loại tin tức đã được tạo thành công!')
    
    router.push('/admin/post-categories')
  } catch (e) {
    const toast = useToast()
    toast.error(e.data?.message || 'Không thể tạo loại tin tức', 'Lỗi')
    console.error(e)
  } finally {
    loading.value = false
  }
}
</script>
