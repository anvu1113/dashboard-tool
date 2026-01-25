<template>
  <div v-if="order">
    <div class="flex justify-between items-center mb-6">
      <div class="flex items-center gap-3">
        <h1 class="text-3xl font-bold bg-gradient-to-r from-white to-gray-200 bg-clip-text text-transparent">Chi tiết đơn hàng #{{ order.id }}</h1>
        <span :class="order.order_type === 'proxy' ? 'bg-orange-100 text-orange-800' : 'bg-blue-100 text-blue-800'" class="px-3 py-1 text-sm font-semibold rounded-full">
            {{ order.order_type === 'proxy' ? 'Order Hộ' : 'Mua Trực Tiếp' }}
        </span>
      </div>
      <button @click="router.back()" class="inline-flex items-center gap-2 text-blue-400 hover:text-blue-300 font-medium transition-colors">
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
        </svg>
        Quay lại
      </button>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
       <!-- Main Info -->
       <div class="lg:col-span-2 space-y-6">
           <div class="bg-gray-800/50 backdrop-blur-xl rounded-lg shadow-xl border border-gray-700/50 p-6">
               <h3 class="text-lg font-bold mb-4 border-b pb-2">Sản phẩm</h3>
               <div v-for="item in order.items" :key="item.id" class="flex gap-4 mb-4 pb-4 border-b last:border-0 last:pb-0">
                    <img v-if="item.product_image" :src="item.product_image.startsWith('http') ? item.product_image : `${config.public.apiBase}/storage/${item.product_image}`" class="w-20 h-20 object-cover rounded bg-gray-100" />
                    <div v-else class="w-20 h-20 bg-gray-100 rounded flex items-center justify-center text-xs">No Img</div>
                    
                    <div class="flex-1">
                        <div v-if="item.product_link">
                             <a :href="item.product_link" target="_blank" class="text-blue-600 hover:underline break-all">{{ item.product_link }}</a>
                        </div>
                        <div class="text-sm mt-1">
                            <p>SL: {{ item.quantity }} | {{ item.variant }}</p>
                            <p class="text-gray-500 italic">{{ item.note }}</p>
                        </div>
                    </div>
               </div>
           </div>
           
           <div class="bg-gray-800/50 backdrop-blur-xl rounded-lg shadow-xl border border-gray-700/50 p-6">
               <h3 class="text-lg font-bold mb-4 border-b pb-2">Ghi chú & Phản hồi</h3>
               <div class="mb-4">
                   <label class="block text-sm font-semibold text-gray-200 mb-2">Ghi chú của khách</label>
                   <div class="p-3 bg-gray-50 rounded mt-1">{{ order.customer_note || 'Không có' }}</div>
               </div>
               <div>
                   <label class="block text-sm font-semibold text-gray-200 mb-2">Ghi chú nội bộ / Admin</label>
                   <textarea v-model="form.admin_note" class="w-full mt-1 border-gray-600 rounded-md shadow-sm" rows="3"></textarea>
               </div>
           </div>
       </div>

       <!-- Sidebar Actions -->
       <div class="space-y-6">
           <div class="bg-gray-800/50 backdrop-blur-xl rounded-lg shadow-xl border border-gray-700/50 p-6">
               <h3 class="text-lg font-bold mb-4 border-b pb-2">Trạng thái & Giá</h3>
               
               <div class="space-y-4">
                   <div>
                       <label class="block text-sm font-semibold text-gray-200 mb-2">Trạng thái</label>
                       <select v-model="form.status" class="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-600 focus:outline-none focus:ring-primary focus:border-primary sm:text-sm rounded-md">
                           <option value="NEW">Mới</option>
                           <option value="QUOTED">Đã báo giá</option>
                           <option value="CONFIRMED">Đã chốt</option>
                           <option value="ORDERED">Đã đặt hàng</option>
                           <option value="IN_TRANSIT">Đang về</option>
                           <option value="COMPLETED">Hoàn thành</option>
                           <option value="CANCELED">Hủy</option>
                       </select>
                   </div>
                   
                   <div>
                       <label class="block text-sm font-semibold text-gray-200 mb-2">Giá hàng (VNĐ)</label>
                       <input type="number" v-model="form.product_price" class="mt-1 w-full border-gray-600 rounded-md shadow-sm" />
                   </div>
                   <div>
                       <label class="block text-sm font-semibold text-gray-200 mb-2">Phí dịch vụ</label>
                       <input type="number" v-model="form.service_fee" class="mt-1 w-full border-gray-600 rounded-md shadow-sm" />
                   </div>
                   <div>
                       <label class="block text-sm font-semibold text-gray-200 mb-2">Phí Ship</label>
                       <input type="number" v-model="form.shipping_fee" class="mt-1 w-full border-gray-600 rounded-md shadow-sm" />
                   </div>
                    <div class="pt-2 border-t font-bold flex justify-between">
                       <span>Tổng cộng:</span>
                       <span>{{ totalComputed }} VNĐ</span>
                   </div>
                   <div>
                       <label class="block text-sm font-semibold text-gray-200 mb-2">Đã cọc</label>
                       <input type="number" v-model="form.deposit_amount" class="mt-1 w-full border-gray-600 rounded-md shadow-sm" />
                   </div>

                   <button @click="saveOrder" :disabled="saving" class="w-full bg-primary text-white py-2 px-4 rounded hover:bg-primary-dark transition-colors disabled:opacity-50">
                       {{ saving ? 'Đang lưu...' : 'Cập nhật' }}
                   </button>
               </div>
           </div>

           <div class="bg-gray-800/50 backdrop-blur-xl rounded-lg shadow-xl border border-gray-700/50 p-6">
               <h3 class="text-lg font-bold mb-4 border-b pb-2">Khách hàng</h3>
               <p><span class="font-medium">Tên:</span> {{ order.contact_name }}</p>
               <p><span class="font-medium">SĐT:</span> {{ order.contact_phone }}</p>
               <p><span class="font-medium">Email:</span> {{ order.contact_email || 'N/A' }}</p>
           </div>
       </div>
    </div>
  </div>
</template>

<script setup>
definePageMeta({
  layout: 'admin',
  middleware: 'auth'
})

const route = useRoute()
const router = useRouter()
const config = useRuntimeConfig()
const { token } = useAuth()

const order = ref(null)
const saving = ref(false)

const form = ref({
    status: 'NEW',
    product_price: 0,
    service_fee: 0,
    shipping_fee: 0,
    deposit_amount: 0,
    admin_note: ''
})

const totalComputed = computed(() => {
    return Number(form.value.product_price || 0) + Number(form.value.service_fee || 0) + Number(form.value.shipping_fee || 0)
})

const loadOrder = async () => {
    try {
        const response = await $fetch(`${config.public.apiBase}/api/admin/orders/${route.params.id}`, {
            headers: { Authorization: `Bearer ${token.value}` }
        })
        order.value = response
        
        // Init form
        form.value.status = response.status
        form.value.product_price = Number(response.product_price)
        form.value.service_fee = Number(response.service_fee)
        form.value.shipping_fee = Number(response.shipping_fee)
        form.value.deposit_amount = Number(response.deposit_amount)
        form.value.admin_note = response.admin_note
    } catch (e) {
        console.error(e)
    }
}

const saveOrder = async () => {
    saving.value = true
    try {
        await $fetch(`${config.public.apiBase}/api/admin/orders/${route.params.id}`, {
            method: 'PUT',
            body: form.value,
            headers: { Authorization: `Bearer ${token.value}` }
        })
        await loadOrder()
        alert('Cập nhật thành công')
    } catch (e) {
        alert('Lỗi cập nhật')
        console.error(e)
    } finally {
        saving.value = false
    }
}

onMounted(loadOrder)
</script>
