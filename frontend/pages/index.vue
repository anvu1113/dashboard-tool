<template>
  <div class="p-6">
    <h1 class="text-2xl font-bold mb-4">Dashboard</h1>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      <div class="bg-white p-6 rounded-lg shadow">
        <h2 class="text-xl font-semibold mb-2">Users</h2>
        <p class="text-gray-600">Manage your platform users.</p>
        <NuxtLink to="/admin/users" class="text-blue-500 hover:underline mt-2 block">Go to Users</NuxtLink>
      </div>
      <div class="bg-white p-6 rounded-lg shadow">
        <h2 class="text-xl font-semibold mb-2">Licenses</h2>
        <p class="text-gray-600">Manage extension licenses.</p>
        <NuxtLink to="/admin/licenses" class="text-blue-500 hover:underline mt-2 block">Go to Licenses</NuxtLink>
      </div>
      <div class="bg-white p-6 rounded-lg shadow">
        <h2 class="text-xl font-semibold mb-2">Usage</h2>
        <p class="text-gray-600">View API usage logs.</p>
        <NuxtLink to="/admin/usage" class="text-blue-500 hover:underline mt-2 block">Go to Usage</NuxtLink>
      </div>
    </div>
  </div>
</template>

<script setup>
definePageMeta({
  middleware: ['auth']
})
</script>
