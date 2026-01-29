
const activeAction = ref<(() => void) | null>(null)

export const useModal = () => {
  const isOpen = useState('modal_is_open', () => false)
  const modalState = useState('modal_state', () => ({
    title: '',
    message: '',
    type: 'success', // success | error | info
    confirmText: 'OK',
    // onConfirm removed from here to avoid serialization error
  }))

  const show = ({ title, message, type = 'success', confirmText = 'OK', onConfirm = null }: { title: string, message: string, type?: 'success' | 'error' | 'info', confirmText?: string, onConfirm?: () => void }) => {
    modalState.value = {
      title,
      message,
      type,
      confirmText
    }
    // Store function in a local ref (client-side)
    activeAction.value = onConfirm || null
    isOpen.value = true
  }

  const close = () => {
    isOpen.value = false
    // Delay clearing state to allow transition to finish
    setTimeout(() => {
      activeAction.value = null
    }, 300)
  }

  const confirm = () => {
    if (activeAction.value) {
      activeAction.value()
    }
    close()
  }

  return {
    isOpen,
    state: modalState,
    show,
    close,
    confirm
  }
}
