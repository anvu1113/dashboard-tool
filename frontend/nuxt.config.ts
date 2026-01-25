// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: ['@nuxtjs/tailwindcss'],
  css: ['~/assets/css/main.css', '~/assets/css/vue-select.css'],
  runtimeConfig: {
    public: {
      // Always use localhost for client-side API calls (browser can't resolve docker hostnames)
      apiBase: process.env.API_BASE_URL || 'http://localhost:8000'
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








