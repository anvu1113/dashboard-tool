<template>
  <div>
    <!-- Header -->
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold bg-gradient-to-r from-white to-gray-200 bg-clip-text text-transparent">
        Cache Management
      </h1>
      <button @click="clearAllCaches" class="bg-red-500/10 border border-red-500/50 text-red-400 px-6 py-3 rounded-lg hover:bg-red-500/20 transition-all duration-200 font-medium flex items-center gap-2">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" /></svg>
        Clear All Caches
      </button>
    </div>

    <!-- Cache Cards Grid -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
      <div v-for="cache in caches" :key="cache.name" class="bg-card-dark border border-gray-700/50 rounded-xl p-6 shadow-xl hover:border-gray-600/50 transition-colors">
        <!-- Cache Header -->
        <div class="flex items-start justify-between mb-4">
          <div class="flex items-center gap-3">
            <div class="text-3xl">{{ getCacheIcon(cache.name) }}</div>
            <div>
              <h3 class="text-lg font-semibold text-white">{{ getCacheName(cache.name) }}</h3>
              <div class="flex items-center gap-2 mt-1">
                <span :class="cache.is_active ? 'bg-green-500' : 'bg-gray-500'" class="w-2 h-2 rounded-full"></span>
                <span :class="cache.is_active ? 'text-green-400' : 'text-gray-400'" class="text-sm">
                  {{ cache.is_active ? 'Active' : 'Inactive' }}
                </span>
              </div>
            </div>
          </div>
        </div>

        <!-- Cache Stats -->
        <div class="space-y-2 mb-4">
          <div v-if="cache.expires_at" class="flex justify-between text-sm">
            <span class="text-gray-400">Expires:</span>
            <span class="text-white font-medium">{{ formatExpiry(cache.expires_at) }}</span>
          </div>
          <div v-if="cache.item_count !== null" class="flex justify-between text-sm">
            <span class="text-gray-400">Items:</span>
            <span class="text-white font-medium">{{ cache.item_count }}</span>
          </div>
          <div class="flex justify-between text-sm">
            <span class="text-gray-400">Duration:</span>
            <span class="text-white font-medium">{{ formatDuration(cache.duration_seconds) }}</span>
          </div>
        </div>

        <!-- Clear Button -->
        <button 
          @click="clearCache(cache.name)" 
          :disabled="!cache.is_active"
          class="w-full bg-blue-500/10 border border-blue-500/50 text-blue-400 px-4 py-2 rounded-lg hover:bg-blue-500/20 disabled:opacity-50 disabled:cursor-not-allowed transition-all duration-200 font-medium"
        >
          Clear Cache
        </button>
      </div>

      <!-- Placeholder for future caches -->
      <div v-for="i in placeholderCount" :key="`placeholder-${i}`" class="bg-card-dark border border-gray-700/50 border-dashed rounded-xl p-6 shadow-xl flex items-center justify-center">
        <div class="text-center text-gray-500">
          <div class="text-4xl mb-2">📦</div>
          <p class="text-sm">Future Cache Slot</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
definePageMeta({
  layout: 'admin',
})

const caches = ref([])
const { token } = useAuth()
const toast = useToast()
const { confirmDelete, alert } = useConfirm()
const isLoading = ref(false)

// Calculate placeholder slots (always show at least 4 cards total)
const placeholderCount = computed(() => {
  const minCards = 4
  return Math.max(0, minCards - caches.value.length)
})

const fetchCacheStatus = async () => {
  isLoading.value = true
  try {
    const data = await $fetch('/api/admin/cache/status', {
      headers: {
        Authorization: `Bearer ${token.value}`
      }
    })
    
    if (data.success) {
      caches.value = data.data
    }
  } catch (e) {
    console.error('Fetch error:', e)
    if (e.response?.status === 401 || e.response?.status === 403) {
      await alert('Phiên đăng nhập hết hạn hoặc không có quyền. Vui lòng đăng nhập lại.', 'Lỗi Xác Thực')
      navigateTo('/admin/login')
    } else {
      toast.error('Không thể tải thông tin cache')
    }
  } finally {
    isLoading.value = false
  }
}

const clearCache = async (cacheName) => {
  const isConfirmed = await confirmDelete(`Bạn có chắc muốn xóa cache "${getCacheName(cacheName)}"?`)
  if (!isConfirmed) return

  try {
    const data = await $fetch(`/api/admin/cache/clear/${cacheName}`, {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${token.value}`
      }
    })

    if (data.success) {
      toast.success(data.message)
      fetchCacheStatus()
    } else {
      toast.error(data.message)
    }
  } catch (e) {
    toast.error('Có lỗi khi xóa cache: ' + (e.data?.detail || e.message))
  }
}

const clearAllCaches = async () => {
  const isConfirmed = await confirmDelete('Bạn có chắc muốn xóa TẤT CẢ cache?')
  if (!isConfirmed) return

  try {
    const data = await $fetch('/api/admin/cache/clear-all', {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${token.value}`
      }
    })

    if (data.success) {
      toast.success(data.message)
      fetchCacheStatus()
    }
  } catch (e) {
    toast.error('Có lỗi khi xóa cache: ' + (e.data?.detail || e.message))
  }
}

const getCacheIcon = (name) => {
  const icons = {
    'supported_domains': '🌐',
    'translation': '🔤',
    'user_sessions': '👥',
  }
  return icons[name] || '📦'
}

const getCacheName = (name) => {
  const names = {
    'supported_domains': 'Supported Domains',
    'translation': 'Translation Results',
    'user_sessions': 'User Sessions',
  }
  return names[name] || name.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase())
}

const formatExpiry = (expiresAt) => {
  if (!expiresAt) return 'N/A'
  
  const now = new Date()
  const expiry = new Date(expiresAt)
  const diff = expiry - now
  
  if (diff <= 0) return 'Expired'
  
  const days = Math.floor(diff / (1000 * 60 * 60 * 24))
  const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60))
  
  if (days > 0) {
    return `${days}d ${hours}h`
  } else if (hours > 0) {
    const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60))
    return `${hours}h ${minutes}m`
  } else {
    const minutes = Math.floor(diff / (1000 * 60))
    return `${minutes}m`
  }
}

const formatDuration = (seconds) => {
  const days = Math.floor(seconds / (60 * 60 * 24))
  const hours = Math.floor((seconds % (60 * 60 * 24)) / (60 * 60))
  
  if (days > 0) {
    return `${days} day${days > 1 ? 's' : ''}`
  } else if (hours > 0) {
    return `${hours} hour${hours > 1 ? 's' : ''}`
  } else {
    const minutes = Math.floor(seconds / 60)
    return `${minutes} minute${minutes > 1 ? 's' : ''}`
  }
}

// Auto-refresh every 30 seconds
let refreshInterval = null

onMounted(() => {
  fetchCacheStatus()
  refreshInterval = setInterval(fetchCacheStatus, 30000)
})

onUnmounted(() => {
  if (refreshInterval) {
    clearInterval(refreshInterval)
  }
})
</script>
