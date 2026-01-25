export const useAuth = () => {
  const token = useCookie<string | null>('auth_token', {
    maxAge: 60 * 60 * 24 * 7, // 7 days
    path: '/'
  })
  
  // Store user basic info in cookie to prevent flickering
  const userCookie = useCookie<any>('auth_user', {
    maxAge: 60 * 60 * 24 * 7,
    path: '/'
  })
  
  const user = useState<any>('auth.user', () => userCookie.value || null)
  const { getApiBase } = useApi()

  // Check if user is authenticated
  const isAuthenticated = computed(() => !!token.value)

  // Sync user state with cookie
  watch(user, (newUser) => {
    if (newUser) {
      userCookie.value = {
        id: newUser.id,
        name: newUser.name,
        email: newUser.email,
        role: newUser.role
      }
    } else {
      userCookie.value = null
    }
  })

  // Login
  const login = async (email: string, password: string) => {
    try {
      const response = await $fetch(`${getApiBase()}/api/auth/login`, {
        method: 'POST',
        body: {
          email,
          password
        }
      })

      if (response.success) {
        user.value = response.data.user
        token.value = response.data.token
        return { success: true, data: response.data }
      }

      return { success: false, message: response.message }
    } catch (error: any) {
      return {
        success: false,
        message: error.data?.message || 'Đăng nhập thất bại. Vui lòng thử lại.'
      }
    }
  }

  // Register
  const register = async (data: {
    name: string
    email: string
    password: string
    password_confirmation: string
    phone?: string
  }) => {
    try {
      const response = await $fetch(`${getApiBase()}/api/auth/register`, {
        method: 'POST',
        body: data
      })

      if (response.success) {
        user.value = response.data.user
        token.value = response.data.token
        return { success: true, data: response.data }
      }

      return { success: false, message: response.message, errors: response.errors }
    } catch (error: any) {
      return {
        success: false,
        message: error.data?.message || 'Đăng ký thất bại. Vui lòng thử lại.',
        errors: error.data?.errors
      }
    }
  }

  // Logout
  const logout = async () => {
    try {
      if (token.value) {
        await $fetch(`${getApiBase()}/api/auth/logout`, {
          method: 'POST',
          headers: {
            Authorization: `Bearer ${token.value}`
          }
        })
      }
    } catch (error) {
      console.error('Logout error:', error)
    } finally {
      user.value = null
      token.value = null
      userCookie.value = null
      navigateTo('/login')
    }
  }

  // Get current user
  const fetchUser = async () => {
    if (!token.value) return

    try {
      const response = await $fetch(`${getApiBase()}/api/auth/me`, {
        headers: {
          Authorization: `Bearer ${token.value}`
        }
      })

      if (response.success) {
        // This will trigger the watcher to update userCookie
        user.value = response.data.user
        return { success: true, user: response.data.user }
      }
    } catch (error) {
      // Token invalid, clear auth
      user.value = null
      token.value = null
      userCookie.value = null
    }
  }

  // Initialize auth
  const initAuth = async () => {
    // If we have token but no user, try to fetch
    // But now we have userCookie, so user state might already be populated
    if (token.value && !user.value) {
      await fetchUser()
    } else if (token.value) {
      // Even if we have user from cookie, refresh it in background
      fetchUser()
    }
  }

  // Forgot password
  const forgotPassword = async (email: string) => {
    try {
      const response = await $fetch(`${getApiBase()}/api/auth/forgot-password`, {
        method: 'POST',
        body: { email }
      })

      return {
        success: response.success,
        message: response.message || 'Link đặt lại mật khẩu đã được gửi đến email của bạn'
      }
    } catch (error: any) {
      return {
        success: false,
        message: error.data?.message || 'Có lỗi xảy ra. Vui lòng thử lại.'
      }
    }
  }

  // Reset password
  const resetPassword = async (data: {
    email: string
    token: string
    password: string
    password_confirmation: string
  }) => {
    try {
      const response = await $fetch(`${getApiBase()}/api/auth/reset-password`, {
        method: 'POST',
        body: data
      })

      return {
        success: response.success,
        message: response.message || 'Đặt lại mật khẩu thành công'
      }
    } catch (error: any) {
      return {
        success: false,
        message: error.data?.message || 'Có lỗi xảy ra. Vui lòng thử lại.',
        errors: error.data?.errors
      }
    }
  }

  return {
    user: readonly(user),
    token: readonly(token),
    isAuthenticated,
    login,
    register,
    logout,
    fetchUser,
    initAuth,
    forgotPassword,
    resetPassword
  }
}

