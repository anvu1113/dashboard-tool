export default defineNuxtPlugin(() => {
  return {
    provide: {
      can: (permission: string) => {
        const { hasPermission } = useAuth()
        return hasPermission(permission)
      },
      canAny: (permissions: string[]) => {
        const { hasAnyPermission } = useAuth()
        return hasAnyPermission(permissions)
      },
      canAll: (permissions: string[]) => {
          const { hasAllPermissions } = useAuth()
          return hasAllPermissions(permissions)
      }
    }
  }
})
