<template>
  <div class="min-h-screen bg-bg-dark flex font-sans text-text">
    <!-- Sidebar -->
    <aside class="w-64 bg-card-dark border-r border-border-dark flex-shrink-0 fixed h-full z-20 flex flex-col">
      <div class="h-16 flex items-center px-6 border-b border-border-dark flex-shrink-0">
        <span class="text-xl font-bold bg-gradient-to-r from-blue-400 to-blue-600 bg-clip-text text-transparent">
          Admin Panel
        </span>
      </div>
      
      <nav class="p-4 space-y-1 flex-1 overflow-y-auto custom-scrollbar">
        <template v-for="item in menuItems">
          <NuxtLink 
            v-if="!item.permission || $can(item.permission)"
            :key="item.to"
            :to="item.to" 
            active-class="bg-blue-600/10 text-blue-400 border-r-2 border-blue-500" 
            class="flex items-center gap-3 px-4 py-3 text-gray-300 hover:bg-gray-800 rounded-l-lg transition-colors group"
          >
            <component :is="item.icon" class="w-5 h-5 group-hover:text-white transition-colors" />
            <span class="font-medium group-hover:text-white">{{ item.label }}</span>
          </NuxtLink>
        </template>
      </nav>

       <div class="p-4 border-t border-border-dark flex-shrink-0">
         <button @click="handleLogout" class="flex items-center gap-3 px-4 py-2 w-full text-red-500 hover:text-red-400 hover:bg-gray-800 rounded-lg transition-colors">
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

<script setup>
import { 
  HomeIcon, 
  UsersIcon, 
  CreditCardIcon, 
  ChartBarIcon, 
  GlobeAltIcon, 
  CircleStackIcon, 
  CurrencyDollarIcon, 
  Cog6ToothIcon,
  ShieldCheckIcon
} from '@heroicons/vue/24/outline'

const { logout } = useAuth()
// const router = useRouter() // logout handles redirect

const menuItems = [
  {
    label: 'Dashboard',
    to: '/admin/dashboard',
    icon: HomeIcon,
    permission: 'dashboard.view'
  },
  {
    label: 'Users',
    to: '/admin/users',
    icon: UsersIcon,
    permission: 'users.view'
  },
  {
    label: 'Roles & Permissions',
    to: '/admin/roles',
    icon: ShieldCheckIcon,
    permission: 'roles.manage'
  },
  {
    label: 'Licenses',
    to: '/admin/licenses',
    icon: CreditCardIcon,
    permission: 'subscription.view' // Assuming mapping
  },
  {
    label: 'Usage Logs',
    to: '/admin/usage',
    icon: ChartBarIcon,
    permission: 'usage.view'
  },
  {
    label: 'Supported Domains',
    to: '/admin/supported-domains',
    icon: GlobeAltIcon,
    permission: 'domains.view' // Assuming
  },
  {
    label: 'Cache',
    to: '/admin/cache',
    icon: CircleStackIcon,
    permission: 'cache.manage' // Assuming
  },
  {
    label: 'Tỉ Giá (Exchange Rates)',
    to: '/admin/exchange-rates',
    icon: CurrencyDollarIcon,
    permission: 'exchange_rates.view' // Assuming
  },
  {
    label: 'Settings',
    to: '/admin/settings',
    icon: Cog6ToothIcon,
    permission: 'settings.view' // Assuming
  }
]

const handleLogout = async () => {
  await logout()
}
</script>
