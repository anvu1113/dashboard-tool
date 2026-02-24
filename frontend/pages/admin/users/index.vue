<template>
  <div>
    <!-- Header -->
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold bg-gradient-to-r from-white to-gray-200 bg-clip-text text-transparent">
        Quản lý người dùng
      </h1>
      <button 
        v-if="$can('users.create')"
        @click="openCreateModal" 
        class="bg-gradient-to-r from-green-500 to-green-600 text-white px-6 py-3 rounded-lg hover:shadow-lg hover:shadow-green-500/50 transition-all duration-200 font-medium flex items-center gap-2"
      >
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
        </svg>
        Thêm mới
      </button>
    </div>

    <!-- Filters/Search -->
    <div class="mb-6 flex gap-4">
      <div class="relative flex-1 max-w-md">
        <input 
          v-model="tempSearch"
          @keydown.enter="handleSearch"
          type="text" 
          placeholder="Tìm kiếm theo email, tên..." 
          class="block w-full bg-card-dark border border-gray-600 text-white rounded-lg py-3 pl-10 pr-4 focus:ring-2 focus:ring-primary focus:border-transparent outline-none"
        >
        <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
          <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" /></svg>
        </div>
      </div>
       <select v-model="tempRoleFilter" class="bg-card-dark border border-gray-600 text-white rounded-lg px-4 focus:ring-2 focus:ring-primary focus:border-transparent outline-none">
          <option value="">Tất cả vai trò</option>
          <option v-for="role in rolesList" :key="role.id" :value="role.code">
            {{ role.name || role.code }}
          </option>
      </select>
      <button 
        @click="handleSearch"
        class="bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-lg transition-colors font-medium flex items-center gap-2"
      >
        Tìm kiếm
      </button>
    </div>

    <!-- Table -->
    <div class="bg-card-dark rounded-lg shadow-xl border border-gray-700/50 overflow-hidden">
      <table class="min-w-full divide-y divide-gray-700/50">
        <thead class="bg-gray-800/50">
          <tr>
            <th class="px-6 py-4 text-left text-xs font-semibold text-gray-300 uppercase tracking-wider">ID</th>
            <th class="px-6 py-4 text-left text-xs font-semibold text-gray-300 uppercase tracking-wider">Email</th>
            <th class="px-6 py-4 text-left text-xs font-semibold text-gray-300 uppercase tracking-wider">Tên</th>
            <th class="px-6 py-4 text-left text-xs font-semibold text-gray-300 uppercase tracking-wider">Vai trò</th>
            <th class="px-6 py-4 text-left text-xs font-semibold text-gray-300 uppercase tracking-wider">SĐT</th>
            <th class="px-6 py-4 text-right text-xs font-semibold text-gray-300 uppercase tracking-wider">Hành động</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-gray-700/50">
          <tr v-if="pending">
             <td colspan="6" class="px-6 py-4 text-center text-gray-400">Đang tải...</td>
          </tr>
          <tr v-else-if="users && users.length === 0">
             <td colspan="6" class="px-6 py-4 text-center text-gray-400">Không tìm thấy người dùng nào.</td>
          </tr>
          <tr v-for="user in users" :key="user.id" class="hover:bg-gray-700/30 transition-colors">
            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                #{{ user.id }}
            </td>
            <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-white">{{ user.email }}</td>
            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-300">{{ user.name || '---' }}</td>
             <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-300">
               <div v-if="user.roles && user.roles.length > 0" class="flex flex-wrap gap-1">
                   <span v-for="role in user.roles" :key="role.id" class="px-2 py-1 bg-blue-500/10 text-blue-400 rounded-full text-xs font-semibold border border-blue-500/20">
                       {{ role.name || role.code }}
                   </span>
               </div>
               <div v-else>
                   <span v-if="user.role === 'admin'" class="px-2 py-1 bg-yellow-500/10 text-yellow-400 rounded-full text-xs font-semibold">Admin</span>
                   <span v-else class="px-2 py-1 bg-gray-700 text-gray-400 rounded-full text-xs font-semibold capitalize">{{ user.role || 'User' }}</span>
               </div>
             </td>
            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-400">{{ user.phone || '---' }}</td>
            <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
              <button 
                v-if="$can('users.edit')" 
                @click="openEditModal(user)" 
                class="text-blue-400 hover:text-blue-300 mr-4 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
              >
                Sửa
              </button>
              <button 
                v-if="$can('users.delete')"
                @click="deleteUser(user.id)" 
                class="text-red-400 hover:text-red-300 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
              >
                Xóa
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    
     <!-- Pagination -->
    <div class="flex justify-between items-center mt-4 text-gray-400 text-sm">
      <span>Trang {{ page }}</span>
      <div class="flex gap-2">
        <button @click="page--" :disabled="page <= 1" class="px-3 py-1 border border-gray-700 rounded hover:bg-gray-800 disabled:opacity-50 disabled:cursor-not-allowed">Previous</button>
        <button @click="page++" :disabled="!users || users.length < limit" class="px-3 py-1 border border-gray-700 rounded hover:bg-gray-800 disabled:opacity-50 disabled:cursor-not-allowed">Next</button>
      </div>
    </div>

    <!-- Modal Form (Simple implementation) -->
    <div v-if="showModal" class="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
        <div class="bg-gray-800 p-6 rounded-lg w-full max-w-md shadow-lg border border-gray-700">
            <h2 class="text-xl font-bold text-white mb-4">{{ isEditing ? 'Cập nhật người dùng' : 'Thêm người dùng mới' }}</h2>
            <form @submit.prevent="submitForm">
                <div class="mb-4">
                    <label class="block text-gray-300 mb-1 text-sm">Email</label>
                    <input v-model="form.email" type="email" required class="w-full bg-gray-700 border border-gray-600 rounded px-3 py-2 text-white focus:ring-2 focus:ring-primary outline-none">
                </div>
                 <div class="mb-4">
                    <label class="block text-gray-300 mb-1 text-sm">Password</label>
                    <input v-model="form.password" :required="!isEditing" type="password" placeholder="Để trống nếu không đổi" class="w-full bg-gray-700 border border-gray-600 rounded px-3 py-2 text-white focus:ring-2 focus:ring-primary outline-none">
                </div>
                <div class="mb-4">
                    <label class="block text-gray-300 mb-1 text-sm">Tên</label>
                    <input v-model="form.name" type="text" class="w-full bg-gray-700 border border-gray-600 rounded px-3 py-2 text-white focus:ring-2 focus:ring-primary outline-none">
                </div>
                <div class="mb-4">
                    <label class="block text-gray-300 mb-1 text-sm">Số điện thoại</label>
                    <input v-model="form.phone" type="text" class="w-full bg-gray-700 border border-gray-600 rounded px-3 py-2 text-white focus:ring-2 focus:ring-primary outline-none">
                </div>
                <div class="mb-4">
                    <label class="block text-gray-300 mb-1 text-sm">Vai trò</label>
                     <select v-model="form.role" class="w-full bg-gray-700 border border-gray-600 rounded px-3 py-2 text-white focus:ring-2 focus:ring-primary outline-none">
                        <option v-for="role in rolesList" :key="role.id" :value="role.code">
                            {{ role.name || role.code }}
                        </option>
                    </select>
                </div>
                <div class="flex justify-end gap-2 mt-6">
                    <button type="button" @click="showModal = false" class="px-4 py-2 text-gray-300 hover:bg-gray-700 rounded transition-colors">Hủy</button>
                    <button type="submit" class="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded transition-colors">Lưu</button>
                </div>
            </form>
        </div>
    </div>

  </div>
</template>

<script setup>
import { ref, watch } from 'vue'

definePageMeta({
  layout: 'admin',
  permissions: ['users.view']
})
useHead({
  title: 'Quản lý người dùng - Admin'
})

const config = useRuntimeConfig()
const page = ref(1)
const limit = ref(10)
const filterSearch = ref('')
const tempSearch = ref('')
const roleFilter = ref('')
const tempRoleFilter = ref('')

const { token } = useAuth()
const { $can } = useNuxtApp() // Access plugin helper in script if needed, but template access is automatic

// Fetch Data
const { data: users, pending, refresh } = await useFetch('/api/admin/users', {
  query: {
    page: page,
    limit: limit,
    search: filterSearch,
    role: roleFilter
  },
  headers: {
    Authorization: `Bearer ${token.value}`
  },
  watch: [page] // auto refresh on page change, others are in query so might auto-watch too? Nuxt 3 useFetch watches refs in options.
})

// Fetch roles for dropdowns
const { data: rolesData } = await useFetch('/api/admin/roles', {
    headers: { Authorization: `Bearer ${token.value}` }
})
const rolesList = computed(() => rolesData.value || [])

// Manual search trigger
const handleSearch = () => {
    filterSearch.value = tempSearch.value
    roleFilter.value = tempRoleFilter.value
    page.value = 1
    // Removed explicit refresh() to avoid double call. 
    // Changing filterSearch/roleFilter trigger reactivity in useFetch.
    // If values are same, no refresh occurs. To force refresh, we can call refresh() but only if values didn't change?
    // For now, let's assume user changes criteria -> search.
}

// const refreshData = () => refresh() // Removed immediate refresh on role change

// --- Modal & Form ---
const showModal = ref(false)
const isEditing = ref(false)
const form = ref({
    id: null,
    email: '',
    password: '',
    name: '',
    phone: '',
    role: 'user'
})

const openCreateModal = () => {
    isEditing.value = false
    form.value = {
        id: null,
        email: '',
        password: '',
        name: '',
        phone: '',
        role: 'user'
    }
    showModal.value = true
}

const openEditModal = (user) => {
    isEditing.value = true
    form.value = { ...user, password: '' } // Clear password field
    showModal.value = true
}

const { success, error } = useToast()
const { confirmDelete } = useConfirm()

const submitForm = async () => {
    try {
        const headers = { Authorization: `Bearer ${token.value}` }
        
        // Basic validation
        if (!form.value.email || !form.value.name) {
             error("Vui lòng điền đầy đủ email và tên.")
             return
        }

        if (isEditing.value) {
            await $fetch(`/api/admin/users/${form.value.id}`, {
                method: 'PUT',
                body: form.value,
                headers
            })
            success("Cập nhật người dùng thành công!")
        } else {
             if (!form.value.password) {
                 error("Vui lòng nhập mật khẩu cho người dùng mới.")
                 return
             }
            await $fetch('/api/admin/users', {
                method: 'POST',
                body: form.value,
                headers
            })
            success("Thêm người dùng mới thành công!")
        }
        showModal.value = false
        refresh()
    } catch (e) {
        error("Lỗi: " + (e.data?.detail || e.message))
    }
}

const deleteUser = async (id) => {
    if(!await confirmDelete("người dùng này")) return
    try {
        await $fetch(`/api/admin/users/${id}`, {
            method: 'DELETE',
            headers: { Authorization: `Bearer ${token.value}` }
        })
        refresh()
        success("Đã xóa người dùng thành công")
    } catch (e) {
         error("Lỗi xóa người dùng: " + (e.data?.detail || e.message))
    }
}

</script>
