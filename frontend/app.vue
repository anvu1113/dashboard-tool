<template>
  <div>
    <Notivue v-slot="item">
      <Notification :item="item" />
    </Notivue>
    <GlobalModal />
    <NuxtLayout>
      <NuxtPage />
    </NuxtLayout>
  </div>
</template>

<script setup>
import { Notivue, Notification } from 'notivue'

useHead({
  titleTemplate: (titleChunk) => {
    return titleChunk ? `${titleChunk} - ExtensionHub` : 'ExtensionHub - Công cụ Order Taobao/1688'
  },
  meta: [
    { charset: 'utf-8' },
    { name: 'viewport', content: 'width=device-width, initial-scale=1' },
    { name: 'description', content: 'ExtensionHub - Giải pháp toàn diện cho dân order Taobao, 1688. Dịch thuật, tính giá, phân tích shop tự động.' }
  ],
  link: [
    { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
  ]
})
</script>




