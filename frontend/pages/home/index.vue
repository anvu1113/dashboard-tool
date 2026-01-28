<template>
  <div class="bg-bg-dark">
    <!-- Hero Section -->
    <section class="relative pt-20 pb-24 lg:pt-32 overflow-hidden">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 text-center">
        <h1 class="text-4xl md:text-6xl font-extrabold text-white tracking-tight mb-8 leading-tight">
          Extension hỗ trợ order hàng <br>
          <span class="bg-gradient-to-r from-blue-400 to-blue-600 bg-clip-text text-transparent">Taobao / 1688</span> nhanh & chính xác
        </h1>
        <p class="mt-4 max-w-2xl mx-auto text-xl text-gray-400 mb-10">
          Công cụ tối ưu dành cho dân order, giúp bạn xóa bỏ rào cản ngôn ngữ, tính toán giá vốn chính xác và đặt hàng hiệu quả hơn bao giờ hết.
        </p>
        <div class="flex justify-center gap-4">
          <a href="#" class="px-8 py-4 bg-primary hover:bg-primary-hover text-white rounded-lg font-bold text-lg transition-all shadow-lg hover:shadow-blue-500/50 flex items-center gap-2">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
            </svg>
            Cài Extension Ngay
          </a>
          <NuxtLink to="/features" class="px-8 py-4 bg-gray-800 hover:bg-gray-700 text-white border border-gray-700 rounded-lg font-bold text-lg transition-all">
            Xem chi tiết
          </NuxtLink>
        </div>
        
        <!-- Mockup/Screenshot placeholder -->
        <div class="mt-16 relative mx-auto max-w-5xl rounded-xl bg-gray-800/50 border border-gray-700 shadow-2xl overflow-hidden aspect-video flex items-center justify-center">
          <span class="text-gray-500 text-lg">Chrome Extension Interface Screenshot</span>
           <!-- In reality, this would be an <img> tag -->
        </div>
      </div>
       
      <!-- Background Glow -->
      <div class="absolute top-0 left-1/2 -translate-x-1/2 w-full h-full max-w-7xl pointer-events-none opacity-20">
         <div class="absolute top-20 left-1/4 w-96 h-96 bg-blue-500 rounded-full blur-3xl"></div>
         <div class="absolute bottom-20 right-1/4 w-96 h-96 bg-purple-500 rounded-full blur-3xl"></div>
      </div>
    </section>

    <!-- Pain Points Section -->
    <section class="py-20 bg-card-dark border-t border-b border-border-dark">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="text-3xl font-bold text-white mb-4">Tại sao bạn cần công cụ này?</h2>
          <p class="text-gray-400">Những vấn đề muôn thuở của dân order hàng Trung</p>
        </div>
        
        <div class="grid md:grid-cols-3 gap-8">
          <div class="bg-bg-dark p-8 rounded-xl border border-gray-800 hover:border-blue-500/50 transition-colors group">
            <div class="w-12 h-12 bg-red-500/10 rounded-lg flex items-center justify-center mb-6 text-red-400 group-hover:text-red-300">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5h12M9 3v2m1.048 9.5A18.022 18.022 0 016.412 9m6.088 9h7M11 21l5-10 5 10M12.751 5C11.783 10.77 8.07 15.61 3 18.129" />
              </svg>
            </div>
            <h3 class="text-xl font-bold text-white mb-3">Google Dịch không sát nghĩa</h3>
            <p class="text-gray-400">Dịch tự động thường sai lệch về màu sắc, chất liệu, kích thước khiến việc tư vấn cho khách gặp rủi ro.</p>
          </div>

          <div class="bg-bg-dark p-8 rounded-xl border border-gray-800 hover:border-blue-500/50 transition-colors group">
            <div class="w-12 h-12 bg-yellow-500/10 rounded-lg flex items-center justify-center mb-6 text-yellow-400 group-hover:text-yellow-300">
               <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
            </div>
            <h3 class="text-xl font-bold text-white mb-3">Tính giá thủ công lâu</h3>
            <p class="text-gray-400">Mất thời gian quy đổi tỷ giá, cộng phí vận chuyển, phí dịch vụ để ra báo giá cuối cùng.</p>
          </div>

          <div class="bg-bg-dark p-8 rounded-xl border border-gray-800 hover:border-blue-500/50 transition-colors group">
             <div class="w-12 h-12 bg-purple-500/10 rounded-lg flex items-center justify-center mb-6 text-purple-400 group-hover:text-purple-300">
               <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z" />
              </svg>
            </div>
            <h3 class="text-xl font-bold text-white mb-3">Đọc review khó khăn</h3>
            <p class="text-gray-400">Khó lọc được review thật/giả và xem ảnh thực tế từ người mua trước đó.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Solutions / Features Preview -->
    <section class="py-20">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid md:grid-cols-2 gap-16 items-center">
          <div>
            <h2 class="text-3xl font-bold text-white mb-6">Giải pháp toàn diện</h2>
            <div class="space-y-8">
              <div class="flex gap-4">
                <div class="w-8 h-8 rounded-full bg-blue-500/20 flex items-center justify-center text-blue-400 flex-shrink-0">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                  </svg>
                </div>
                <div>
                  <h4 class="text-lg font-bold text-white">Dịch thuật ngữ chuyên ngành</h4>
                  <p class="text-gray-400">Chỉ cần bôi đen text, extension tự động dịch sát nghĩa chuyên ngành order.</p>
                </div>
              </div>
              
              <div class="flex gap-4">
                <div class="w-8 h-8 rounded-full bg-blue-500/20 flex items-center justify-center text-blue-400 flex-shrink-0">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                  </svg>
                </div>
                <div>
                  <h4 class="text-lg font-bold text-white">Tự động quy đổi giá</h4>
                  <p class="text-gray-400">Tự động convert giá CNY sang VND theo tỷ giá real-time hoặc cài đặt.</p>
                </div>
              </div>

               <div class="flex gap-4">
                <div class="w-8 h-8 rounded-full bg-blue-500/20 flex items-center justify-center text-blue-400 flex-shrink-0">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                  </svg>
                </div>
                <div>
                  <h4 class="text-lg font-bold text-white">Phân tích shop uy tín</h4>
                  <p class="text-gray-400">Hiển thị các chỉ số ẩn của shop để đánh giá độ uy tín chính xác.</p>
                </div>
              </div>
            </div>
            
            <div class="mt-8">
               <NuxtLink to="/features" class="text-primary hover:text-primary-hover font-semibold inline-flex items-center gap-1 transition-colors">
                 Xem tất cả tính năng
                 <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3" />
                  </svg>
               </NuxtLink>
            </div>
          </div>
          <div class="bg-card-dark border border-gray-700 rounded-xl p-4 h-96 flex items-center justify-center relative">
              <div class="absolute inset-0 bg-gradient-to-tr from-blue-500/10 to-purple-500/10 rounded-xl"></div>
              <span class="text-gray-500 relative z-10">Feature Visualization</span>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="py-20 bg-gradient-to-br from-gray-900 to-black relative border-t border-gray-800">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h2 class="text-3xl font-bold text-white mb-6">Bắt đầu tối ưu công việc kinh doanh ngay hôm nay</h2>
        <p class="text-xl text-gray-400 mb-10">
          Gia nhập cộng đồng hơn 10.000 người bán hàng đang sử dụng công cụ của chúng tôi.
        </p>
        <a href="#" class="inline-flex justify-center items-center gap-2 px-8 py-4 bg-primary hover:bg-primary-hover text-white rounded-lg font-bold text-lg transition-all shadow-lg hover:shadow-blue-500/50">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
            </svg>
          Cài đặt miễn phí
        </a>
      </div>
    </section>
  </div>
</template>

<script setup>
useHead({
  title: 'ExtensionHub - Công cụ hỗ trợ order Taobao/1688 tốt nhất',
  meta: [
    { name: 'description', content: 'Chrome Extension giúp dịch thuật, tính giá và phân tích shop Taobao/1688 nhanh chóng, chính xác.' }
  ]
})
</script>
