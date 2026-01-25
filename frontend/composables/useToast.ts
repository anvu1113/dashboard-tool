import { push } from 'notivue'

export const useToast = () => {
  const success = (message: string, title?: string) => {
    push.success({
      title: title || 'Thành công',
      message
    })
  }

  const error = (message: string, title?: string) => {
    push.error({
      title: title || 'Lỗi',
      message
    })
  }

  const warning = (message: string, title?: string) => {
    push.warning({
      title: title || 'Cảnh báo',
      message
    })
  }

  const info = (message: string, title?: string) => {
    push.info({
      title: title || 'Thông báo',
      message
    })
  }

  const promise = async <T,>(
    promiseFn: Promise<T>,
    messages: {
      loading?: string
      success?: string | ((data: T) => string)
      error?: string | ((error: any) => string)
    }
  ) => {
    return push.promise(promiseFn, {
      loading: {
        title: 'Đang xử lý...',
        message: messages.loading || 'Vui lòng đợi'
      },
      success: (data) => ({
        title: 'Thành công',
        message: typeof messages.success === 'function' 
          ? messages.success(data) 
          : messages.success || 'Hoàn thành'
      }),
      error: (error) => ({
        title: 'Lỗi',
        message: typeof messages.error === 'function'
          ? messages.error(error)
          : messages.error || 'Đã có lỗi xảy ra'
      })
    })
  }

  return {
    success,
    error,
    warning,
    info,
    promise
  }
}
