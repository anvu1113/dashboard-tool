<template>
  <div>
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold bg-gradient-to-r from-white to-gray-200 bg-clip-text text-transparent">
        Thêm sản phẩm mới
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

    <form @submit.prevent="handleSubmit" class="bg-gray-800/50 backdrop-blur-xl rounded-lg shadow-xl border border-gray-700/50 p-6 space-y-6">
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
            placeholder="VD: Áo Thun Nữ Basic Trắng"
          />
        </div>

        <div class="grid grid-cols-2 gap-4">
          <div>
            <label class="block text-sm font-semibold text-gray-200 mb-2">Mã SKU</label>
            <input 
              v-model="form.sku" 
              type="text"
              class="w-full px-4 py-2 bg-gray-700/50 border border-gray-600 rounded-lg text-white focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              placeholder="VD: AO-THUN-001"
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
            placeholder="Mô tả chi tiết về sản phẩm..."
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
              placeholder="0"
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
              placeholder="0"
            />
          </div>
        </div>

        <div class="grid grid-cols-2 gap-4">
          <div>
            <label class="block text-sm font-semibold text-gray-200 mb-2">
              Số lượng tồn kho <span class="text-red-400">*</span>
            </label>
            <input 
              v-model.number="form.stock_quantity" 
              type="number" 
              min="0"
              required
              class="w-full px-4 py-2 bg-gray-700/50 border border-gray-600 rounded-lg text-white focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              placeholder="0"
            />
          </div>

          <div>
            <label class="block text-sm font-semibold text-gray-200 mb-2">
              Mức cảnh báo tồn kho
            </label>
            <input 
              v-model.number="form.reorder_level" 
              type="number" 
              min="0"
              class="w-full px-4 py-2 bg-gray-700/50 border border-gray-600 rounded-lg text-white focus:ring-2 focus:ring-yellow-500 focus:border-transparent"
              placeholder="10"
            />
          </div>
        </div>
      </div>

      <div class="space-y-4">
        <h2 class="text-xl font-semibold text-white border-b border-gray-700 pb-2">Hình ảnh</h2>
        <div class="p-4 bg-blue-500/10 border border-blue-500/30 rounded-lg">
          <p class="text-sm text-blue-300">
            💡 <strong>Lưu ý:</strong> Vui lòng tạo sản phẩm trước, sau đó bạn có thể upload nhiều hình ảnh ở trang chỉnh sửa.
          </p>
        </div>
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
          <label for="is_active" class="text-sm font-semibold text-gray-200">
            Hiển thị sản phẩm (Bỏ tick để ẩn)
          </label>
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
          :disabled="loading"
          class="px-6 py-2 bg-gradient-to-r from-blue-500 to-blue-600 text-white rounded-lg hover:shadow-lg hover:shadow-blue-500/50 transition-all duration-200 font-medium disabled:opacity-50 disabled:cursor-not-allowed"
        >
          {{ loading ? 'Đang tạo...' : 'Tạo sản phẩm' }}
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

const { token } = useAuth()
const config = useRuntimeConfig()
const router = useRouter()

const loading = ref(false)
const categories = ref([])

const form = reactive({
  name: '',
  sku: '',
  description: '',
  category_id: null,
  cost_price: 0,
  selling_price: 0,
  stock_quantity: 0,
  reorder_level: 10,
  image: null,
  is_active: true
})

const loadCategories = async () => {
  try {
    const response = await $fetch(`${config.public.apiBase}/api/categories`)
    categories.value = response.data || []
  } catch (e) {
    console.error('Error loading categories:', e)
  }
}

const handleSubmit = async () => {
  loading.value = true
  try {
    const payload = { ...form }
    if (!payload.image) delete payload.image

    const createdProduct = await $fetch(`${config.public.apiBase}/api/admin/products`, {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${token.value}`
      },
      body: payload
    })
    
    const toast = useToast()
    toast.success('Bạn có thể upload hình ảnh ở trang tiếp theo', 'Tạo sản phẩm thành công!')
    
    router.push(`/admin/products/${createdProduct.id}`)
  } catch (e) {
    console.error('Error creating product:', e)
    const toast = useToast()
    toast.error(e.data?.message || 'Không thể tạo sản phẩm', 'Lỗi')
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  loadCategories()
})
</script>
