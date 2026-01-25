<template>
  <div class="bg-white min-h-screen py-12 md:py-16">
    <div class="container mx-auto px-4">
      <div class="max-w-md mx-auto">
        <!-- Header -->
        <div class="text-center mb-8">
          <h1 class="text-3xl md:text-4xl font-bold text-primary mb-4">
            Đăng ký
          </h1>
          <p class="text-gray-dark">
            Tạo tài khoản để mua sắm dễ dàng hơn
          </p>
        </div>

        <!-- Register Form -->
        <div class="bg-white border border-gray-light rounded-lg p-6 md:p-8">
          <form @submit.prevent="handleRegister" class="space-y-6">
            <!-- Name -->
            <div>
              <label for="name" class="block text-sm font-semibold text-primary mb-2">
                Họ và tên <span class="text-red-500">*</span>
              </label>
              <input
                id="name"
                v-model="form.name"
                type="text"
                required
                placeholder="Nguyễn Văn A"
                class="w-full px-4 py-3 border border-gray-light rounded focus:outline-none focus:ring-2 focus:ring-primary"
                :class="{ 'border-red-500': errors.name }"
              />
              <p v-if="errors.name" class="text-red-500 text-sm mt-1">{{ errors.name }}</p>
            </div>

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

            <!-- Phone -->
            <div>
              <label for="phone" class="block text-sm font-semibold text-primary mb-2">
                Số điện thoại
              </label>
              <input
                id="phone"
                v-model="form.phone"
                type="tel"
                placeholder="0901234567"
                class="w-full px-4 py-3 border border-gray-light rounded focus:outline-none focus:ring-2 focus:ring-primary"
                :class="{ 'border-red-500': errors.phone }"
              />
              <p v-if="errors.phone" class="text-red-500 text-sm mt-1">{{ errors.phone }}</p>
            </div>

            <!-- Password -->
            <div>
              <label for="password" class="block text-sm font-semibold text-primary mb-2">
                Mật khẩu <span class="text-red-500">*</span>
              </label>
              <input
                id="password"
                v-model="form.password"
                type="password"
                required
                placeholder="Tối thiểu 8 ký tự"
                class="w-full px-4 py-3 border border-gray-light rounded focus:outline-none focus:ring-2 focus:ring-primary"
                :class="{ 'border-red-500': errors.password }"
              />
              <p v-if="errors.password" class="text-red-500 text-sm mt-1">{{ errors.password }}</p>
            </div>

            <!-- Confirm Password -->
            <div>
              <label for="password_confirmation" class="block text-sm font-semibold text-primary mb-2">
                Xác nhận mật khẩu <span class="text-red-500">*</span>
              </label>
              <input
                id="password_confirmation"
                v-model="form.password_confirmation"
                type="password"
                required
                placeholder="Nhập lại mật khẩu"
                class="w-full px-4 py-3 border border-gray-light rounded focus:outline-none focus:ring-2 focus:ring-primary"
                :class="{ 'border-red-500': errors.password_confirmation }"
              />
              <p v-if="errors.password_confirmation" class="text-red-500 text-sm mt-1">{{ errors.password_confirmation }}</p>
            </div>

            <!-- Submit Button -->
            <button
              type="submit"
              :disabled="isLoading"
              class="w-full bg-primary text-white px-6 py-4 rounded font-semibold hover:bg-primary-dark transition-colors disabled:opacity-50 disabled:cursor-not-allowed text-lg"
            >
              {{ isLoading ? 'Đang đăng ký...' : 'Đăng ký' }}
            </button>
          </form>

          <!-- Error Message -->
          <div v-if="error" class="mt-6 p-4 bg-red-50 border border-red-200 rounded text-red-800">
            <p class="text-sm">{{ error }}</p>
          </div>

          <!-- Success Message -->
          <div v-if="showSuccess" class="mt-6 p-4 bg-green-50 border border-green-200 rounded text-green-800">
            <p class="text-sm">Đăng ký thành công! Đang chuyển hướng...</p>
          </div>

          <!-- Login Link -->
          <div class="mt-6 text-center">
            <p class="text-gray-dark text-sm">
              Đã có tài khoản?
              <NuxtLink to="/login" class="text-primary hover:underline font-semibold">
                Đăng nhập ngay
              </NuxtLink>
            </p>
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
  title: 'Đăng ký - Clothes Store'
})

const { register } = useAuth()
const router = useRouter()

const form = ref({
  name: '',
  email: '',
  phone: '',
  password: '',
  password_confirmation: ''
})

const errors = ref({})
const error = ref('')
const isLoading = ref(false)
const showSuccess = ref(false)

const handleRegister = async () => {
  errors.value = {}
  error.value = ''
  isLoading.value = true
  showSuccess.value = false

  const result = await register(form.value)

  if (result.success) {
    showSuccess.value = true
    setTimeout(() => {
      navigateTo('/')
    }, 1500)
  } else {
    error.value = result.message || 'Đăng ký thất bại'
    if (result.errors) {
      errors.value = result.errors
    }
  }

  isLoading.value = false
}
</script>






