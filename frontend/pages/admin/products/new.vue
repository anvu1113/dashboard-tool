<template>
  <div>
    <div class="max-w-4xl">
      <!-- Header -->
      <div class="mb-8">
        <NuxtLink 
          to="/admin/products"
          class="text-primary hover:underline mb-4 inline-block"
        >
          ← Quay lại danh sách
        </NuxtLink>
        <h1 class="text-3xl font-bold text-primary mb-2">
          Thêm sản phẩm mới
        </h1>
      </div>

      <!-- Form -->
      <div class="bg-white border border-gray-light rounded-lg p-6 md:p-8">
        <form @submit.prevent="saveProduct" class="space-y-6">
          <!-- Product Name -->
          <div>
            <label for="name" class="block text-sm font-semibold text-primary mb-2">
              Tên sản phẩm <span class="text-red-500">*</span>
            </label>
            <input
              id="name"
              v-model="form.name"
              type="text"
              required
              placeholder="Nhập tên sản phẩm"
              class="w-full px-4 py-3 border border-gray-light rounded focus:outline-none focus:ring-2 focus:ring-primary"
            />
          </div>

          <!-- SKU -->
          <div>
            <label for="sku" class="block text-sm font-semibold text-primary mb-2">
              Mã sản phẩm (SKU)
            </label>
            <input
              id="sku"
              v-model="form.sku"
              type="text"
              placeholder="Nhập mã sản phẩm"
              class="w-full px-4 py-3 border border-gray-light rounded focus:outline-none focus:ring-2 focus:ring-primary"
            />
          </div>

          <!-- Price -->
          <div>
            <label for="price" class="block text-sm font-semibold text-primary mb-2">
              Giá bán (VNĐ) <span class="text-red-500">*</span>
            </label>
            <input
              id="price"
              v-model.number="form.price"
              type="number"
              required
              min="0"
              step="1000"
              placeholder="0"
              class="w-full px-4 py-3 border border-gray-light rounded focus:outline-none focus:ring-2 focus:ring-primary"
            />
          </div>

          <!-- Stock -->
          <div>
            <label for="stock" class="block text-sm font-semibold text-primary mb-2">
              Số lượng tồn kho
            </label>
            <input
              id="stock"
              v-model.number="form.stock"
              type="number"
              min="0"
              placeholder="0"
              class="w-full px-4 py-3 border border-gray-light rounded focus:outline-none focus:ring-2 focus:ring-primary"
            />
          </div>

          <!-- Image URL -->
          <div>
            <label for="image" class="block text-sm font-semibold text-primary mb-2">
              Link ảnh sản phẩm
            </label>
            <input
              id="image"
              v-model="form.image"
              type="url"
              placeholder="https://..."
              class="w-full px-4 py-3 border border-gray-light rounded focus:outline-none focus:ring-2 focus:ring-primary"
            />
            <p class="text-xs text-gray-dark mt-1">Hoặc upload ảnh sau khi tạo sản phẩm</p>
          </div>

          <!-- Description -->
          <div>
            <label for="description" class="block text-sm font-semibold text-primary mb-2">
              Mô tả sản phẩm
            </label>
            <textarea
              id="description"
              v-model="form.description"
              rows="6"
              placeholder="Mô tả chi tiết về sản phẩm..."
              class="w-full px-4 py-3 border border-gray-light rounded focus:outline-none focus:ring-2 focus:ring-primary resize-none"
            ></textarea>
          </div>

          <!-- Featured -->
          <div>
            <label class="flex items-center">
              <input
                v-model="form.featured"
                type="checkbox"
                class="mr-2"
              />
              <span class="text-sm text-gray-dark">Sản phẩm nổi bật (hiển thị trên trang chủ)</span>
            </label>
          </div>

          <!-- Submit Button -->
          <div class="flex space-x-4 pt-4">
            <button
              type="submit"
              :disabled="isSaving"
              class="flex-1 bg-primary text-white px-6 py-4 rounded font-semibold hover:bg-primary-dark transition-colors disabled:opacity-50"
            >
              {{ isSaving ? 'Đang lưu...' : 'Lưu sản phẩm' }}
            </button>
            <NuxtLink
              to="/admin/products"
              class="px-6 py-4 border border-gray-light rounded font-semibold text-gray-dark hover:bg-gray-50 transition-colors"
            >
              Hủy
            </NuxtLink>
          </div>

          <!-- Success Message -->
          <div v-if="showSuccess" class="p-4 bg-green-50 border border-green-200 rounded text-green-800">
            ✓ Đã tạo sản phẩm thành công!
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
definePageMeta({
  layout: 'admin'
})

useHead({
  title: 'Thêm sản phẩm - Admin'
})

const form = ref({
  name: '',
  sku: '',
  price: 0,
  stock: 0,
  image: '',
  description: '',
  featured: false
})

const isSaving = ref(false)
const showSuccess = ref(false)

const saveProduct = async () => {
  isSaving.value = true
  showSuccess.value = false

  try {
    const config = useRuntimeConfig()
    await $fetch(`${config.public.apiBase}/api/admin/products`, {
      method: 'POST',
      body: form.value
    })

    showSuccess.value = true
    setTimeout(() => {
      navigateTo('/admin/products')
    }, 1500)
  } catch (err) {
    console.error('Error saving product:', err)
    alert('Có lỗi xảy ra khi tạo sản phẩm')
  } finally {
    isSaving.value = false
  }
}
</script>










