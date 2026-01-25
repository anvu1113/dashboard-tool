import { createNotivue } from 'notivue'
import 'notivue/notification.css'
import 'notivue/animations.css'

export default defineNuxtPlugin((nuxtApp) => {
  const notivue = createNotivue({
    position: 'top-right',
    limit: 4,
    enqueue: true,
    avoidDuplicates: true,
    notifications: {
      global: {
        duration: 4000
      }
    }
  })

  nuxtApp.vueApp.use(notivue)
})
