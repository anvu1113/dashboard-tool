<template>
  <div class="tiptap-editor border border-gray-600 rounded-lg overflow-hidden bg-white">
    <div v-if="editor" class="toolbar flex flex-wrap gap-2 p-3 border-b border-gray-300 bg-gray-100">
      <button
        type="button"
        @click="editor.chain().focus().toggleBold().run()"
        :disabled="!editor.can().chain().focus().toggleBold().run()"
        :class="{ 'is-active': editor.isActive('bold') }"
        class="p-2 rounded hover:bg-gray-200 text-gray-700 hover:text-gray-900 transition-colors"
        title="Bold"
      >
        <span class="font-bold">B</span>
      </button>
      <button
        type="button"
        @click="editor.chain().focus().toggleItalic().run()"
        :disabled="!editor.can().chain().focus().toggleItalic().run()"
        :class="{ 'is-active': editor.isActive('italic') }"
        class="p-2 rounded hover:bg-gray-200 text-gray-700 hover:text-gray-900 transition-colors"
        title="Italic"
      >
        <span class="italic">I</span>
      </button>
      <button
        type="button"
        @click="editor.chain().focus().toggleStrike().run()"
        :disabled="!editor.can().chain().focus().toggleStrike().run()"
        :class="{ 'is-active': editor.isActive('strike') }"
        class="p-2 rounded hover:bg-gray-200 text-gray-700 hover:text-gray-900 transition-colors"
        title="Strike"
      >
        <span class="line-through">S</span>
      </button>
      <div class="w-px h-6 bg-gray-300 mx-1"></div>
      <button
        type="button"
        @click="editor.chain().focus().toggleHeading({ level: 1 }).run()"
        :class="{ 'is-active': editor.isActive('heading', { level: 1 }) }"
        class="p-2 rounded hover:bg-gray-200 text-gray-700 hover:text-gray-900 font-bold transition-colors"
        title="H1"
      >
        H1
      </button>
      <button
        type="button"
        @click="editor.chain().focus().toggleHeading({ level: 2 }).run()"
        :class="{ 'is-active': editor.isActive('heading', { level: 2 }) }"
        class="p-2 rounded hover:bg-gray-200 text-gray-700 hover:text-gray-900 font-bold transition-colors"
        title="H2"
      >
        H2
      </button>
      <button
        type="button"
        @click="editor.chain().focus().toggleHeading({ level: 3 }).run()"
        :class="{ 'is-active': editor.isActive('heading', { level: 3 }) }"
        class="p-2 rounded hover:bg-gray-200 text-gray-700 hover:text-gray-900 font-bold transition-colors"
        title="H3"
      >
        H3
      </button>
      <div class="w-px h-6 bg-gray-300 mx-1"></div>
      <button
        type="button"
        @click="editor.chain().focus().toggleBulletList().run()"
        :class="{ 'is-active': editor.isActive('bulletList') }"
        class="p-2 rounded hover:bg-gray-200 text-gray-700 hover:text-gray-900 transition-colors"
        title="Bullet List"
      >
        • List
      </button>
      <button
        type="button"
        @click="editor.chain().focus().toggleOrderedList().run()"
        :class="{ 'is-active': editor.isActive('orderedList') }"
        class="p-2 rounded hover:bg-gray-200 text-gray-700 hover:text-gray-900 transition-colors"
        title="Ordered List"
      >
        1. List
      </button>
      <div class="w-px h-6 bg-gray-300 mx-1"></div>
      
      <!-- Image Upload Button -->
      <button
        type="button"
        @click="triggerImageUpload"
        class="p-2 rounded hover:bg-gray-200 text-gray-700 hover:text-gray-900 transition-colors"
        title="Add Image"
      >
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
        </svg>
      </button>
      <input 
        ref="imageInput" 
        type="file" 
        accept="image/*" 
        @change="handleImageUpload" 
        class="hidden"
      />
      
      <div class="w-px h-6 bg-gray-300 mx-1"></div>
      <button
        type="button"
        @click="editor.chain().focus().undo().run()"
        :disabled="!editor.can().chain().focus().undo().run()"
        class="p-2 rounded hover:bg-gray-200 text-gray-700 hover:text-gray-900 transition-colors disabled:opacity-50"
        title="Undo"
      >
        ↺
      </button>
      <button
        type="button"
        @click="editor.chain().focus().redo().run()"
        :disabled="!editor.can().chain().focus().redo().run()"
        class="p-2 rounded hover:bg-gray-200 text-gray-700 hover:text-gray-900 transition-colors disabled:opacity-50"
        title="Redo"
      >
        ↻
      </button>
    </div>
    <editor-content :editor="editor" class="tiptap-content" />
  </div>
</template>

<script setup>
import { useEditor, EditorContent } from '@tiptap/vue-3'
import StarterKit from '@tiptap/starter-kit'
import Image from '@tiptap/extension-image'

const props = defineProps({
  modelValue: {
    type: String,
    default: '',
  },
})

const emit = defineEmits(['update:modelValue'])

const config = useRuntimeConfig()
const { token } = useAuth()
const imageInput = ref(null)

const editor = useEditor({
  content: props.modelValue,
  extensions: [
    StarterKit,
    Image.configure({
      inline: true,
      HTMLAttributes: {
        class: 'max-w-full h-auto rounded-lg my-2',
      },
    }),
  ],
  editorProps: {
      attributes: {
          class: 'prose max-w-none focus:outline-none min-h-[400px] p-4 text-gray-900'
      }
  },
  onUpdate: () => {
    emit('update:modelValue', editor.value.getHTML())
  },
})

const triggerImageUpload = () => {
  imageInput.value?.click()
}

const handleImageUpload = async (event) => {
  const file = event.target.files?.[0]
  if (!file) return

  const formData = new FormData()
  formData.append('file', file)

  try {
    const response = await $fetch(`${config.public.apiBase}/api/upload`, {
      method: 'POST',
      body: formData,
      headers: token.value ? { Authorization: `Bearer ${token.value}` } : {}
    })

    if (response.path) {
      const imageUrl = `${config.public.apiBase}${response.path}`
      editor.value?.chain().focus().setImage({ src: imageUrl }).run()
    }
  } catch (error) {
    console.error('Image upload failed:', error)
    alert('Failed to upload image')
  }

  // Clear input
  event.target.value = ''
}

watch(() => props.modelValue, (newValue) => {
  const isSame = editor.value?.getHTML() === newValue
  if (!isSame) {
    editor.value?.commands.setContent(newValue, false)
  }
})

onBeforeUnmount(() => {
  editor.value?.destroy()
})
</script>

<style scoped>
.is-active {
  background-color: #e2e8f0; /* bg-gray-200 */
  color: #1a202c;
  font-weight: bold;
}

/* White background for Tiptap content */
.tiptap-content :deep(.ProseMirror) {
  min-height: 400px;
  padding: 1rem;
  background-color: white;
  color: #1a202c; /* gray-900 */
  outline: none;
}

.tiptap-content :deep(.ProseMirror):focus {
  outline: none;
  background-color: white;
}

/* Style headings */
.tiptap-content :deep(.ProseMirror h1) {
  color: #1a202c;
  font-size: 2rem;
  font-weight: bold;
  margin-top: 1rem;
  margin-bottom: 0.5rem;
}

.tiptap-content :deep(.ProseMirror h2) {
  color: #1a202c;
  font-size: 1.5rem;
  font-weight: bold;
  margin-top: 0.75rem;
  margin-bottom: 0.5rem;
}

.tiptap-content :deep(.ProseMirror h3) {
  color: #1a202c;
  font-size: 1.25rem;
  font-weight: bold;
  margin-top: 0.5rem;
  margin-bottom: 0.5rem;
}

/* Style lists */
.tiptap-content :deep(.ProseMirror ul),
.tiptap-content :deep(.ProseMirror ol) {
  padding-left: 1.5rem;
  color: #1a202c;
}

.tiptap-content :deep(.ProseMirror p) {
  color: #1a202c;
  margin: 0.5rem 0;
}

/* Placeholder */
.tiptap-content :deep(.ProseMirror p.is-editor-empty:first-child::before) {
  color: #9ca3af; /* gray-400 */
  content: "Nhập nội dung bài viết...";
  float: left;
  height: 0;
  pointer-events: none;
}
</style>
