<template>
  <div class="min-h-screen flex items-center justify-center bg-bg-dark text-text">
    <div class="w-full max-w-md p-8 bg-card-dark border border-gray-700 rounded-xl shadow-2xl">
      <div class="text-center mb-8">
        <h1 class="text-3xl font-bold bg-gradient-to-r from-blue-400 to-blue-600 bg-clip-text text-transparent mb-2">
          Admin Login
        </h1>
        <p class="text-gray-400">Đăng nhập để quản lý hệ thống</p>
      </div>

      <form @submit.prevent="handleLogin" class="space-y-6">
        <div>
          <label class="block text-sm font-medium text-gray-300 mb-2">Email</label>
          <input type="email" v-model="email" class="block w-full bg-bg-dark border border-gray-600 text-white rounded-lg py-3 px-4 focus:ring-2 focus:ring-primary focus:border-transparent outline-none" required placeholder="admin@example.com">
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-300 mb-2">Mật khẩu</label>
          <input type="password" v-model="password" class="block w-full bg-bg-dark border border-gray-600 text-white rounded-lg py-3 px-4 focus:ring-2 focus:ring-primary focus:border-transparent outline-none" required placeholder="••••••••">
        </div>

        <button type="submit" :disabled="loading" class="w-full py-3 px-4 bg-gradient-to-r from-blue-500 to-blue-600 hover:from-blue-600 hover:to-blue-700 text-white font-bold rounded-lg shadow-lg transition-all flex justify-center items-center">
          <svg v-if="loading" class="animate-spin -ml-1 mr-3 h-5 w-5 text-white" fill="none" viewBox="0 0 24 24">
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
          </svg>
          {{ loading ? 'Đang xử lý...' : 'Đăng nhập' }}
        </button>

        <div class="text-center mt-6">
          <p class="text-gray-400 text-sm">
            Chưa có tài khoản?
            <NuxtLink to="/admin/register" class="text-primary hover:text-primary-hover font-bold transition-colors">
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
  layout: false
})

const email = ref('')
const password = ref('')
const loading = ref(false)
const router = useRouter()

const { login } = useAuth()
// const router = useRouter() // Already defined
const toast = useToast()

const handleLogin = async () => {
  loading.value = true
  try {
    const res = await login(email.value, password.value)
    
    if (res.success) {
        toast.success('Đăng nhập thành công')
        // useAuth handles state/cookie update
        // Redirect
        router.push('/admin/dashboard') 
    } else {
        toast.error(res.message || 'Đăng nhập thất bại')
    }
  } catch (e) {
      toast.error('Có lỗi xảy ra: ' + e.message)
  } finally {
    loading.value = false
  }
}

useHead({
  title: 'Admin Login - ExtensionHub'
})
</script>
