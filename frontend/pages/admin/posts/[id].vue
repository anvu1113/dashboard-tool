<template>
  <div v-if="post">
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold bg-gradient-to-r from-white to-gray-200 bg-clip-text text-transparent">Sửa bài viết</h1>
      <NuxtLink to="/admin/posts" class="inline-flex items-center gap-2 text-blue-400 hover:text-blue-300 font-medium transition-colors">
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
        </svg>
        Quay lại
      </NuxtLink>
<!-- TEMP_MARKER -->
    </div>

    <div class="bg-gray-800/50 backdrop-blur-xl rounded-lg shadow-xl border border-gray-700/50 p-6 max-w-none">
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
                        :initial-files="initialThumbnail"
                        @uploaded="handleUpload"
                        @removed="handleRemove"
                    />
                </div>
            </div>

            <div class="flex items-center">
                <input v-model="form.is_published" type="checkbox" class="h-4 w-4 text-primary focus:ring-primary border-gray-600 rounded" />
                <label class="ml-2 block text-sm text-gray-200">Xuất bản</label>
            </div>

            <div class="flex justify-end gap-4 pt-4 border-t border-gray-700">
                <NuxtLink 
                  to="/admin/posts"
                  class="px-6 py-3 border-2 border-gray-600 text-gray-300 rounded-lg hover:border-gray-500 hover:text-white font-medium transition-colors"
                >
                  Hủy
                </NuxtLink>
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
                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 714 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                  </svg>
                  {{ loading ? 'Đang lưu...' : 'Cập nhật' }}
                </button>
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

const route = useRoute()
const router = useRouter()
const { token } = useAuth()
const config = useRuntimeConfig()
const loading = ref(false)
const post = ref(null)

const form = reactive({
    title: '',
    content: '',
    thumbnail: null, // undefined = keep existing, null = delete, string = new file
    is_published: true
})

const loadPost = async () => {
    try {
        const response = await $fetch(`${config.public.apiBase}/api/admin/posts/${route.params.id}`, {
            headers: { Authorization: `Bearer ${token.value}` }
        })
        post.value = response
        form.title = response.title
        form.content = response.content
        form.is_published = Boolean(response.is_published)
    } catch (e) {
        console.error(e)
    }
}

const initialThumbnail = computed(() => {
    if (post.value?.thumbnail) {
        const thumbnailUrl = post.value.thumbnail.startsWith('http') 
            ? post.value.thumbnail 
            : `${config.public.apiBase}/storage/${post.value.thumbnail}`
        return [thumbnailUrl]
    }
    return []
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
        const payload = {
            title: form.title,
            content: form.content || '',
            is_published: form.is_published ? 1 : 0
        }
        if (form.thumbnail) {
            payload.thumbnail = form.thumbnail
        }

        await $fetch(`${config.public.apiBase}/api/admin/posts/${route.params.id}`, {
            method: 'PUT',
            body: payload,
            headers: { Authorization: `Bearer ${token.value}` }
        })

        const toast = useToast()
        toast.success('Bài viết đã được cập nhật thành công!')
        
        router.push('/admin/posts')
    } catch (e) {
        const toast = useToast()
        toast.error(e.data?.message || 'Không thể cập nhật bài viết', 'Lỗi')
        console.error(e)
    } finally {
        loading.value = false
    }
}

onMounted(loadPost)
</script>
