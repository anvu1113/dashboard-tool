<template>
  <div class="min-h-screen bg-gradient-to-br from-gray-900 via-gray-800 to-gray-900 flex">
    <!-- Dark Sidebar -->
    <aside class="w-64 bg-gray-800/50 backdrop-blur-xl border-r border-gray-700/50 hidden md:block flex-shrink-0 shadow-2xl">
      <!-- Logo Area -->
      <div class="p-6 border-b border-gray-700/50">
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 bg-gradient-to-br from-primary to-primary-dark rounded-lg flex items-center justify-center shadow-lg shadow-primary/50">
            <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
            </svg>
          </div>
          <div>
            <h2 class="text-lg font-bold text-white">Admin Panel</h2>
            <p class="text-xs text-gray-400">Quản trị hệ thống</p>
          </div>
        </div>
      </div>

      <!-- Navigation Menu -->
      <nav class="p-4 space-y-1">
        <NuxtLink 
          to="/admin" 
          class="flex items-center gap-3 px-4 py-3 rounded-lg transition-all duration-200 group"
          :class="route.path === '/admin' 
            ? 'bg-gradient-to-r from-primary to-primary-dark text-white shadow-lg shadow-primary/50' 
            : 'text-gray-300 hover:bg-gray-700/50 hover:text-white'"
        >
          <svg class="w-5 h-5" :class="route.path === '/admin' ? 'text-white' : 'text-gray-400 group-hover:text-primary'" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
          </svg>
          <span class="font-medium">Dashboard</span>
        </NuxtLink>

        <NuxtLink 
          to="/admin/orders" 
          class="flex items-center gap-3 px-4 py-3 rounded-lg transition-all duration-200 group"
          :class="route.path.startsWith('/admin/orders')
            ? 'bg-gradient-to-r from-primary to-primary-dark text-white shadow-lg shadow-primary/50' 
            : 'text-gray-300 hover:bg-gray-700/50 hover:text-white'"
        >
          <svg class="w-5 h-5" :class="route.path.startsWith('/admin/orders') ? 'text-white' : 'text-gray-400 group-hover:text-primary'" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
          </svg>
          <span class="font-medium">Đơn hàng</span>
        </NuxtLink>

        <NuxtLink 
          to="/admin/products" 
          class="flex items-center gap-3 px-4 py-3 rounded-lg transition-all duration-200 group"
          :class="route.path.startsWith('/admin/products')
            ? 'bg-gradient-to-r from-primary to-primary-dark text-white shadow-lg shadow-primary/50' 
            : 'text-gray-300 hover:bg-gray-700/50 hover:text-white'"
        >
          <svg class="w-5 h-5" :class="route.path.startsWith('/admin/products') ? 'text-white' : 'text-gray-400 group-hover:text-primary'" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4" />
          </svg>
          <span class="font-medium">Sản phẩm</span>
        </NuxtLink>

        <NuxtLink 
          to="/admin/categories" 
          class="flex items-center gap-3 px-4 py-3 rounded-lg transition-all duration-200 group"
          :class="route.path.startsWith('/admin/categories')
            ? 'bg-gradient-to-r from-primary to-primary-dark text-white shadow-lg shadow-primary/50' 
            : 'text-gray-300 hover:bg-gray-700/50 hover:text-white'"
        >
          <svg class="w-5 h-5" :class="route.path.startsWith('/admin/categories') ? 'text-white' : 'text-gray-400 group-hover:text-primary'" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 7h.01M7 3h5c.512 0 1.024.195 1.414.586l7 7a2 2 0 010 2.828l-7 7a2 2 0 01-2.828 0l-7-7A1.994 1.994 0 013 12V7a4 4 0 014-4z" />
          </svg>
          <span class="font-medium">Loại sản phẩm</span>
        </NuxtLink>

        <NuxtLink 
          to="/admin/posts" 
          class="flex items-center gap-3 px-4 py-3 rounded-lg transition-all duration-200 group"
          :class="route.path.startsWith('/admin/posts')
            ? 'bg-gradient-to-r from-primary to-primary-dark text-white shadow-lg shadow-primary/50' 
            : 'text-gray-300 hover:bg-gray-700/50 hover:text-white'"
        >
          <svg class="w-5 h-5" :class="route.path.startsWith('/admin/posts') ? 'text-white' : 'text-gray-400 group-hover:text-primary'" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9M7 16h6M7 8h6v4H7V8z" />
          </svg>
          <span class="font-medium">Bài viết</span>
        </NuxtLink>

        <NuxtLink 
          to="/admin/post-categories" 
          class="flex items-center gap-3 px-4 py-3 rounded-lg transition-all duration-200 group"
          :class="route.path.startsWith('/admin/post-categories')
            ? 'bg-gradient-to-r from-primary to-primary-dark text-white shadow-lg shadow-primary/50' 
            : 'text-gray-300 hover:bg-gray-700/50 hover:text-white'"
        >
          <svg class="w-5 h-5" :class="route.path.startsWith('/admin/post-categories') ? 'text-white' : 'text-gray-400 group-hover:text-primary'" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 7h.01M7 3h5c.512 0 1.024.195 1.414.586l7 7a2 2 0 010 2.828l-7 7a2 2 0 01-2.828 0l-7-7A1.994 1.994 0 013 12V7a4 4 0 014-4z" />
          </svg>
          <span class="font-medium">Loại tin tức</span>
        </NuxtLink>
      </nav>
    </aside>

    <!-- Main Content -->
    <div class="flex-1 flex flex-col overflow-hidden">
      <!-- Dark Header -->
      <header class="bg-gray-800/50 backdrop-blur-xl border-b border-gray-700/50 py-4 px-6 flex justify-between items-center z-10 shadow-lg">
        <div>
          <h1 class="text-2xl font-bold bg-gradient-to-r from-white to-gray-300 bg-clip-text text-transparent">{{ getPageTitle() }}</h1>
          <p class="text-sm text-gray-400 mt-1">{{ getPageDescription() }}</p>
        </div>

        <!-- User Menu with Dropdown -->
        <div class="flex items-center gap-4">
          <!-- Loading State -->
          <div v-if="!isMounted" class="flex items-center gap-3">
            <div class="w-32 h-10 bg-gray-700/50 rounded-lg animate-pulse"></div>
          </div>

          <!-- Authenticated - Dropdown Menu -->
          <div v-else-if="user" class="relative" ref="userMenuRef">
            <button 
              @click="toggleUserMenu"
              class="flex items-center gap-3 bg-gradient-to-r from-gray-700/50 to-gray-600/50 backdrop-blur-sm px-4 py-2 rounded-lg border border-gray-600/50 hover:border-primary/50 transition-all duration-200 cursor-pointer"
            >
              <div class="w-10 h-10 rounded-full bg-gradient-to-br from-primary to-primary-dark flex items-center justify-center text-white font-bold text-sm shadow-lg shadow-primary/50">
                {{ user.name.charAt(0).toUpperCase() }}
              </div>
              <div class="text-left">
                <div class="text-sm font-semibold text-white">{{ user.name }}</div>
                <div class="text-xs text-gray-400">{{ user.role || 'Administrator' }}</div>
              </div>
              <svg class="w-4 h-4 text-gray-400" :class="{ 'rotate-180': userMenuOpen }" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
              </svg>
            </button>

            <!-- Dropdown -->
            <div 
              v-if="userMenuOpen"
              class="absolute right-0 mt-2 w-56 bg-gray-800 border border-gray-700 rounded-lg shadow-2xl py-2 z-50"
            >
              <div class="px-4 py-3 border-b border-gray-700">
                <p class="text-sm font-semibold text-white">{{ user.name }}</p>
                <p class="text-xs text-gray-400">{{ user.email }}</p>
              </div>
              
              <NuxtLink 
                to="/" 
                class="flex items-center gap-3 px-4 py-3 text-sm text-gray-300 hover:bg-gray-700/50 hover:text-white transition-colors"
                @click="userMenuOpen = false"
              >
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
                </svg>
                Về trang chủ
              </NuxtLink>

              <button 
                @click="handleLogout"
                class="flex items-center gap-3 px-4 py-3 text-sm text-red-400 hover:bg-red-900/20 hover:text-red-300 transition-colors w-full text-left"
              >
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
                </svg>
                Đăng xuất
              </button>
            </div>
          </div>
        </div>
      </header>

      <!-- Content Area -->
      <main class="flex-1 overflow-auto p-6">
        <AdminBreadcrumb :items="breadcrumbs" />
        <slot />
      </main>
    </div>
  </div>
</template>

<script setup>
const route = useRoute()
const router = useRouter()
const { user, logout: authLogout } = useAuth()
const { breadcrumbs } = useBreadcrumb()
const isMounted = ref(false)
const userMenuOpen = ref(false)
const userMenuRef = ref(null)

onMounted(() => {
  isMounted.value = true
  
  // Close dropdown when clicking outside
  document.addEventListener('click', handleClickOutside)
})

onBeforeUnmount(() => {
  document.removeEventListener('click', handleClickOutside)
})

const handleClickOutside = (event) => {
  if (userMenuRef.value && !userMenuRef.value.contains(event.target)) {
    userMenuOpen.value = false
  }
}

const toggleUserMenu = () => {
  userMenuOpen.value = !userMenuOpen.value
}

const handleLogout = async () => {
  userMenuOpen.value = false
  await authLogout()
  router.push('/login')
}

const getPageTitle = () => {
  const path = route.path
  if (path === '/admin') return 'Dashboard'
  if (path.startsWith('/admin/orders')) return 'Quản lý Đơn hàng'
  if (path.startsWith('/admin/products')) return 'Quản lý Sản phẩm'
  if (path.startsWith('/admin/categories')) return 'Quản lý Loại sản phẩm'
  if (path.startsWith('/admin/posts')) return 'Quản lý Bài viết'
  return 'Admin Panel'
}

const getPageDescription = () => {
  const path = route.path
  if (path === '/admin') return 'Tổng quan hệ thống'
  if (path.startsWith('/admin/orders')) return 'Theo dõi và xử lý đơn hàng'
  if (path.startsWith('/admin/products')) return 'Quản lý danh mục sản phẩm'
  if (path.startsWith('/admin/categories')) return 'Phân loại sản phẩm'
  if (path.startsWith('/admin/posts')) return 'Quản lý nội dung blog'
  return 'Quản trị hệ thống'
}
</script>
