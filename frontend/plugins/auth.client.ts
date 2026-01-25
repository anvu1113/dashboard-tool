export default defineNuxtPlugin(() => {
  const { initAuth } = useAuth()
  
  // Initialize auth on app start
  initAuth()
})






