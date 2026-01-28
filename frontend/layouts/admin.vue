<template>
  <div class="min-h-screen bg-bg-dark flex font-sans text-text">
    <!-- Sidebar -->
    <aside class="w-64 bg-card-dark border-r border-border-dark flex-shrink-0 fixed h-full z-20 overflow-y-auto">
      <div class="h-16 flex items-center px-6 border-b border-border-dark">
        <span class="text-xl font-bold bg-gradient-to-r from-blue-400 to-blue-600 bg-clip-text text-transparent">
          Admin Panel
        </span>
      </div>
      
      <nav class="p-4 space-y-1">
        <NuxtLink to="/admin/dashboard" active-class="bg-blue-600/10 text-blue-400 border-r-2 border-blue-500" class="flex items-center gap-3 px-4 py-3 text-gray-300 hover:bg-gray-800 rounded-l-lg transition-colors group">
          <svg class="w-5 h-5 group-hover:text-white transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24">
             <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z" />
          </svg>
          <span class="font-medium group-hover:text-white">Dashboard</span>
        </NuxtLink>

        <NuxtLink to="/admin/users" active-class="bg-blue-600/10 text-blue-400 border-r-2 border-blue-500" class="flex items-center gap-3 px-4 py-3 text-gray-300 hover:bg-gray-800 rounded-l-lg transition-colors group">
          <svg class="w-5 h-5 group-hover:text-white transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24">
             <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z" />
          </svg>
          <span class="font-medium group-hover:text-white">Users</span>
        </NuxtLink>

        <NuxtLink to="/admin/licenses" active-class="bg-blue-600/10 text-blue-400 border-r-2 border-blue-500" class="flex items-center gap-3 px-4 py-3 text-gray-300 hover:bg-gray-800 rounded-l-lg transition-colors group">
          <svg class="w-5 h-5 group-hover:text-white transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24">
             <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 5v2m0 4v2m0 4v2M5 5a2 2 0 00-2 2v3a2 2 0 110 4v3a2 2 0 002 2h14a2 2 0 002-2v-3a2 2 0 110-4V7a2 2 0 00-2-2H5z" />
          </svg>
          <span class="font-medium group-hover:text-white">Licenses</span>
        </NuxtLink>

        <NuxtLink to="/admin/usage" active-class="bg-blue-600/10 text-blue-400 border-r-2 border-blue-500" class="flex items-center gap-3 px-4 py-3 text-gray-300 hover:bg-gray-800 rounded-l-lg transition-colors group">
          <svg class="w-5 h-5 group-hover:text-white transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24">
             <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
          </svg>
          <span class="font-medium group-hover:text-white">Usage Logs</span>
        </NuxtLink>

        <NuxtLink to="/admin/settings" active-class="bg-blue-600/10 text-blue-400 border-r-2 border-blue-500" class="flex items-center gap-3 px-4 py-3 text-gray-300 hover:bg-gray-800 rounded-l-lg transition-colors group">
          <svg class="w-5 h-5 group-hover:text-white transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24">
             <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
             <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
          </svg>
          <span class="font-medium group-hover:text-white">Settings</span>
        </NuxtLink>
      </nav>

       <div class="absolute bottom-0 w-full p-4 border-t border-border-dark">
         <button class="flex items-center gap-3 px-4 py-2 w-full text-red-500 hover:text-red-400 hover:bg-gray-800 rounded-lg transition-colors">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
            </svg>
            <span class="font-medium">Logout</span>
         </button>
       </div>
    </aside>

    <!-- Main Content -->
    <main class="flex-1 ml-64 p-8">
      <div class="max-w-7xl mx-auto">
         <slot />
      </div>
    </main>
  </div>
</template>
