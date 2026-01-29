<template>
  <Teleport to="body">
    <Transition
      enter-active-class="transition duration-200 ease-out"
      enter-from-class="opacity-0"
      enter-to-class="opacity-100"
      leave-active-class="transition duration-150 ease-in"
      leave-from-class="opacity-100"
      leave-to-class="opacity-0"
    >
      <div v-if="isOpen" class="fixed inset-0 z-[100] flex items-center justify-center bg-black/60 backdrop-blur-sm p-4" @click.self="close">
        <div 
          class="w-full max-w-sm bg-card-dark border border-gray-700/50 rounded-xl shadow-2xl overflow-hidden transform transition-all scale-100"
          role="dialog"
          aria-modal="true"
        >
          <!-- Icon & Header -->
          <div class="p-6 text-center">
            <div class="mx-auto flex items-center justify-center h-16 w-16 rounded-full mb-4" :class="{
              'bg-green-500/10 text-green-500': state.type === 'success',
              'bg-red-500/10 text-red-500': state.type === 'error',
              'bg-blue-500/10 text-blue-500': state.type === 'info',
            }">
              <!-- Success Icon -->
              <svg v-if="state.type === 'success'" class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
              <!-- Error Icon -->
              <svg v-else-if="state.type === 'error'" class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" /></svg>
              <!-- Info Icon -->
              <svg v-else class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
            </div>

            <h3 class="text-xl font-bold text-white mb-2">{{ state.title }}</h3>
            <p class="text-gray-400">{{ state.message }}</p>
          </div>

          <!-- Actions -->
          <div class="p-4 bg-gray-800/50 border-t border-gray-700/50 flex justify-center">
            <button 
              @click="confirm" 
              class="w-full py-2.5 px-4 rounded-lg font-medium transition-all shadow-lg text-white"
              :class="{
                'bg-gradient-to-r from-green-500 to-green-600 hover:from-green-600 hover:to-green-700': state.type === 'success',
                'bg-gradient-to-r from-red-500 to-red-600 hover:from-red-600 hover:to-red-700': state.type === 'error',
                'bg-gradient-to-r from-blue-500 to-blue-600 hover:from-blue-600 hover:to-blue-700': state.type === 'info',
              }"
            >
              {{ state.confirmText }}
            </button>
          </div>
        </div>
      </div>
    </Transition>
  </Teleport>
</template>

<script setup>
const { isOpen, state, close, confirm } = useModal()
</script>
