# 🔍 Vue Select - Searchable Dropdown Guide

## 📦 Đã cài đặt
- **Package**: `vue-select@beta` (Vue 3 compatible)
- **Plugin**: `/plugins/vue-select.client.ts`
- **Styles**: `/assets/css/vue-select.css` (Dark theme)

---

## 🎯 Khi nào dùng VSelect?

### ✅ Dùng VSelect khi:
- Danh sách có **nhiều options** (>10 items)
- Cần **search/filter** options
- Cần **clear** selection
- Cần **multiple select**
- Cần **lazy loading** (load thêm khi scroll)

### ❌ Dùng `<select>` native khi:
- Danh sách **ít options** (<10 items)
- Không cần search
- Form đơn giản

---

## 💡 Cách sử dụng

### Basic Usage (Single Select)

```vue
<template>
  <div>
    <label class="block text-sm font-semibold text-gray-200 mb-2">
      Loại tin tức
    </label>
    <VSelect
      v-model="form.category_id"
      :options="categories"
      :reduce="cat => cat.id"
      label="name"
      placeholder="-- Tìm kiếm hoặc chọn --"
      :clearable="true"
      :searchable="true"
    >
      <template #no-options>
        Không tìm thấy kết quả
      </template>
    </VSelect>
  </div>
</template>

<script setup>
const form = reactive({
  category_id: null
})

const categories = ref([
  { id: 1, name: 'Công nghệ' },
  { id: 2, name: 'Thời trang' },
  { id: 3, name: 'Ẩm thực' }
])
</script>
```

### Multiple Select

```vue
<VSelect
  v-model="form.tag_ids"
  :options="tags"
  :reduce="tag => tag.id"
  label="name"
  placeholder="Chọn nhiều tags"
  :multiple="true"
  :searchable="true"
  :close-on-select="false"
>
  <template #no-options>
    Không tìm thấy tag
  </template>
</VSelect>
```

### With Custom Display

```vue
<VSelect
  v-model="form.user_id"
  :options="users"
  :reduce="user => user.id"
  label="name"
  placeholder="Chọn người dùng"
>
  <template #option="{ name, email }">
    <div>
      <strong>{{ name }}</strong>
      <div class="text-xs text-gray-400">{{ email }}</div>
    </div>
  </template>
  
  <template #selected-option="{ name }">
    <strong>{{ name }}</strong>
  </template>
</VSelect>
```

### With Loading State

```vue
<VSelect
  v-model="form.product_id"
  :options="products"
  :reduce="p => p.id"
  label="name"
  :loading="isLoading"
  placeholder="Đang tải..."
>
  <template #spinner="{ loading }">
    <div v-if="loading" class="vs__spinner">Loading...</div>
  </template>
</VSelect>
```

---

## 🎨 Props quan trọng

| Prop | Type | Default | Mô tả |
|------|------|---------|-------|
| `v-model` | Any | - | Giá trị được chọn |
| `options` | Array | `[]` | Danh sách options |
| `reduce` | Function | - | Hàm để lấy giá trị từ object |
| `label` | String | `'label'` | Key để hiển thị text |
| `placeholder` | String | - | Placeholder text |
| `searchable` | Boolean | `true` | Cho phép search |
| `clearable` | Boolean | `true` | Hiện nút clear |
| `multiple` | Boolean | `false` | Chọn nhiều |
| `disabled` | Boolean | `false` | Disable select |
| `loading` | Boolean | `false` | Hiện loading spinner |
| `closeOnSelect` | Boolean | `true` | Đóng dropdown sau khi chọn |

---

## 📋 Áp dụng cho tất cả Select

### Danh sách cần update:

#### Posts Module
- ✅ `/pages/admin/posts/create.vue` - post_category_id
- ⏳ `/pages/admin/posts/[id].vue` - post_category_id

#### Products Module
- ⏳ `/pages/admin/products/create.vue` - category_id
- ⏳ `/pages/admin/products/[id].vue` - category_id

#### Các module khác (nếu có select)
- Kiểm tra tất cả `<select>` tags
- Thay thế bằng `<VSelect>` nếu cần search

---

## 🎯 Template chuẩn

### Single Select (Category, Status, etc.)

```vue
<div>
  <label class="block text-sm font-semibold text-gray-200 mb-2">
    [Label] <span v-if="required" class="text-red-400">*</span>
  </label>
  <VSelect
    v-model="form.field_id"
    :options="items"
    :reduce="item => item.id"
    label="name"
    placeholder="-- Tìm kiếm hoặc chọn [label] --"
    :clearable="!required"
    :searchable="true"
  >
    <template #no-options>
      Không tìm thấy kết quả
    </template>
  </VSelect>
</div>
```

### Multiple Select (Tags, Permissions, etc.)

```vue
<div>
  <label class="block text-sm font-semibold text-gray-200 mb-2">
    [Label]
  </label>
  <VSelect
    v-model="form.field_ids"
    :options="items"
    :reduce="item => item.id"
    label="name"
    placeholder="Chọn một hoặc nhiều [label]"
    :multiple="true"
    :searchable="true"
    :close-on-select="false"
  >
    <template #no-options>
      Không tìm thấy kết quả
    </template>
  </VSelect>
  <p class="text-xs text-gray-400 mt-1">
    Đã chọn: {{ form.field_ids?.length || 0 }}
  </p>
</div>
```

---

## 🎨 Dark Theme

Đã custom CSS cho dark theme tại `/assets/css/vue-select.css`:
- Background: `bg-gray-700/50`
- Border: `border-gray-600`
- Text: `text-white`
- Hover: `bg-blue-500/20`
- Selected: `bg-blue-500/30`

---

## 🚀 Advanced Features

### Lazy Loading (Load more on scroll)

```vue
<VSelect
  v-model="selected"
  :options="visibleOptions"
  @open="onOpen"
  @search="onSearch"
>
  <template #list-footer>
    <li v-if="hasMore" class="text-center py-2">
      <button @click="loadMore">Tải thêm...</button>
    </li>
  </template>
</VSelect>

<script setup>
const page = ref(1)
const visibleOptions = ref([])

const loadMore = async () => {
  page.value++
  const newData = await fetchData(page.value)
  visibleOptions.value.push(...newData)
}
</script>
```

### Custom Filter

```vue
<VSelect
  :options="options"
  :filter-by="customFilter"
>
</VSelect>

<script setup>
const customFilter = (option, label, search) => {
  // Custom search logic
  return label.toLowerCase().includes(search.toLowerCase())
}
</script>
```

---

## 📝 Checklist Migration

Khi migrate từ `<select>` sang `<VSelect>`:

- [ ] Import không cần (đã global)
- [ ] Thay `<select>` → `<VSelect>`
- [ ] Thay `<option>` → `:options` prop
- [ ] Thêm `:reduce` nếu cần lấy ID
- [ ] Thêm `label` prop
- [ ] Thêm `placeholder`
- [ ] Thêm `#no-options` template
- [ ] Test search functionality
- [ ] Test clear functionality
- [ ] Check dark theme styling

---

## 🐛 Troubleshooting

### VSelect không hiện
- Check plugin đã load: `/plugins/vue-select.client.ts`
- Check CSS đã import trong `nuxt.config.ts`

### Styling bị lỗi
- Check `/assets/css/vue-select.css` đã load
- Check Tailwind classes compile đúng

### v-model không work
- Check `:reduce` prop đúng
- Check `label` prop match với data structure

---

**GHI NHỚ**: Dùng VSelect cho tất cả dropdown cần search!
