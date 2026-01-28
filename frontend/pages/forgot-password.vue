<template>
  <div class="bg-white min-h-screen py-12 md:py-16">
    <div class="container mx-auto px-4">
      <div class="max-w-md mx-auto">
        <!-- Header -->
        <div class="text-center mb-8">
          <h1 class="text-3xl md:text-4xl font-bold text-primary mb-4">
            Quên mật khẩu
          </h1>
          <p class="text-gray-dark">
            Nhập email để nhận link đặt lại mật khẩu
          </p>
        </div>

        <!-- Form -->
        <div class="bg-white border border-gray-light rounded-lg p-6 md:p-8">
          <form @submit.prevent="handleForgotPassword" class="space-y-6">
            <!-- Email -->
            <div>
              <label for="email" class="block text-sm font-semibold text-primary mb-2">
                Email <span class="text-red-500">*</span>
              </label>
              <input
                id="email"
                v-model="form.email"
                type="email"
                required
                placeholder="your@email.com"
                class="w-full px-4 py-3 border border-gray-light rounded focus:outline-none focus:ring-2 focus:ring-primary"
                :class="{ 'border-red-500': errors.email }"
              />
              <p v-if="errors.email" class="text-red-500 text-sm mt-1">{{ errors.email }}</p>
            </div>

            <!-- Submit Button -->
            <button
              type="submit"
              :disabled="isLoading"
              class="w-full bg-primary text-white px-6 py-4 rounded font-semibold hover:bg-primary-dark transition-colors disabled:opacity-50 disabled:cursor-not-allowed text-lg"
            >
              {{ isLoading ? 'Đang gửi...' : 'Gửi link đặt lại mật khẩu' }}
            </button>
          </form>

          <!-- Success Message -->
          <div v-if="showSuccess" class="mt-6 p-4 bg-green-50 border border-green-200 rounded text-green-800">
            <p class="font-semibold mb-2">✓ Email đã được gửi!</p>
            <p class="text-sm">{{ successMessage }}</p>
            <p class="text-sm mt-2">Vui lòng kiểm tra hộp thư đến và spam của bạn.</p>
          </div>

          <!-- Error Message -->
          <div v-if="error" class="mt-6 p-4 bg-red-50 border border-red-200 rounded text-red-800">
            <p class="text-sm">{{ error }}</p>
          </div>

          <!-- Back to Login -->
          <div class="mt-6 text-center">
            <NuxtLink to="/login" class="text-primary hover:underline font-semibold text-sm">
              ← Quay lại đăng nhập
            </NuxtLink>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
definePageMeta({
  layout: 'default',
  middleware: 'guest'
})

useHead({
  title: 'Quên mật khẩu - Dashboard Tool'
})

const { forgotPassword } = useAuth()

const form = ref({
  email: ''
})

const errors = ref({})
const error = ref('')
const isLoading = ref(false)
const showSuccess = ref(false)
const successMessage = ref('')

const handleForgotPassword = async () => {
  errors.value = {}
  error.value = ''
  isLoading.value = true
  showSuccess.value = false

  const result = await forgotPassword(form.value.email)

  if (result.success) {
    showSuccess.value = true
    successMessage.value = result.message
  } else {
    error.value = result.message || 'Có lỗi xảy ra. Vui lòng thử lại.'
  }

  isLoading.value = false
}
</script>






