<template>
  <div>
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold bg-gradient-to-r from-white to-gray-200 bg-clip-text text-transparent">Quản lý bài viết</h1>
      <NuxtLink 
        to="/admin/posts/create" 
        class="bg-gradient-to-r from-green-500 to-green-600 text-white px-6 py-3 rounded-lg hover:shadow-lg hover:shadow-green-500/50 transition-all duration-200 font-medium flex items-center gap-2"
      >
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
        </svg>
        Viết bài mới
      </NuxtLink>
    </div>

    <div class="bg-gray-800/50 backdrop-blur-xl rounded-lg shadow-xl border border-gray-700/50 overflow-hidden">
      <table class="min-w-full divide-y divide-gray-700/50">
        <thead class="bg-gray-700/30">
          <tr>
            <th class="px-6 py-4 text-left text-xs font-semibold text-gray-300 uppercase tracking-wider">Hình ảnh</th>
            <th class="px-6 py-4 text-left text-xs font-semibold text-gray-300 uppercase tracking-wider">Tiêu đề</th>
            <th class="px-6 py-4 text-left text-xs font-semibold text-gray-300 uppercase tracking-wider">Trạng thái</th>
            <th class="px-6 py-4 text-left text-xs font-semibold text-gray-300 uppercase tracking-wider">Người tạo</th>
            <th class="px-6 py-4 text-left text-xs font-semibold text-gray-300 uppercase tracking-wider">Ngày tạo</th>
            <th class="px-6 py-4 text-right text-xs font-semibold text-gray-300 uppercase tracking-wider">Thao tác</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-gray-700/50">
          <tr v-for="post in posts" :key="post.id" class="hover:bg-gray-700/30 transition-colors">
            <td class="px-6 py-4 whitespace-nowrap">
                <img v-if="post.thumbnail" :src="post.thumbnail.startsWith('http') ? post.thumbnail : `${config.public.apiBase}/storage/${post.thumbnail}`" class="h-12 w-12 rounded-lg object-cover border border-gray-600" />
                <div v-else class="h-12 w-12 bg-gray-700 rounded-lg flex items-center justify-center">
                  <svg class="w-6 h-6 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
                  </svg>
                </div>
            </td>
            <td class="px-6 py-4 text-sm font-semibold text-white max-w-md truncate">{{ post.title }}</td>
            <td class="px-6 py-4 whitespace-nowrap">
              <span :class="post.is_published ? 'bg-green-500/20 text-green-400 border-green-500/50' : 'bg-yellow-500/20 text-yellow-400 border-yellow-500/50'" class="px-3 py-1 inline-flex text-xs leading-5 font-semibold rounded-full border">
                {{ post.is_published ? 'Đã đăng' : 'Nháp' }}
              </span>
            </td>
            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-200">
              {{ post.user?.name || 'Không rõ' }}
            </td>
            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-400">{{ formatDate(post.created_at) }}</td>
            <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
              <NuxtLink 
                :to="`/admin/posts/${post.id}`" 
                class="inline-flex items-center gap-1 text-blue-400 hover:text-blue-300 mr-4 transition-colors"
              >
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                </svg>
                Sửa
              </NuxtLink>
              <button 
                @click="deletePost(post.id)" 
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
  middleware: 'admin-auth'
})

const config = useRuntimeConfig()
const { token } = useAuth()
const posts = ref([])
const page = ref(1)
const totalPages = ref(1)

const loadPosts = async () => {
    try {
        const response = await $fetch(`${config.public.apiBase}/api/admin/posts?page=${page.value}`, {
            headers: { Authorization: `Bearer ${token.value}` }
        })
        posts.value = response.data
        totalPages.value = response.last_page
    } catch (e) {
        console.error(e)
    }
}

const deletePost = async (id) => {
    const { confirmDelete } = useConfirm()
    const confirmed = await confirmDelete('bài viết này')
    if (!confirmed) return
    
    try {
        await $fetch(`${config.public.apiBase}/api/admin/posts/${id}`, {
            method: 'DELETE',
            headers: { Authorization: `Bearer ${token.value}` }
        })
        loadPosts()
        
        const toast = useToast()
        toast.success('Đã xóa bài viết thành công!')
    } catch (e) {
        const toast = useToast()
        toast.error('Không thể xóa bài viết', 'Lỗi')
    }
}

const formatDate = (d) => new Date(d).toLocaleDateString('vi-VN')

watch(page, loadPosts)
onMounted(loadPosts)
</script>
