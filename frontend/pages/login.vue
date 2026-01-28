<template>
  <div class="bg-white min-h-screen py-12 md:py-16">
    <div class="container mx-auto px-4">
      <div class="max-w-md mx-auto">
        <!-- Header -->
        <div class="text-center mb-8">
          <h1 class="text-3xl md:text-4xl font-bold text-primary mb-4">
            Đăng nhập
          </h1>
          <p class="text-gray-dark">
            Đăng nhập để tiếp tục mua sắm
          </p>
        </div>

        <!-- Login Form -->
        <div class="bg-white border border-gray-light rounded-lg p-6 md:p-8">
          <form @submit.prevent="handleLogin" class="space-y-6">
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
                placeholder="Nhập mật khẩu"
                class="w-full px-4 py-3 border border-gray-light rounded focus:outline-none focus:ring-2 focus:ring-primary"
                :class="{ 'border-red-500': errors.password }"
              />
              <p v-if="errors.password" class="text-red-500 text-sm mt-1">{{ errors.password }}</p>
            </div>

            <!-- Remember & Forgot -->
            <div class="flex items-center justify-between">
              <label class="flex items-center">
                <input
                  v-model="form.remember"
                  type="checkbox"
                  class="mr-2"
                />
                <span class="text-sm text-gray-dark">Ghi nhớ đăng nhập</span>
              </label>
              <NuxtLink
                to="/forgot-password"
                class="text-sm text-primary hover:underline"
              >
                Quên mật khẩu?
              </NuxtLink>
            </div>

            <!-- Submit Button -->
            <button
              type="submit"
              :disabled="isLoading"
              class="w-full bg-primary text-white px-6 py-4 rounded font-semibold hover:bg-primary-dark transition-colors disabled:opacity-50 disabled:cursor-not-allowed text-lg"
            >
              {{ isLoading ? 'Đang đăng nhập...' : 'Đăng nhập' }}
            </button>
          </form>

          <!-- Error Message -->
          <div v-if="error" class="mt-6 p-4 bg-red-50 border border-red-200 rounded text-red-800">
            <p class="text-sm">{{ error }}</p>
          </div>

          <!-- Register Link -->
          <div class="mt-6 text-center">
            <p class="text-gray-dark text-sm">
              Chưa có tài khoản?
              <NuxtLink to="/register" class="text-primary hover:underline font-semibold">
                Đăng ký ngay
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
  title: 'Đăng nhập - Dashboard Tool'
})

const { login } = useAuth()
const router = useRouter()

const form = ref({
  email: '',
  password: '',
  remember: false
})

const errors = ref({})
const error = ref('')
const isLoading = ref(false)

const handleLogin = async () => {
  errors.value = {}
  error.value = ''
  isLoading.value = true

  const result = await login(form.value.email, form.value.password)

  if (result.success) {
    // Redirect to home or intended page
    const redirectQuery = router.currentRoute.value.query.redirect
    const redirectTo = Array.isArray(redirectQuery) ? redirectQuery[0] : (redirectQuery || '/')
    navigateTo(redirectTo)
  } else {
    error.value = result.message || 'Đăng nhập thất bại'
    if (result.errors) {
      errors.value = result.errors
    }
  }

  isLoading.value = false
}
</script>

