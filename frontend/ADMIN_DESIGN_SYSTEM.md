# 🎨 Admin UI Design System - CHUẨN BẮT BUỘC

> **QUAN TRỌNG**: Tất cả trang admin PHẢI tuân thủ design system này. Không được tự ý thay đổi màu sắc, kích thước, vị trí.

---

## 📐 Layout Structure

### Header Section
```vue
<div class="flex justify-between items-center mb-6">
  <h1 class="text-3xl font-bold bg-gradient-to-r from-white to-gray-200 bg-clip-text text-transparent">
    [Tiêu đề trang]
  </h1>
  <NuxtLink to="[back-url]" class="inline-flex items-center gap-2 text-blue-400 hover:text-blue-300 font-medium transition-colors">
    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
    </svg>
    Quay lại
  </NuxtLink>
</div>
```

### Content Container
```vue
<div class="bg-gray-800/50 backdrop-blur-xl rounded-lg shadow-xl border border-gray-700/50 p-6">
  <!-- Form content -->
</div>
```

---

## 🎨 Color Palette

### Primary Actions (Submit/Save/Create/Update)
- **Color**: Blue gradient
- **Class**: `bg-gradient-to-r from-blue-500 to-blue-600`
- **Hover**: `hover:shadow-blue-500/50`

### Destructive Actions (Delete)
- **Confirm Dialog**: Red (`#ef4444`)
- **In SweetAlert2**: Already configured

### Secondary Actions (Cancel/Back)
- **Color**: Gray border
- **Class**: `border-2 border-gray-600 text-gray-300`
- **Hover**: `hover:border-gray-500 hover:text-white`

### Success Actions (Add New in list)
- **Color**: Green gradient
- **Class**: `bg-gradient-to-r from-green-500 to-green-600`
- **Hover**: `hover:shadow-green-500/50`

---

## 🔘 Button Standards

### Submit Button (Create/Update)
**CHUẨN BẮT BUỘC - KHÔNG THAY ĐỔI:**

```vue
<button 
  type="submit"
  :disabled="loading"
  class="inline-flex justify-center items-center gap-2 py-3 px-8 min-w-[200px] bg-gradient-to-r from-blue-500 to-blue-600 text-white rounded-lg shadow-lg hover:shadow-blue-500/50 font-medium focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary disabled:opacity-50 transition-all"
>
  <!-- Icon: Checkmark when idle -->
  <svg v-if="!loading" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
  </svg>
  
  <!-- Icon: Spinner when loading -->
  <svg v-else class="animate-spin w-5 h-5" fill="none" viewBox="0 0 24 24">
    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
  </svg>
  
  {{ loading ? 'Đang lưu...' : 'Tạo mới' }}
  <!-- Hoặc: {{ loading ? 'Đang lưu...' : 'Cập nhật' }} -->
</button>
```

### Cancel Button
```vue
<NuxtLink 
  to="/admin/[module]"
  class="px-6 py-3 border-2 border-gray-600 text-gray-300 rounded-lg hover:border-gray-500 hover:text-white font-medium transition-colors"
>
  Hủy
</NuxtLink>
```

### Add New Button (List pages)
```vue
<NuxtLink 
  to="/admin/[module]/create" 
  class="bg-gradient-to-r from-green-500 to-green-600 text-white px-6 py-3 rounded-lg hover:shadow-lg hover:shadow-green-500/50 transition-all duration-200 font-medium flex items-center gap-2"
>
  <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
  </svg>
  Thêm mới
</NuxtLink>
```

### Edit Button (In table)
```vue
<NuxtLink 
  :to="`/admin/[module]/${item.id}`" 
  class="inline-flex items-center gap-1 text-blue-400 hover:text-blue-300 mr-4 transition-colors"
>
  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
  </svg>
  Sửa
</NuxtLink>
```

### Delete Button (In table)
```vue
<button 
  @click="deleteItem(item.id)" 
  class="inline-flex items-center gap-1 text-red-400 hover:text-red-300 transition-colors"
>
  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
  </svg>
  Xóa
</button>
```

---

## 📝 Form Elements

### Input Fields
```vue
<input 
  v-model="form.field"
  type="text"
  required
  class="block w-full bg-gray-700/50 border border-gray-600 text-white rounded-lg shadow-sm py-3 px-4 focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent placeholder-gray-400"
  placeholder="Nhập..."
/>
```

### Textarea
```vue
<textarea 
  v-model="form.field"
  rows="4"
  class="block w-full bg-gray-700/50 border border-gray-600 text-white rounded-lg shadow-sm py-3 px-4 focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent placeholder-gray-400"
  placeholder="Nhập mô tả..."
></textarea>
```

### Select Dropdown
```vue
<select 
  v-model="form.field"
  class="block w-full bg-gray-700/50 border border-gray-600 text-white rounded-lg shadow-sm py-3 px-4 focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent"
>
  <option :value="null">-- Chọn --</option>
  <option v-for="item in items" :key="item.id" :value="item.id">
    {{ item.name }}
  </option>
</select>
```

### Checkbox
```vue
<div class="flex items-center gap-3">
  <input 
    v-model="form.field"
    type="checkbox"
    id="field_id"
    class="w-5 h-5 rounded bg-gray-700 border-gray-600 text-blue-500 focus:ring-2 focus:ring-blue-500"
  />
  <label for="field_id" class="text-sm font-semibold text-gray-200">
    Label text
  </label>
</div>
```

---

## 📊 Table Design

### Table Container
```vue
<div class="bg-gray-800/50 backdrop-blur-xl rounded-lg shadow-xl border border-gray-700/50 overflow-hidden">
  <table class="min-w-full divide-y divide-gray-700/50">
    <!-- Table content -->
  </table>
</div>
```

### Table Header
```vue
<thead class="bg-gray-700/30">
  <tr>
    <th class="px-6 py-4 text-left text-xs font-semibold text-gray-300 uppercase tracking-wider">
      Column Name
    </th>
  </tr>
</thead>
```

### Table Body
```vue
<tbody class="divide-y divide-gray-700/50">
  <tr v-for="item in items" :key="item.id" class="hover:bg-gray-700/30 transition-colors">
    <td class="px-6 py-4 whitespace-nowrap text-sm font-semibold text-white">
      {{ item.name }}
    </td>
  </tr>
</tbody>
```

---

## 🎯 Action Buttons Position

### Form Actions (Bottom Right)
```vue
<div class="flex justify-end gap-4 pt-4 border-t border-gray-700">
  <!-- Cancel button (left) -->
  <NuxtLink to="..." class="...">Hủy</NuxtLink>
  
  <!-- Submit button (right) -->
  <button type="submit" class="...">Lưu</button>
</div>
```

### List Page Header (Top Right)
```vue
<div class="flex justify-between items-center mb-6">
  <h1>...</h1>
  <!-- Add new button (right) -->
  <NuxtLink to="..." class="...">Thêm mới</NuxtLink>
</div>
```

### Table Row Actions (Right Aligned)
```vue
<td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
  <!-- Edit (left) -->
  <NuxtLink :to="..." class="... mr-4">Sửa</NuxtLink>
  
  <!-- Delete (right) -->
  <button @click="..." class="...">Xóa</button>
</td>
```

---

## 🔔 Notifications

### Toast (Thông báo)
```javascript
const toast = useToast()

// Success
toast.success('Thành công!')

// Error
toast.error('Lỗi!', 'Tiêu đề')

// Warning
toast.warning('Cảnh báo!')

// Info
toast.info('Thông tin')
```

### Confirm Dialog (Xác nhận)
```javascript
const { confirmDelete, confirm } = useConfirm()

// Delete confirmation
const ok = await confirmDelete('item này')
if (!ok) return

// Custom confirmation
const ok = await confirm('Message', 'Title')
if (!ok) return
```

---

## 📱 Responsive Classes

### Grid Layouts
- 2 columns: `grid grid-cols-2 gap-4`
- 3 columns: `grid grid-cols-3 gap-4`

### Spacing
- Section spacing: `space-y-6`
- Form spacing: `space-y-4`
- Button gap: `gap-3` or `gap-4`

---

## ✅ Checklist Tạo Page Mới

Khi tạo page admin mới, PHẢI có:

### List Page (`index.vue`)
- [ ] Header với title gradient white-to-gray
- [ ] Button "Thêm mới" màu green (top right)
- [ ] Table với bg-gray-800/50
- [ ] Button "Sửa" màu blue
- [ ] Button "Xóa" màu red
- [ ] SweetAlert2 confirm khi xóa
- [ ] Toast success sau khi xóa
- [ ] Middleware: `admin-auth`

### Create Page (`create.vue`)
- [ ] Header với "Quay lại" link
- [ ] Form container bg-gray-800/50
- [ ] Input fields với bg-gray-700/50
- [ ] Button "Tạo mới" màu blue (với icon)
- [ ] Button "Hủy" gray border
- [ ] Toast success sau khi tạo
- [ ] Toast error khi fail
- [ ] Middleware: `admin-auth`

### Edit Page (`[id].vue`)
- [ ] Header với "Quay lại" link
- [ ] Form container bg-gray-800/50
- [ ] Input fields với bg-gray-700/50
- [ ] Button "Cập nhật" màu blue (với icon)
- [ ] Button "Hủy" gray border
- [ ] Toast success sau khi update
- [ ] Toast error khi fail
- [ ] Middleware: `admin-auth`

---

## 🚫 KHÔNG ĐƯỢC LÀM

❌ Thay đổi màu button submit (PHẢI là blue)
❌ Thay đổi kích thước button (PHẢI là `py-3 px-8 min-w-[200px]`)
❌ Bỏ icon loading spinner
❌ Dùng `alert()` hoặc `confirm()` native
❌ Thay đổi vị trí button (submit luôn bên phải)
❌ Dùng màu khác cho "Thêm mới" button (PHẢI là green)
❌ Thay đổi background color của form/table
❌ Bỏ hover effects
❌ Thay đổi text color (white cho primary, gray-300 cho secondary)

---

## 📚 Reference Files

Tham khảo các file mẫu chuẩn:
- `/pages/admin/categories/index.vue` - List page
- `/pages/admin/categories/create.vue` - Create page
- `/pages/admin/categories/[id].vue` - Edit page
- `/composables/useToast.ts` - Toast notifications
- `/composables/useConfirm.ts` - Confirm dialogs

---

**GHI NHỚ**: Design system này là CHUẨN. Mọi page mới PHẢI tuân thủ 100%.
