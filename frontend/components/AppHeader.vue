<template>
  <header class="bg-white border-b border-gray-light">
    <div class="container mx-auto px-4">
      <div class="flex items-center justify-between h-16">
        <!-- Logo -->
        <NuxtLink to="/" class="text-xl font-bold text-primary">
          Clothes Store
        </NuxtLink>

        <!-- Navigation Menu -->
        <nav class="hidden md:flex items-center space-x-8">
          <NuxtLink 
            to="/" 
            class="text-gray-dark hover:text-primary transition-colors"
            active-class="text-primary font-semibold"
          >
            Trang chủ
          </NuxtLink>
          <NuxtLink 
            to="/products" 
            class="text-gray-dark hover:text-primary transition-colors"
            active-class="text-primary font-semibold"
          >
            Sản phẩm
          </NuxtLink>
          <NuxtLink 
            to="/order" 
            class="text-gray-dark hover:text-primary transition-colors text-sm"
            active-class="text-primary font-semibold"
          >
            Đặt hàng
          </NuxtLink>
          <NuxtLink 
            to="/track-order" 
            class="text-gray-dark hover:text-primary transition-colors text-sm"
            active-class="text-primary font-semibold"
          >
            Tra cứu đơn
          </NuxtLink>
        </nav>

        <!-- Auth Buttons / User Menu -->
        <div class="flex items-center gap-4">
          <!-- Loading State (SSR + Initial Client) -->
          <div v-if="!isMounted" class="flex items-center gap-4">
               <div class="w-20 h-8 bg-gray-100 rounded animate-pulse"></div>
               <div class="w-24 h-10 bg-gray-100 rounded animate-pulse"></div>
          </div>

          <!-- Authenticated -->
          <div v-else-if="isAuthenticated" class="flex items-center gap-4">
              <!-- User Menu -->
              <div class="relative" ref="userMenuRef">
                <button
                  @click="userMenuOpen = !userMenuOpen"
                  class="flex items-center gap-2 text-gray-dark hover:text-primary transition-colors"
                >
                  <span class="hidden md:inline">{{ user?.name }}</span>
                  <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                  </svg>
                </button>
                
                <!-- Dropdown Menu -->
                <div
                  v-if="userMenuOpen"
                  class="absolute right-0 mt-2 w-48 bg-white border border-gray-light rounded-lg shadow-lg z-50"
                >
                  <div class="p-4 border-b border-gray-light">
                    <p class="font-semibold text-primary">{{ user?.name }}</p>
                    <p class="text-sm text-gray-dark">{{ user?.email }}</p>
                  </div>
                  <div class="p-2">
                    <NuxtLink
                      to="/admin"
                      class="block px-4 py-2 text-sm text-gray-dark hover:bg-gray-50 rounded"
                      @click="userMenuOpen = false"
                    >
                      Quản trị
                    </NuxtLink>
                    <button
                      @click="handleLogout"
                      class="w-full text-left px-4 py-2 text-sm text-gray-dark hover:bg-gray-50 rounded"
                    >
                      Đăng xuất
                    </button>
                  </div>
                </div>
              </div>
          </div>
            
          <!-- Guest -->
          <div v-else class="flex items-center gap-4">
              <NuxtLink
                to="/login"
                class="text-gray-dark hover:text-primary transition-colors font-medium"
              >
                Đăng nhập
              </NuxtLink>
              <NuxtLink
                to="/register"
                class="bg-primary text-white px-6 py-2 rounded hover:bg-primary-dark transition-colors font-medium"
              >
                Đăng ký
              </NuxtLink>
          </div>
          
          <!-- CTA Button (always visible) -->
          <NuxtLink 
            to="/products"
            class="bg-primary text-white px-6 py-2 rounded hover:bg-primary-dark transition-colors font-medium"
          >
            Xem sản phẩm
          </NuxtLink>
        </div>

        <!-- Mobile Menu Button -->
        <button 
          @click="mobileMenuOpen = !mobileMenuOpen"
          class="md:hidden text-gray-dark"
          aria-label="Toggle menu"
        >
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path v-if="!mobileMenuOpen" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
            <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
      </div>

      <!-- Mobile Menu -->
      <div v-if="mobileMenuOpen" class="md:hidden py-4 border-t border-gray-light">
        <nav class="flex flex-col space-y-4">
          <NuxtLink 
            to="/" 
            @click="mobileMenuOpen = false"
            class="text-gray-dark hover:text-primary transition-colors"
            active-class="text-primary font-semibold"
          >
            Trang chủ
          </NuxtLink>
          <NuxtLink 
            to="/products" 
            @click="mobileMenuOpen = false"
            class="text-gray-dark hover:text-primary transition-colors"
            active-class="text-primary font-semibold"
          >
            Sản phẩm
          </NuxtLink>
          <NuxtLink 
            to="/order" 
            @click="mobileMenuOpen = false"
            class="text-gray-dark hover:text-primary transition-colors text-sm"
            active-class="text-primary font-semibold"
          >
            Đặt hàng
          </NuxtLink>
          <NuxtLink 
            to="/track-order" 
            @click="mobileMenuOpen = false"
            class="text-gray-dark hover:text-primary transition-colors text-sm"
            active-class="text-primary font-semibold"
          >
            Tra cứu đơn
          </NuxtLink>
        </nav>
      </div>
    </div>
  </header>
</template>

<script setup>
const { user, isAuthenticated, logout } = useAuth()
const mobileMenuOpen = ref(false)
const userMenuOpen = ref(false)
const userMenuRef = ref(null)
const isMounted = ref(false)

onMounted(() => {
  isMounted.value = true
})

const handleLogout = async () => {
  userMenuOpen.value = false
  await logout()
}

// Close user menu when clicking outside
onMounted(() => {
  if (process.client) {
    document.addEventListener('click', (e) => {
      if (userMenuRef.value && !userMenuRef.value.contains(e.target)) {
        userMenuOpen.value = false
      }
    })
  }
})
</script>

