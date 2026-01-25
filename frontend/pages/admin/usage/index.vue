<template>
  <div class="p-6">
    <h1 class="text-2xl font-bold mb-4">Usage Logs</h1>
    <div class="bg-white rounded-lg shadow overflow-hidden">
      <table class="min-w-full">
        <thead class="bg-gray-50">
          <tr>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Time</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">License</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Endpoint</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">IP</th>
          </tr>
        </thead>
        <tbody class="bg-white divide-y divide-gray-200">
           <!-- TODO: Integrate API data -->
           <tr>
             <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500" colspan="4">Loading... (API Integration needed)</td>
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
