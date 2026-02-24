<template>
  <div>
    <!-- Header -->
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold bg-gradient-to-r from-white to-gray-200 bg-clip-text text-transparent">
        Quản lý Vai trò & Quyền hạn
      </h1>
      <div class="flex gap-2">
         <button 
          v-if="$can('roles.manage')"
          @click="openPermissionModal" 
          class="bg-gray-700 text-white px-4 py-2 rounded-lg hover:bg-gray-600 transition-all duration-200 font-medium flex items-center gap-2"
        >
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
          </svg>
          Thêm Quyền
        </button>
        <button 
          v-if="$can('roles.manage')"
          @click="openCreateModal" 
          class="bg-gradient-to-r from-blue-500 to-blue-600 text-white px-6 py-2 rounded-lg hover:shadow-lg hover:shadow-blue-500/50 transition-all duration-200 font-medium flex items-center gap-2"
        >
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
          </svg>
          Thêm Vai trò
        </button>
      </div>
    </div>

    <!-- Roles Grid -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-8">
       <div v-if="pending" class="col-span-full text-center text-gray-400 py-10">Đang tải...</div>
       <div v-else-if="roles && roles.length === 0" class="col-span-full text-center text-gray-400 py-10">Chưa có vai trò nào.</div>
       
       <div v-for="role in roles" :key="role.id" class="bg-card-dark rounded-xl border border-gray-700 shadow-lg p-6 relative group hover:border-blue-500 transition-colors">
          <div class="flex justify-between items-start mb-4">
             <div>
                <h3 class="text-xl font-bold text-white">{{ role.name }}</h3>
                <p class="text-sm text-gray-400 mt-1 font-mono bg-gray-800 px-2 py-0.5 rounded inline-block">{{ role.code }}</p>
             </div>
             <div class="flex gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                <button @click="openEditModal(role)" class="p-1 text-blue-400 hover:text-blue-300 bg-blue-500/10 rounded mb-1">
                   <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" /></svg>
                </button>
                <button @click="deleteRole(role.id)" class="p-1 text-red-400 hover:text-red-300 bg-red-500/10 rounded">
                   <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" /></svg>
                </button>
             </div>
          </div>
          
          <p class="text-gray-400 text-sm mb-4 line-clamp-2 h-10">{{ role.description || 'Không có mô tả' }}</p>
          
          <div class="border-t border-gray-700 pt-4">
             <h4 class="text-xs font-semibold text-gray-500 uppercase tracking-wider mb-2">Quyền hạn ({{ role.permissions ? role.permissions.length : 0 }})</h4>
             <div class="flex flex-wrap gap-2 max-h-32 overflow-y-auto">
                <span v-for="perm in role.permissions" :key="perm.id" class="px-2 py-1 bg-gray-800 text-gray-300 rounded text-xs border border-gray-700">
                   {{ perm.code }}
                </span>
                <span v-if="!role.permissions || role.permissions.length === 0" class="text-xs text-gray-500 italic">Chưa có quyền hạn nào được gán</span>
             </div>
          </div>
       </div>
    </div>

    <!-- Permissions List (Grouped) -->
    <div class="bg-card-dark rounded-lg shadow-xl border border-gray-700/50 overflow-hidden mb-8">
      <div class="px-6 py-4 border-b border-gray-700 flex justify-between items-center cursor-pointer" @click="showPermissionsList = !showPermissionsList">
        <h3 class="text-lg font-bold text-white">Danh sách tất cả Quyền hạn</h3>
        <svg :class="{'rotate-180': showPermissionsList}" class="w-5 h-5 text-gray-400 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" /></svg>
      </div>
      <div v-show="showPermissionsList" class="p-6">
          <div v-for="(perms, group) in groupedPermissions" :key="group" class="mb-6 last:mb-0">
             <h4 class="text-md font-bold text-gray-400 capitalize mb-3 border-b border-gray-700 pb-1">{{ group }}</h4>
             <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
                 <div v-for="perm in perms" :key="perm.id" class="flex flex-col p-3 bg-gray-800 rounded border border-gray-700 hover:border-gray-500 transition-colors group relative">
                    <div class="flex items-center gap-2 mb-1">
                        <div class="w-2 h-2 rounded-full bg-green-500"></div>
                        <div class="text-sm font-medium text-white truncate" :title="perm.code">{{ perm.code }}</div>
                    </div>
                    <div class="text-xs text-gray-500 line-clamp-2 h-8">{{ perm.description }}</div>
                    
                    <!-- Actions -->
                    <div class="absolute top-2 right-2 flex gap-1 opacity-0 group-hover:opacity-100 transition-opacity">
                        <button @click.stop="openEditPermissionModal(perm)" class="p-1 text-blue-400 hover:bg-blue-900/50 rounded" title="Sửa">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z" /></svg>
                        </button>
                        <button @click.stop="deletePermission(perm.id)" class="p-1 text-red-400 hover:bg-red-900/50 rounded" title="Xóa">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" /></svg>
                        </button>
                    </div>
                 </div>
             </div>
          </div>
      </div>
    </div>

    <!-- Role Modal -->
    <div v-if="showRoleModal" class="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4">
        <div class="bg-gray-800 rounded-lg w-full max-w-2xl shadow-lg border border-gray-700 max-h-[90vh] flex flex-col">
            <div class="p-6 border-b border-gray-700">
               <h2 class="text-xl font-bold text-white">{{ isEditing ? 'Cập nhật Vai trò' : 'Thêm Vai trò mới' }}</h2>
            </div>
            
            <div class="p-6 overflow-y-auto flex-1">
                <div class="grid grid-cols-2 gap-4 mb-4">
                    <div>
                        <label class="block text-gray-300 mb-1 text-sm">Mã Vai trò (Code)</label>
                        <input v-model="roleForm.code" :disabled="isEditing" type="text" placeholder="e.g. sale_manager" class="w-full bg-gray-700 border border-gray-600 rounded px-3 py-2 text-white focus:ring-2 focus:ring-primary outline-none disabled:opacity-50">
                    </div>
                    <div>
                        <label class="block text-gray-300 mb-1 text-sm">Tên hiển thị</label>
                        <input v-model="roleForm.name" type="text" placeholder="e.g. Sale Manager" class="w-full bg-gray-700 border border-gray-600 rounded px-3 py-2 text-white focus:ring-2 focus:ring-primary outline-none">
                    </div>
                </div>
                <div class="mb-6">
                    <label class="block text-gray-300 mb-1 text-sm">Mô tả</label>
                    <textarea v-model="roleForm.description" rows="2" class="w-full bg-gray-700 border border-gray-600 rounded px-3 py-2 text-white focus:ring-2 focus:ring-primary outline-none"></textarea>
                </div>

                <!-- Permission Selection -->
                <div class="border-t border-gray-700 pt-4">
                    <div class="flex justify-between items-center mb-3">
                       <label class="block text-gray-300 font-bold">Gán Quyền hạn</label>
                       <div class="text-xs text-gray-400">
                          Đã chọn: {{ selectedPermissionIds.length }}
                       </div>
                    </div>
                    
                    <div class="space-y-6 max-h-[60vh] overflow-y-auto pr-2">
                       <div v-for="(perms, group) in groupedPermissions" :key="group" class="bg-gray-700/30 rounded-lg p-4 border border-gray-700">
                          <div class="flex items-center justify-between mb-3 pb-2 border-b border-gray-600">
                             <div class="flex items-center gap-2">
                                <input 
                                  type="checkbox" 
                                  :checked="isGroupSelected(perms)"
                                  @change="toggleGroup(perms)"
                                  class="w-5 h-5 text-blue-600 rounded bg-gray-700 border-gray-600 focus:ring-blue-500 cursor-pointer"
                                >
                                <h3 class="font-bold text-white capitalize">{{ group }}</h3>
                             </div>
                             <span class="text-xs text-gray-400">{{ perms.filter(p => selectedPermissionIds.includes(p.id)).length }}/{{ perms.length }}</span>
                          </div>
                          
                          <div class="grid grid-cols-1 md:grid-cols-2 gap-2">
                             <label v-for="perm in perms" :key="perm.id" class="flex items-center gap-3 p-2 rounded hover:bg-gray-700 cursor-pointer border border-transparent hover:border-gray-600 transition-colors" :class="{'bg-blue-600/10 border-blue-600/30': selectedPermissionIds.includes(perm.id)}">
                                <input type="checkbox" :value="perm.id" v-model="selectedPermissionIds" class="w-4 h-4 text-blue-600 rounded bg-gray-700 border-gray-600 focus:ring-blue-500">
                                <div>
                                   <div class="text-sm font-medium text-gray-200">{{ perm.code }}</div>
                                   <div class="text-xs text-gray-500">{{ perm.description }}</div>
                                </div>
                             </label>
                          </div>
                       </div>
                    </div>
                </div>
            </div>

            <div class="p-6 border-t border-gray-700 flex justify-end gap-2 bg-gray-800 rounded-b-lg">
                <button type="button" @click="showRoleModal = false" class="px-4 py-2 text-gray-300 hover:bg-gray-700 rounded transition-colors">Hủy</button>
                <button type="button" @click="submitRoleForm" class="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded transition-colors">Lưu</button>
            </div>
        </div>
    </div>

    <!-- Create Permission Modal -->
    <div v-if="showPermModal" class="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4">
        <div class="bg-gray-800 p-6 rounded-lg w-full max-w-md shadow-lg border border-gray-700">
            <h2 class="text-xl font-bold text-white mb-4">{{ isPermEditing ? 'Cập nhật Quyền hạn' : 'Thêm Quyền hạn mới' }}</h2>
            <div class="mb-4">
                <label class="block text-gray-300 mb-1 text-sm">Mã Quyền (Code)</label>
                <input v-model="permForm.code" type="text" placeholder="e.g. reports.view" class="w-full bg-gray-700 border border-gray-600 rounded px-3 py-2 text-white focus:ring-2 focus:ring-primary outline-none">
                <p class="text-xs text-gray-500 mt-1">Nên đặt theo format: resource.action</p>
            </div>
            <div class="mb-4">
                <label class="block text-gray-300 mb-1 text-sm">Mô tả</label>
                <input v-model="permForm.description" type="text" class="w-full bg-gray-700 border border-gray-600 rounded px-3 py-2 text-white focus:ring-2 focus:ring-primary outline-none">
            </div>
            <div class="flex justify-end gap-2 mt-6">
                <button type="button" @click="showPermModal = false" class="px-4 py-2 text-gray-300 hover:bg-gray-700 rounded transition-colors">Hủy</button>
                <button type="button" @click="submitPermForm" class="px-4 py-2 bg-green-600 hover:bg-green-700 text-white rounded transition-colors">{{ isPermEditing ? 'Cập nhật' : 'Tạo mới' }}</button>
            </div>
        </div>
    </div>

  </div>
</template>

<script setup>
definePageMeta({
  layout: 'admin',
  permissions: ['roles.manage']
})
useHead({
  title: 'Quản lý Vai trò - Admin'
})

const { token } = useAuth()
const showPermissionsList = ref(false)

// Data Fetching
const { data: roles, pending, refresh: refreshRoles } = await useFetch('/api/admin/roles', {
   headers: { Authorization: `Bearer ${token.value}` }
})

const { data: permissions, refresh: refreshPerms } = await useFetch('/api/admin/permissions', {
   headers: { Authorization: `Bearer ${token.value}` }
})

// --- Role Modal ---
const showRoleModal = ref(false)
const isEditing = ref(false)
const roleForm = ref({ id: null, code: '', name: '', description: '' })
const selectedPermissionIds = ref([])

const openCreateModal = () => {
   isEditing.value = false
   roleForm.value = { id: null, code: '', name: '', description: '' }
   selectedPermissionIds.value = []
   showRoleModal.value = true
}

const openEditModal = (role) => {
   isEditing.value = true
   roleForm.value = { ...role }
   // Populate selected permissions
   selectedPermissionIds.value = role.permissions ? role.permissions.map(p => p.id) : []
   showRoleModal.value = true
}

const groupedPermissions = computed(() => {
   const groups = {}
   if (!permissions.value) return groups
   
   permissions.value.forEach(p => {
      // Split by dot to get group name (e.g. users.view -> users)
      const parts = p.code.split('.')
      const group = parts.length > 1 ? parts[0] : 'other'
      
      if (!groups[group]) groups[group] = []
      groups[group].push(p)
   })
   return groups
})

const isGroupSelected = (perms) => {
    if (!perms || perms.length === 0) return false
    return perms.every(p => selectedPermissionIds.value.includes(p.id))
}

const toggleGroup = (perms) => {
    if (isGroupSelected(perms)) {
        // Deselect all in group
        const idsToRemove = perms.map(p => p.id)
        selectedPermissionIds.value = selectedPermissionIds.value.filter(id => !idsToRemove.includes(id))
    } else {
        // Select all in group
        const idsToAdd = perms.map(p => p.id).filter(id => !selectedPermissionIds.value.includes(id))
        selectedPermissionIds.value = [...selectedPermissionIds.value, ...idsToAdd]
    }
}



const { success, error } = useToast()

const submitRoleForm = async () => {
    // console.log("Submit clicked", roleForm.value)
    if (!token.value) {
        error("Lỗi: Không tìm thấy token xác thực. Vui lòng đăng nhập lại.")
        return
    }
    
    try {
        const headers = { Authorization: `Bearer ${token.value}` }
        let savedRole;
        
        if (isEditing.value) {
            console.log("Updating role...", roleForm.value.id);
            savedRole = await $fetch(`/api/admin/roles/${roleForm.value.id}`, {
                method: 'PUT',
                body: roleForm.value,
                headers
            })
        } else {
            console.log("Creating role...");
            savedRole = await $fetch('/api/admin/roles', {
                method: 'POST',
                body: roleForm.value,
                headers
            })
        }
        
        console.log("Saved Role response:", savedRole);

        // Update Permissions
        if (savedRole && savedRole.id) {
           console.log("Updating permissions for role", savedRole.id, "with IDs:", selectedPermissionIds.value);
           if (selectedPermissionIds.value.length === 0) {
                console.warn("Warning: No permissions selected!");
           }
           
           const permResponse = await $fetch(`/api/admin/roles/${savedRole.id}/permissions`, {
               method: 'POST',
               body: selectedPermissionIds.value, 
               headers
           })
           console.log("Permission update response:", permResponse);
        } else {
            console.error("Error: Could not get Role ID from savedRole response");
            error("Không thể lấy ID vai trò để cập nhật quyền!");
            return;
        }

        showRoleModal.value = false
        refreshRoles()
        success(isEditing.value ? "Cập nhật vai trò thành công!" : "Tạo vai trò mới thành công!")
    } catch (e) {
        console.error("Submit Error:", e)
        error("Lỗi: " + (e.data?.detail || e.message))
    }
}

const { confirmDelete } = useConfirm()

const deleteRole = async (id) => {
    if(!await confirmDelete("vai trò này")) return
    try {
        await $fetch(`/api/admin/roles/${id}`, {
            method: 'DELETE',
            headers: { Authorization: `Bearer ${token.value}` }
        })
        refreshRoles()
        success("Đã xóa vai trò thành công")
    } catch (e) {
         error("Lỗi xóa vai trò: " + (e.data?.detail || e.message))
    }
}

// --- Permission Modal ---
const showPermModal = ref(false)
const isPermEditing = ref(false)
const permForm = ref({ id: null, code: '', description: '' })

const openPermissionModal = () => {
    isPermEditing.value = false
    permForm.value = { id: null, code: '', description: '' }
    showPermModal.value = true
}

const openEditPermissionModal = (perm) => {
    isPermEditing.value = true
    permForm.value = { ...perm }
    showPermModal.value = true
}

const submitPermForm = async () => {
    try {
        if (isPermEditing.value) {
            await $fetch(`/api/admin/permissions/${permForm.value.id}`, {
                method: 'PUT',
                body: permForm.value,
                headers: { Authorization: `Bearer ${token.value}` }
            })
            success("Cập nhật quyền thành công!")
        } else {
            await $fetch('/api/admin/permissions', {
                method: 'POST',
                body: permForm.value,
                headers: { Authorization: `Bearer ${token.value}` }
            })
            success("Đã tạo quyền mới thành công!")
        }
        showPermModal.value = false
        refreshPerms()
    } catch (e) {
        error("Lỗi: " + (e.data?.detail || e.message))
    }
}

const deletePermission = async (id) => {
    const { confirm } = useConfirm()
    if(!await confirm("Cảnh báo: Xóa quyền này sẽ xóa nó khỏi tất cả các vai trò đang sử dụng. Bạn có chắc chắn?", "Xóa Quyền hạn")) return
    
    try {
        await $fetch(`/api/admin/permissions/${id}`, {
            method: 'DELETE',
            headers: { Authorization: `Bearer ${token.value}` }
        })
        refreshPerms()
        success("Đã xóa quyền thành công!")
    } catch (e) {
        error("Lỗi: " + (e.data?.detail || e.message))
    }
}

</script>
