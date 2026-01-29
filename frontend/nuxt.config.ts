// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: ['@nuxtjs/tailwindcss'],
  css: ['~/assets/css/main.css', '~/assets/css/vue-select.css'],
  runtimeConfig: {
    public: {
      apiBase: '' // Use relative path, handled by proxy
    }
  },
  nitro: {
    routeRules: {
      '/api/**': { proxy: 'http://api:8000/api/**' }
    }
  },
  build: {
    transpile: [
      'vue-filepond',
      'filepond',
      'filepond-plugin-file-validate-type',
      'filepond-plugin-image-preview'
    ]
  },
  vite: {
    optimizeDeps: {
      include: [
        'vue-filepond',
        'filepond-plugin-file-validate-type',
        'filepond-plugin-image-preview'
      ]
    }
  }
})








