<template>
  <div class="bg-bg-dark py-20 min-h-screen">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="max-w-2xl mx-auto">
        <div class="text-center mb-12">
          <h1 class="text-4xl font-bold text-white mb-4">Liên hệ với chúng tôi</h1>
          <p class="text-xl text-gray-400">Chúng tôi luôn sẵn sàng lắng nghe và hỗ trợ bạn</p>
        </div>

        <div class="bg-card-dark border border-gray-700 rounded-xl p-8 shadow-xl">
          <form class="space-y-6">
            <div class="grid grid-cols-2 gap-6">
              <div>
                <label class="block text-sm font-medium text-gray-300 mb-2">Họ tên</label>
                <input type="text" class="block w-full bg-bg-dark border border-gray-600 text-white rounded-lg py-3 px-4 focus:ring-2 focus:ring-primary focus:border-transparent outline-none" placeholder="Nguyễn Văn A">
              </div>
              <div>
                 <label class="block text-sm font-medium text-gray-300 mb-2">Email</label>
                <input type="email" class="block w-full bg-bg-dark border border-gray-600 text-white rounded-lg py-3 px-4 focus:ring-2 focus:ring-primary focus:border-transparent outline-none" placeholder="email@example.com">
              </div>
            </div>
            
            <div>
              <label class="block text-sm font-medium text-gray-300 mb-2">Chủ đề</label>
              <select class="block w-full bg-bg-dark border border-gray-600 text-white rounded-lg py-3 px-4 focus:ring-2 focus:ring-primary focus:border-transparent outline-none">
                <option>Hỗ trợ kỹ thuật</option>
                <option>Tư vấn gói cước</option>
                <option>hợp tác kinh doanh</option>
                <option>Khác</option>
              </select>
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-300 mb-2">Nội dung</label>
              <textarea rows="4" class="block w-full bg-bg-dark border border-gray-600 text-white rounded-lg py-3 px-4 focus:ring-2 focus:ring-primary focus:border-transparent outline-none" placeholder="Nhập nội dung tin nhắn..."></textarea>
            </div>

            <button type="submit" class="w-full bg-gradient-to-r from-blue-500 to-blue-600 text-white font-bold py-4 rounded-lg hover:shadow-lg hover:shadow-blue-500/50 transition-all">
              Gửi tin nhắn
            </button>
          </form>

          <div class="mt-12 pt-8 border-t border-gray-700 grid grid-cols-2 gap-8">
            <div class="flex items-start gap-4">
              <div class="p-3 bg-blue-500/10 rounded-lg text-blue-400">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" /></svg>
              </div>
              <div>
                <h4 class="text-white font-semibold">Email</h4>
                <p class="text-gray-400 text-sm">support@extensionhub.com</p>
              </div>
            </div>
             <div class="flex items-start gap-4">
              <div class="p-3 bg-blue-500/10 rounded-lg text-blue-400">
                 <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" /></svg>
              </div>
              <div>
                <h4 class="text-white font-semibold">Hotline</h4>
                <p class="text-gray-400 text-sm">1900 1234</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
useHead({
  title: 'Liên hệ - ExtensionHub',
  meta: [
    { name: 'description', content: 'Liên hệ với chúng tôi để được hỗ trợ.' }
  ]
})
</script>
