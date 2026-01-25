<template>
  <nav class="flex items-center space-x-2 text-sm mb-6">
    <!-- Only show Dashboard when there are no other breadcrumb items (i.e., on /admin page) -->
    <template v-if="items.length === 0">
      <span 
        class="flex items-center gap-1 px-3 py-1 bg-gradient-to-r from-primary/20 to-primary-dark/20 text-white font-semibold rounded-md border border-primary/30"
      >
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
        </svg>
        <span>Dashboard</span>
      </span>
    </template>

    <!-- Show breadcrumb items without Dashboard prefix -->
    <template v-for="(item, index) in items" :key="index">
      <svg v-if="index > 0" class="w-4 h-4 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
      </svg>
      
      <NuxtLink 
        v-if="item.to"
        :to="item.to" 
        class="text-gray-400 hover:text-white transition-colors"
      >
        {{ item.label }}
      </NuxtLink>
      <span 
        v-else 
        class="px-3 py-1 bg-gradient-to-r from-primary/20 to-primary-dark/20 text-white font-semibold rounded-md border border-primary/30"
      >
        {{ item.label }}
      </span>
    </template>
  </nav>
</template>

<script setup>
const route = useRoute()

defineProps({
  items: {
    type: Array,
    default: () => []
  }
})
</script>
