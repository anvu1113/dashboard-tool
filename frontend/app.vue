<template>
  <div>
    <Notivue v-slot="item">
      <Notification :item="item" />
    </Notivue>
    <NuxtLayout>
      <NuxtPage />
    </NuxtLayout>
  </div>
</template>

<script setup>
import { Notivue, Notification } from 'notivue'
</script>




