<template>
  <div>
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold bg-gradient-to-r from-white to-gray-200 bg-clip-text text-transparent">
        Chỉnh sửa sản phẩm
      </h1>
      <NuxtLink 
        to="/admin/products" 
        class="text-gray-400 hover:text-white transition-colors flex items-center gap-2"
      >
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
        </svg>
        Quay lại
      </NuxtLink>
    </div>

    <div v-if="loading" class="text-center py-8">
      <p class="text-gray-400">Đang tải...</p>
    </div>

    <form v-else @submit.prevent="handleSubmit" class="bg-gray-800/50 backdrop-blur-xl rounded-lg shadow-xl border border-gray-700/50 p-6 space-y-6">
      <div class="space-y-4">
        <h2 class="text-xl font-semibold text-white border-b border-gray-700 pb-2">Thông tin cơ bản</h2>
        
        <div>
          <label class="block text-sm font-semibold text-gray-200 mb-2">
            Tên sản phẩm <span class="text-red-400">*</span>
          </label>
          <input 
            v-model="form.name" 
            type="text" 
            required
            class="w-full px-4 py-2 bg-gray-700/50 border border-gray-600 rounded-lg text-white focus:ring-2 focus:ring-blue-500 focus:border-transparent"
          />
        </div>

        <div class="grid grid-cols-2 gap-4">
          <div>
            <label class="block text-sm font-semibold text-gray-200 mb-2">Mã SKU</label>
            <input 
              v-model="form.sku" 
              type="text"
              class="w-full px-4 py-2 bg-gray-700/50 border border-gray-600 rounded-lg text-white focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            />
          </div>

          <div>
            <label class="block text-sm font-semibold text-gray-200 mb-2">Danh mục</label>
            <VSelect
              v-model="form.category_id"
              :options="categories"
              :reduce="cat => cat.id"
              label="name"
              placeholder="-- Tìm kiếm hoặc chọn danh mục --"
              :clearable="true"
              :searchable="true"
            >
              <template #no-options>
                Không tìm thấy danh mục
              </template>
            </VSelect>
          </div>
        </div>

        <div>
          <label class="block text-sm font-semibold text-gray-200 mb-2">Mô tả</label>
          <textarea 
            v-model="form.description" 
            rows="4"
            class="w-full px-4 py-2 bg-gray-700/50 border border-gray-600 rounded-lg text-white focus:ring-2 focus:ring-blue-500 focus:border-transparent"
          ></textarea>
        </div>
      </div>

      <div class="space-y-4">
        <h2 class="text-xl font-semibold text-white border-b border-gray-700 pb-2">Giá & Kho hàng</h2>
        
        <div class="grid grid-cols-2 gap-4">
          <div>
            <label class="block text-sm font-semibold text-gray-200 mb-2">
              Giá nhập <span class="text-red-400">*</span>
            </label>
            <input 
              v-model.number="form.cost_price" 
              type="number" 
              min="0"
              step="1000"
              required
              class="w-full px-4 py-2 bg-gray-700/50 border border-gray-600 rounded-lg text-white focus:ring-2 focus:ring-orange-500 focus:border-transparent"
            />
          </div>

          <div>
            <label class="block text-sm font-semibold text-gray-200 mb-2">
              Giá bán <span class="text-red-400">*</span>
            </label>
            <input 
              v-model.number="form.selling_price" 
              type="number" 
              min="0"
              step="1000"
              required
              class="w-full px-4 py-2 bg-gray-700/50 border border-gray-600 rounded-lg text-white focus:ring-2 focus:ring-green-500 focus:border-transparent"
            />
          </div>
        </div>

        <div class="grid grid-cols-3 gap-4">
          <div>
            <label class="block text-sm font-semibold text-gray-200 mb-2">
              Tồn kho <span class="text-red-400">*</span>
            </label>
            <input 
              v-model.number="form.stock_quantity" 
              type="number" 
              min="0"
              required
              class="w-full px-4 py-2 bg-gray-700/50 border border-gray-600 rounded-lg text-white focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            />
          </div>

          <div>
            <label class="block text-sm font-semibold text-gray-200 mb-2">Đã bán</label>
            <input 
              v-model.number="form.sold_quantity" 
              type="number" 
              min="0"
              readonly
              class="w-full px-4 py-2 bg-gray-600/30 border border-gray-600 rounded-lg text-gray-400 cursor-not-allowed"
            />
          </div>

          <div>
            <label class="block text-sm font-semibold text-gray-200 mb-2">Mức cảnh báo</label>
            <input 
              v-model.number="form.reorder_level" 
              type="number" 
              min="0"
              class="w-full px-4 py-2 bg-gray-700/50 border border-gray-600 rounded-lg text-white focus:ring-2 focus:ring-yellow-500 focus:border-transparent"
            />
          </div>
        </div>
      </div>

      <div class="space-y-4">
        <h2 class="text-xl font-semibold text-white border-b border-gray-700 pb-2">Hình ảnh</h2>
        <p class="text-sm text-gray-400">Có thể chọn nhiều hình ảnh cho sản phẩm</p>
        <FileUploader
          type="image"
          :allow-multiple="true"
          :accepted-file-types="'image/jpeg, image/png, image/webp'"
          :initial-files="initialImages"
          model-type="App\Models\Product"
          :model-id="route.params.id"
        />
      </div>

      <div class="space-y-4">
        <h2 class="text-xl font-semibold text-white border-b border-gray-700 pb-2">Trạng thái</h2>
        <div class="flex items-center gap-3">
          <input 
            v-model="form.is_active" 
            type="checkbox" 
            id="is_active"
            class="w-5 h-5 rounded bg-gray-700 border-gray-600 text-blue-500 focus:ring-2 focus:ring-blue-500"
          />
          <label for="is_active" class="text-sm font-semibold text-gray-200">Hiển thị sản phẩm</label>
        </div>
      </div>

      <div class="flex justify-end gap-4 pt-4 border-t border-gray-700">
        <NuxtLink 
          to="/admin/products"
          class="px-6 py-2 bg-gray-700 text-white rounded-lg hover:bg-gray-600 transition-colors"
        >
          Hủy
        </NuxtLink>
        <button 
          type="submit"
          :disabled="saving"
          class="inline-flex justify-center items-center gap-2 py-3 px-8 min-w-[200px] bg-gradient-to-r from-blue-500 to-blue-600 text-white rounded-lg shadow-lg hover:shadow-blue-500/50 font-medium focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary disabled:opacity-50 transition-all"
        >
          <svg v-if="!saving" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
          </svg>
          <svg v-else class="animate-spin w-5 h-5" fill="none" viewBox="0 0 24 24">
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
          </svg>
          {{ saving ? 'Đang lưu...' : 'Cập nhật' }}
        </button>
      </div>
    </form>
  </div>
</template>

<script setup>
definePageMeta({
  layout: 'admin',
  middleware: 'admin-auth'
})

const route = useRoute()
const router = useRouter()
const { token } = useAuth()
const config = useRuntimeConfig()

const loading = ref(true)
const saving = ref(false)
const categories = ref([])
const product = ref(null)

const form = reactive({
  name: '',
  sku: '',
  description: '',
  category_id: null,
  cost_price: 0,
  selling_price: 0,
  stock_quantity: 0,
  sold_quantity: 0,
  reorder_level: 10,
  image: null,
  is_active: true
})

const initialImages = computed(() => {
  if (product.value?.images && Array.isArray(product.value.images) && product.value.images.length > 0) {
    return product.value.images.map(file => {
      return `${config.public.apiBase}/storage/${file.path}`
    })
  }
  if (product.value?.image) {
    const imageUrl = product.value.image.startsWith('http')
      ? product.value.image
      : `${config.public.apiBase}/storage/${product.value.image}`
    return [imageUrl]
  }
  return []
})

const loadCategories = async () => {
  try {
    const response = await $fetch(`${config.public.apiBase}/api/categories`)
    categories.value = response.data || []
  } catch (e) {
    console.error('Error loading categories:', e)
  }
}

const loadProduct = async () => {
  loading.value = true
  try {
    const response = await $fetch(`${config.public.apiBase}/api/admin/products/${route.params.id}`, {
      headers: { Authorization: `Bearer ${token.value}` }
    })
    
    product.value = response
    Object.keys(form).forEach(key => {
      if (key !== 'image' && response[key] !== undefined) form[key] = response[key]
    })
    if (!form.selling_price && response.price) form.selling_price = response.price
  } catch (e) {
    console.error('Error loading product:', e)
    const toast = useToast()
    toast.error('Không thể tải sản phẩm', 'Lỗi')
    router.push('/admin/products')
  } finally {
    loading.value = false
  }
}

const handleSubmit = async () => {
  saving.value = true
  try {
    const payload = { ...form }
    if (!payload.image) delete payload.image

    await $fetch(`${config.public.apiBase}/api/admin/products/${route.params.id}`, {
      method: 'PUT',
      headers: { Authorization: `Bearer ${token.value}` },
      body: payload
    })
    
    const toast = useToast()
    toast.success('Sản phẩm đã được cập nhật thành công!')
    
    router.push('/admin/products')
  } catch (e) {
    console.error('Error updating product:', e)
    const toast = useToast()
    toast.error(e.data?.message || 'Không thể cập nhật sản phẩm', 'Lỗi')
  } finally {
    saving.value = false
  }
}

onMounted(async () => {
  await loadCategories()
  await loadProduct()
})
</script>
