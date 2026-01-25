<template>
  <div>
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold bg-gradient-to-r from-white to-gray-200 bg-clip-text text-transparent">Viết bài mới</h1>
      <NuxtLink to="/admin/posts" class="inline-flex items-center gap-2 text-blue-400 hover:text-blue-300 font-medium transition-colors">
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
        </svg>
        Quay lại
      </NuxtLink>
    </div>

    <div class="bg-gray-800/50 backdrop-blur-xl rounded-lg shadow-xl border border-gray-700/50 p-6">
        <form @submit.prevent="submit" class="space-y-6">
            <div>
                <label class="block text-sm font-semibold text-gray-200 mb-2">Tiêu đề *</label>
                <input v-model="form.title" type="text" required class="mt-1 block w-full border border-gray-600 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-primary focus:border-primary" />
            </div>

            <div>
                <label class="block text-sm font-semibold text-gray-200 mb-2">Nội dung</label>
                <ClientOnly>
                    <TiptapEditor v-model="form.content" />
                </ClientOnly>
                <p class="text-xs text-gray-500 mt-1">Hỗ trợ định dạng văn bản phong phú.</p>
            </div>

            <div>
                <label class="block text-sm font-semibold text-gray-200 mb-2">Hình ảnh Thumbnail</label>
                <div class="mt-1">
                    <FileUploader
                        type="image"
                        :accepted-file-types="'image/jpeg, image/png, image/webp'"
                        @uploaded="handleUpload"
                        @removed="handleRemove"
                    />
                </div>
            </div>

            <div>
                <label class="block text-sm font-semibold text-gray-200 mb-2">Loại tin tức</label>
                <VSelect
                    v-model="form.post_category_id"
                    :options="postCategories"
                    :reduce="category => category.id"
                    label="name"
                    placeholder="-- Tìm kiếm hoặc chọn loại tin tức --"
                    :clearable="true"
                    :searchable="true"
                >
                    <template #no-options>
                        Không tìm thấy kết quả
                    </template>
                </VSelect>
            </div>

            <div class="flex items-center">
                <input v-model="form.is_published" type="checkbox" class="h-4 w-4 text-primary focus:ring-primary border-gray-600 rounded" />
                <label class="ml-2 block text-sm text-gray-200">Xuất bản ngay</label>
            </div>

            <div class="pt-6 flex gap-3 justify-end">
                <button type="submit" :disabled="loading" class="inline-flex justify-center items-center gap-2 py-3 px-8 min-w-[200px] bg-gradient-to-r from-blue-500 to-blue-600 text-white rounded-lg shadow-lg hover:shadow-blue-500/50 font-medium focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary disabled:opacity-50 transition-all">
                    {{ loading ? 'Đang lưu...' : 'Tạo mới' }}
                </button>
                <NuxtLink 
                  to="/admin/posts"
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
import FileUploader from '@/components/FileUploader.vue'
import TiptapEditor from '@/components/TiptapEditor.vue'

definePageMeta({
  layout: 'admin',
  middleware: 'admin-auth'
})

const { token } = useAuth()
const config = useRuntimeConfig()
const router = useRouter()
const loading = ref(false)
const postCategories = ref([])

const form = reactive({
    title: '',
    content: '',
    thumbnail: null,
    is_published: true,
    post_category_id: null
})

const handleUpload = (fileData) => {
    form.thumbnail = fileData.path
}

const handleRemove = () => {
    form.thumbnail = null
}

const submit = async () => {
    loading.value = true
    try {
        await $fetch(`${config.public.apiBase}/api/admin/posts`, {
            method: 'POST',
            body: form,
            headers: { Authorization: `Bearer ${token.value}` }
        })

        const toast = useToast()
        toast.success('Bài viết đã được tạo thành công!')
        
        router.push('/admin/posts')
    } catch (e) {
        const toast = useToast()
        toast.error(e.data?.message || 'Không thể tạo bài viết', 'Lỗi')
        console.error(e)
    } finally {
        loading.value = false
    }
}

const loadPostCategories = async () => {
    try {
        const response = await $fetch(`${config.public.apiBase}/api/admin/post-categories`, {
            headers: { Authorization: `Bearer ${token.value}` }
        })
        postCategories.value = response.data || []
    } catch (e) {
        console.error('Error loading post categories:', e)
    }
}

onMounted(loadPostCategories)
</script>
