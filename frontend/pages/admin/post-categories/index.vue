<template>
  <div>
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold bg-gradient-to-r from-white to-gray-200 bg-clip-text text-transparent">Quản lý Loại tin tức</h1>
      <NuxtLink 
        to="/admin/post-categories/create" 
        class="bg-gradient-to-r from-green-500 to-green-600 text-white px-6 py-3 rounded-lg hover:shadow-lg hover:shadow-green-500/50 transition-all duration-200 font-medium flex items-center gap-2"
      >
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
        </svg>
        Thêm loại mới
      </NuxtLink>
    </div>

    <div class="bg-gray-800/50 backdrop-blur-xl rounded-lg shadow-xl border border-gray-700/50 overflow-hidden">
      <table class="min-w-full divide-y divide-gray-700/50">
        <thead class="bg-gray-700/30">
          <tr>
            <th class="px-6 py-4 text-left text-xs font-semibold text-gray-300 uppercase tracking-wider">Tên</th>
            <th class="px-6 py-4 text-left text-xs font-semibold text-gray-300 uppercase tracking-wider">Slug</th>
            <th class="px-6 py-4 text-left text-xs font-semibold text-gray-300 uppercase tracking-wider">Mô tả</th>
            <th class="px-6 py-4 text-right text-xs font-semibold text-gray-300 uppercase tracking-wider">Thao tác</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-gray-700/50">
          <tr v-for="category in categories" :key="category.id" class="hover:bg-gray-700/30 transition-colors">
            <td class="px-6 py-4 whitespace-nowrap text-sm font-semibold text-white">{{ category.name }}</td>
            <td class="px-6 py-4 whitespace-nowrap text-sm">
              <code class="bg-gray-700/50 px-2 py-1 rounded text-xs text-gray-200">{{ category.slug }}</code>
            </td>
            <td class="px-6 py-4 text-sm text-gray-200">{{ category.description || '-' }}</td>
            <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
              <NuxtLink 
                :to="`/admin/post-categories/${category.id}`" 
                class="inline-flex items-center gap-1 text-blue-400 hover:text-blue-300 mr-4 transition-colors"
              >
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                </svg>
                Sửa
              </NuxtLink>
              <button 
                @click="deleteCategory(category.id)" 
                class="inline-flex items-center gap-1 text-red-400 hover:text-red-300 transition-colors"
              >
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                </svg>
                Xóa
              </button>
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
  middleware: 'admin-auth'
})

const { token } = useAuth()
const config = useRuntimeConfig()
const categories = ref([])

const loadCategories = async () => {
  try {
    const response = await $fetch(`${config.public.apiBase}/api/admin/post-categories`, {
      headers: { Authorization: `Bearer ${token.value}` }
    })
    categories.value = response.data || []
  } catch (e) {
    console.error(e)
  }
}

const deleteCategory = async (id) => {
  const { confirmDelete } = useConfirm()
  const confirmed = await confirmDelete('loại tin tức này')
  if (!confirmed) return
  
  try {
    await $fetch(`${config.public.apiBase}/api/admin/post-categories/${id}`, {
      method: 'DELETE',
      headers: { Authorization: `Bearer ${token.value}` }
    })
    loadCategories()
    
    const toast = useToast()
    toast.success('Đã xóa loại tin tức thành công!')
  } catch (e) {
    const toast = useToast()
    toast.error('Không thể xóa loại tin tức', 'Lỗi')
  }
}

onMounted(loadCategories)
</script>
