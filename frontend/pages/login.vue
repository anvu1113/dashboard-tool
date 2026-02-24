<template>
  <div class="min-h-screen flex items-center justify-center bg-bg-dark text-text">
    <div class="w-full max-w-md p-8 bg-card-dark border border-gray-700 rounded-xl shadow-2xl">
      <!-- Header -->
      <div class="text-center mb-8">
        <h1 class="text-3xl font-bold bg-gradient-to-r from-blue-400 to-blue-600 bg-clip-text text-transparent mb-2">
          Đăng Nhập
        </h1>
        <p class="text-gray-400">
          Đăng nhập để tiếp tục mua sắm
        </p>
      </div>

      <!-- Login Form -->
      <form @submit.prevent="handleLogin" class="space-y-6">
        <!-- Email -->
        <div>
          <label for="email" class="block text-sm font-medium text-gray-300 mb-2">
            Email
          </label>
          <input
            id="email"
            v-model="form.email"
            type="email"
            required
            placeholder="your@email.com"
            class="block w-full bg-bg-dark border border-gray-600 text-white rounded-lg py-3 px-4 focus:ring-2 focus:ring-primary focus:border-transparent outline-none"
            :class="{ 'border-red-500': errors.email }"
          />
          <p v-if="errors.email" class="text-red-500 text-sm mt-1">{{ errors.email }}</p>
        </div>

        <!-- Password -->
        <div>
          <label for="password" class="block text-sm font-medium text-gray-300 mb-2">
            Mật khẩu
          </label>
          <div class="relative">
            <input
              id="password"
              v-model="form.password"
              :type="showPassword ? 'text' : 'password'"
              required
              placeholder="Nhập mật khẩu"
              class="block w-full bg-bg-dark border border-gray-600 text-white rounded-lg py-3 px-4 pr-10 focus:ring-2 focus:ring-primary focus:border-transparent outline-none"
              :class="{ 'border-red-500': errors.password }"
            />
            <button
              type="button"
              @click="showPassword = !showPassword"
              class="absolute inset-y-0 right-0 px-3 flex items-center text-gray-400 hover:text-gray-200 transition-colors"
            >
              <EyeIcon v-if="!showPassword" class="w-5 h-5" />
              <EyeSlashIcon v-else class="w-5 h-5" />
            </button>
          </div>
          <p v-if="errors.password" class="text-red-500 text-sm mt-1">{{ errors.password }}</p>
        </div>

        <!-- Remember & Forgot -->
        <div class="flex items-center justify-between">
          <label class="flex items-center">
            <input
              v-model="form.remember"
              type="checkbox"
              class="mr-2 rounded bg-bg-dark border-gray-600 text-primary focus:ring-primary"
            />
            <span class="text-sm text-gray-400">Ghi nhớ đăng nhập</span>
          </label>
          <NuxtLink
            to="/forgot-password"
            class="text-sm text-primary hover:text-primary-hover transition-colors"
          >
            Quên mật khẩu?
          </NuxtLink>
        </div>

        <!-- Submit Button -->
        <button
          type="submit"
          :disabled="isLoading"
          class="w-full py-3 px-4 bg-gradient-to-r from-blue-500 to-blue-600 hover:from-blue-600 hover:to-blue-700 text-white font-bold rounded-lg shadow-lg transition-all flex justify-center items-center disabled:opacity-50 disabled:cursor-not-allowed"
        >
           <svg v-if="isLoading" class="animate-spin -ml-1 mr-3 h-5 w-5 text-white" fill="none" viewBox="0 0 24 24">
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
          </svg>
          {{ isLoading ? 'Đang đăng nhập...' : 'Đăng nhập' }}
        </button>

        <!-- Error Message -->
        <div v-if="error" class="p-4 bg-red-900/50 border border-red-700 rounded text-red-200">
          <p class="text-sm">{{ error }}</p>
        </div>

        <!-- Register Link -->
        <div class="text-center mt-6">
          <p class="text-gray-400 text-sm">
            Chưa có tài khoản?
            <NuxtLink to="/register" class="text-primary hover:text-primary-hover font-bold transition-colors">
              Đăng ký ngay
            </NuxtLink>
          </p>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
definePageMeta({
  layout: false,
  middleware: 'guest'
})

useHead({
  title: 'Đăng nhập - Dashboard Tool'
})

const { login } = useAuth()
const router = useRouter()
import { EyeIcon, EyeSlashIcon } from '@heroicons/vue/24/outline'

const showPassword = ref(false)

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

