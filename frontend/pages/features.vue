<template>
  <div class="bg-bg-dark py-20 min-h-screen">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-16">
        <h1 class="text-4xl font-bold text-white mb-4">Tính năng nổi bật</h1>
        <p class="text-xl text-gray-400">Công cụ hỗ trợ đắc lực cho mọi nhu cầu đặt hàng</p>
      </div>

      <div class="space-y-24">
        <!-- Feature 1 -->
        <div class="grid md:grid-cols-2 gap-12 items-center">
          <div class="order-2 md:order-1">
            <h2 class="text-3xl font-bold text-white mb-6">Dịch thuật ngữ chuyên ngành Order</h2>
            <p class="text-gray-400 mb-6 text-lg">
              Không còn lo lắng về rào cản ngôn ngữ. Hệ thống AI của chúng tôi tự động nhận diện và dịch các thuật ngữ chuyên ngành về thời trang, đồ gia dụng, linh kiện điện tử... sát nghĩa nhất.
            </p>
            <ul class="space-y-3">
              <li class="flex items-center gap-3 text-gray-300">
                <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
                Dịch màu sắc, kích thước chính xác
              </li>
              <li class="flex items-center gap-3 text-gray-300">
                <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
                Dịch thông số kỹ thuật
              </li>
              <li class="flex items-center gap-3 text-gray-300">
                 <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
                Hỗ trợ 100+ danh mục ngành hàng
              </li>
            </ul>
          </div>
          <div class="order-1 md:order-2 bg-card-dark border border-gray-700 rounded-xl p-8 h-80 flex items-center justify-center">
             <span class="text-gray-500">Translation Feature Screenshot</span>
          </div>
        </div>

        <!-- Feature 2 -->
        <div class="grid md:grid-cols-2 gap-12 items-center">
          <div class="bg-card-dark border border-gray-700 rounded-xl p-8 h-80 flex items-center justify-center">
             <span class="text-gray-500">Price Calculator Screenshot</span>
          </div>
          <div>
            <h2 class="text-3xl font-bold text-white mb-6">Tính giá vốn tự động</h2>
            <p class="text-gray-400 mb-6 text-lg">
              Biết ngay giá vốn về tay chỉ trong 1 click. Hệ thống tự động lấy tỷ giá mới nhất và áp dụng công thức tính phí của bạn.
            </p>
            <ul class="space-y-3">
              <li class="flex items-center gap-3 text-gray-300">
                <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
                Tỷ giá cập nhật Real-time
              </li>
              <li class="flex items-center gap-3 text-gray-300">
                <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
                Tùy chỉnh công thức tính giá
              </li>
              <li class="flex items-center gap-3 text-gray-300">
                 <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
                Xuất báo giá nhanh ra Excel/Image
              </li>
            </ul>
          </div>
        </div>

        <!-- Feature 3 -->
        <div class="grid md:grid-cols-2 gap-12 items-center">
          <div class="order-2 md:order-1">
            <h2 class="text-3xl font-bold text-white mb-6">Phân tích Shop & Sản phẩm</h2>
            <p class="text-gray-400 mb-6 text-lg">
              Tránh rủi ro nhập phải hàng kém chất lượng với công cụ phân tích độ uy tín của shop và sản phẩm.
            </p>
            <ul class="space-y-3">
              <li class="flex items-center gap-3 text-gray-300">
                <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
                Hiển thị điểm uy tín thực
              </li>
              <li class="flex items-center gap-3 text-gray-300">
                <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
                Cảnh báo shop có tỷ lệ hoàn hàng cao
              </li>
              <li class="flex items-center gap-3 text-gray-300">
                 <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
                Lọc review có ảnh nhanh chóng
              </li>
            </ul>
          </div>
          <div class="order-1 md:order-2 bg-card-dark border border-gray-700 rounded-xl p-8 h-80 flex items-center justify-center">
             <span class="text-gray-500">Shop Analysis Screenshot</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
useHead({
  title: 'Tính năng - ExtensionHub',
  meta: [
    { name: 'description', content: 'Chi tiết các tính năng của ExtensionHub: Dịch thuật, Tính giá, Phân tích Shop.' }
  ]
})
</script>
