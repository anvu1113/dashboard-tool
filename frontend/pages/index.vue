<template>
  <div>Loading...</div>
</template>

<script setup>
definePageMeta({
  middleware: [
    function (to, from) {
      return navigateTo('/home')
    }
  ]
})
</script>
