<template>
  <footer class="bg-white border-t border-gray-light mt-auto">
    <div class="container mx-auto px-4 py-8">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
        <!-- Thông tin hệ thống -->
        <div>
          <h3 class="font-semibold text-primary mb-4">Dashboard Tool</h3>
          <p class="text-gray-dark text-sm mb-2">Quản lý hệ thống hiệu quả.</p>
        </div>

        <!-- Liên hệ -->
        <div>
          <h3 class="font-semibold text-primary mb-4">Liên hệ</h3>
          <div class="space-y-3 text-sm">
             <p class="text-gray-dark">admin@example.com</p>
          </div>
        </div>
      </div>

      <div class="mt-8 pt-8 border-t border-gray-light text-center text-sm text-gray-dark">
        <p>&copy; {{ new Date().getFullYear() }} Dashboard Tool. All rights reserved.</p>
      </div>
    </div>
  </footer>
</template>

<script setup>
</script>
