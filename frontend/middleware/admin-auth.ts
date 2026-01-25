export default defineNuxtRouteMiddleware((to, from) => {
  const { isAuthenticated, user } = useAuth()

  if (!isAuthenticated.value) {
    return navigateTo(`/login?redirect=${to.fullPath}`)
  }

  // Check if user has admin role
  // Assuming 'admin' is the role value for administrators
  // Adjust this check based on your actual role values (e.g., 1, 'ADMIN', etc.)
  if (user.value?.role !== 'admin' && user.value?.role !== 1) {
    return navigateTo('/')
  }
})
