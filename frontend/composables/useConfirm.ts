import Swal from 'sweetalert2'

export const useConfirm = () => {
  /**
   * Show confirmation dialog
   * @param {string} message - Main message
   * @param {string} title - Dialog title (default: 'Xác nhận')
   * @returns {Promise<boolean>} - true if confirmed, false if cancelled
   */
  const confirm = async (message: string, title: string = 'Xác nhận') => {
    const result = await Swal.fire({
      title,
      text: message,
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: 'Đồng ý',
      cancelButtonText: 'Hủy',
      background: '#1f2937', // gray-800
      color: '#fff',
      customClass: {
        popup: 'rounded-lg',
        confirmButton: 'px-6 py-2 rounded-lg',
        cancelButton: 'px-6 py-2 rounded-lg'
      }
    })

    return result.isConfirmed
  }

  /**
   * Show delete confirmation dialog
   * @param {string} itemName - Name of item to delete (optional)
   * @returns {Promise<boolean>}
   */
  const confirmDelete = async (itemName?: string) => {
    const message = itemName 
      ? `Bạn có chắc muốn xóa "${itemName}"?`
      : 'Bạn có chắc muốn xóa?'
    
    const result = await Swal.fire({
      title: 'Xác nhận xóa',
      text: message,
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#ef4444', // red-500
      cancelButtonColor: '#6b7280', // gray-500
      confirmButtonText: 'Xóa',
      cancelButtonText: 'Hủy',
      background: '#1f2937',
      color: '#fff',
      customClass: {
        popup: 'rounded-lg',
        confirmButton: 'px-6 py-2 rounded-lg',
        cancelButton: 'px-6 py-2 rounded-lg'
      }
    })

    return result.isConfirmed
  }

  /**
   * Show success alert
   * @param {string} message
   * @param {string} title
   */
  const alert = async (message: string, title: string = 'Thông báo') => {
    await Swal.fire({
      title,
      text: message,
      icon: 'info',
      confirmButtonColor: '#3085d6',
      confirmButtonText: 'OK',
      background: '#1f2937',
      color: '#fff',
      customClass: {
        popup: 'rounded-lg',
        confirmButton: 'px-6 py-2 rounded-lg'
      }
    })
  }

  return {
    confirm,
    confirmDelete,
    alert
  }
}
