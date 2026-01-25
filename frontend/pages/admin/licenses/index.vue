<template>
  <div class="p-6">
    <h1 class="text-2xl font-bold mb-4">License Management</h1>
    <div class="mb-4">
      <button class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">Create License</button>
    </div>
    <div class="bg-white rounded-lg shadow overflow-hidden">
      <table class="min-w-full">
        <thead class="bg-gray-50">
          <tr>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Key</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">User</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Type</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Status</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Expires</th>
          </tr>
        </thead>
        <tbody class="bg-white divide-y divide-gray-200">
           <!-- TODO: Integrate API data -->
           <tr>
             <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500" colspan="5">Loading... (API Integration needed)</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
definePageMeta({
  middleware: ['auth']
})
</script>
