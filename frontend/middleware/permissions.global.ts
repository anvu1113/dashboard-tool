export default defineNuxtRouteMiddleware((to) => {
  const { hasAllPermissions } = useAuth()

  if (!to.meta.permissions) return

  const required = to.meta.permissions as string[]

  if (!hasAllPermissions(required)) {
    // Redirect to 403 page or home with error
    // If 403 page exists
    return navigateTo('/403') 
    // Or assert failure
    // throw createError({ statusCode: 403, statusMessage: 'Forbidden' })
  }
})
