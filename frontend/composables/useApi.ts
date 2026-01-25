/**
 * Composable for API calls
 * Ensures client-side calls use localhost (browser can't resolve docker hostnames)
 */
export const useApi = () => {
  const config = useRuntimeConfig()

  const getApiBase = () => {
    if (process.client) {
      // Browser always uses localhost
      return 'http://localhost:8000'
    }
    // Server-side can use the configured URL
    return config.public.apiBase || 'http://localhost:8000'
  }

  return {
    getApiBase
  }
}



