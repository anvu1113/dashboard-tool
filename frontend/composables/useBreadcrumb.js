export const useBreadcrumb = () => {
  const route = useRoute()
  
  const getBreadcrumbs = () => {
    const path = route.path
    const items = []
    
    // Categories
    if (path.startsWith('/admin/categories')) {
      if (path.includes('/create')) {
        items.push({ label: 'Loại sản phẩm', to: '/admin/categories' })
        items.push({ label: 'Thêm mới' })
      } else if (path.match(/\/\d+$/)) {
        items.push({ label: 'Loại sản phẩm', to: '/admin/categories' })
        items.push({ label: 'Chỉnh sửa' })
      } else {
        // Index page - no 'to' prop so it's active
        items.push({ label: 'Loại sản phẩm' })
      }
    }
    
    // Products
    else if (path.startsWith('/admin/products')) {
      if (path.includes('/create')) {
        items.push({ label: 'Sản phẩm', to: '/admin/products' })
        items.push({ label: 'Thêm mới' })
      } else if (path.match(/\/\d+$/)) {
        items.push({ label: 'Sản phẩm', to: '/admin/products' })
        items.push({ label: 'Chỉnh sửa' })
      } else {
        // Index page - no 'to' prop so it's active
        items.push({ label: 'Sản phẩm' })
      }
    }
    
    // Posts
    else if (path.startsWith('/admin/posts')) {
      if (path.includes('/create')) {
        items.push({ label: 'Bài viết', to: '/admin/posts' })
        items.push({ label: 'Viết bài mới' })
      } else if (path.match(/\/\d+$/)) {
        items.push({ label: 'Bài viết', to: '/admin/posts' })
        items.push({ label: 'Chỉnh sửa' })
      } else {
        // Index page - no 'to' prop so it's active
        items.push({ label: 'Bài viết' })
      }
    }
    
    // Orders
    else if (path.startsWith('/admin/orders')) {
      if (path.match(/\/\d+$/)) {
        items.push({ label: 'Đơn hàng', to: '/admin/orders' })
        items.push({ label: 'Chi tiết' })
      } else {
        // Index page - no 'to' prop so it's active
        items.push({ label: 'Đơn hàng' })
      }
    }
    
    // Post Categories
    else if (path.startsWith('/admin/post-categories')) {
      if (path.includes('/create')) {
        items.push({ label: 'Loại tin tức', to: '/admin/post-categories' })
        items.push({ label: 'Thêm mới' })
      } else if (path.match(/\/\d+$/)) {
        items.push({ label: 'Loại tin tức', to: '/admin/post-categories' })
        items.push({ label: 'Chỉnh sửa' })
      } else {
        // Index page - no 'to' prop so it's active
        items.push({ label: 'Loại tin tức' })
      }
    }
    
    return items
  }
  
  return {
    breadcrumbs: computed(() => getBreadcrumbs())
  }
}
