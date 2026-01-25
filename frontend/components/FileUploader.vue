<template>
  <div class="file-uploader">
    <ClientOnly>
      <file-pond
        ref="pond"
        :name="name"
        :label-idle="labelIdle"
        :allow-multiple="allowMultiple"
        :accepted-file-types="acceptedFileTypes"
        :server="serverConfig"
        :files="myFiles"
        @init="handleFilePondInit"
        @processfile="handleProcessFile"
        @removefile="handleRemoveFile"
      />
    </ClientOnly>
  </div>
</template>

<script setup>
const props = defineProps({
  name: {
    type: String,
    default: 'file'
  },
  labelIdle: {
    type: String,
    default: 'Kéo thả file hoặc <span class="filepond--label-action">Chọn file</span>'
  },
  allowMultiple: {
    type: Boolean,
    default: false
  },
  acceptedFileTypes: {
    type: String,
    default: 'image/jpeg, image/png'
  },
  modelType: {
    type: String,
    default: null
  },
  modelId: {
    type: [String, Number],
    default: null
  },
  type: {
    type: String,
    default: null
  },
  initialFiles: {
      type: Array,
      default: () => []
  }
})

const emit = defineEmits(['uploaded', 'removed', 'update:modelValue'])

const myFiles = ref([])
const uploadedPaths = ref([]) // Track all uploaded file paths
const { token, getApiBase } = useAuth()
const config = useRuntimeConfig()

watch(() => props.initialFiles, (newFiles) => {
    if (newFiles && newFiles.length > 0) {
        // Map URLs to FilePond file objects with type 'local' to trigger server.load
        myFiles.value = newFiles.map(url => ({
            source: url,
            options: {
                type: 'local' // This tells FilePond to use server.load
            }
        }))
        // Initialize uploadedPaths with initial files
        uploadedPaths.value = [...newFiles]
    } else {
        myFiles.value = []
        uploadedPaths.value = []
    }
}, { immediate: true })

const serverConfig = {
  process: {
    url: `${config?.public?.apiBase || 'http://localhost:8000'}/api/upload`,
    method: 'POST',
    headers: {
      Authorization: `Bearer ${token.value}`
    },
    ondata: (formData) => {
        if (props.modelType) formData.append('model_type', props.modelType)
        if (props.modelId) formData.append('model_id', props.modelId)
        if (props.type) formData.append('type', props.type)
        return formData
    },
    onload: (response) => {
        const res = JSON.parse(response)
        if (res.success && res.path) {
            // Add to uploaded paths
            uploadedPaths.value.push(res.path)
            
            // Emit based on allowMultiple prop
            if (props.allowMultiple) {
                emit('uploaded', { paths: [...uploadedPaths.value] })
                emit('update:modelValue', [...uploadedPaths.value])
            } else {
                emit('uploaded', { path: res.path })
                emit('update:modelValue', res.path)
            }
            return res.path
        }
        return null
    },
    onerror: (response) => {
        console.error('Upload error', response)
        return response
    }
  },
  load: (source, load, error, progress, abort) => {
    // Extract clean path from source
    let cleanPath = source
    
    if (typeof source === 'string') {
      // If source is full URL, extract just the path part
      if (source.startsWith('http://') || source.startsWith('https://')) {
        try {
          const url = new URL(source)
          cleanPath = url.pathname // e.g., /storage/uploads/file.jpg
        } catch (e) {
          console.error('Invalid URL:', source)
          error(new Error(`Invalid URL: ${source}`))
          return { abort: () => {} }
        }
      }
      
      // Remove /storage/ prefix
      cleanPath = cleanPath.replace(/^\/storage\//, '').replace(/^\//, '')
      
      // Build API endpoint URL
      const apiBase = config?.public?.apiBase || 'http://localhost:8000'
      const apiUrl = `${apiBase}/api/files/${cleanPath}`
      
      // Validate final URL
      try {
        new URL(apiUrl)
      } catch (e) {
        error(new Error(`Invalid URL: ${apiUrl}`))
        return { abort: () => {} }
      }
      
      // Create abort controller
      const controller = new AbortController()
      
      fetch(apiUrl, { 
        signal: controller.signal,
        headers: {
          'Accept': 'image/*'
        }
        // Remove credentials: 'include' to avoid CORS issue with wildcard
      })
        .then(response => {
          if (!response.ok) {
            throw new Error(`Failed to load image: ${response.status} ${response.statusText}`)
          }
          
          // Check Content-Type
          const contentType = response.headers.get('content-type') || ''
          if (!contentType.startsWith('image/')) {
            return response.text().then(text => {
              throw new Error(`Expected image but got ${contentType}`)
            })
          }
          
          return response.blob()
        })
        .then(blob => {
          if (blob.size === 0) {
            throw new Error('Blob is empty - no image data received')
          }
          
          if (!blob.type.startsWith('image/')) {
            throw new Error(`Blob type is ${blob.type}, expected image/*`)
          }
          
          load(blob)
        })
        .catch(err => {
          if (err.name !== 'AbortError') {
            console.error('Load error:', err)
            error(err)
          }
        })
      
      // Return abort function
      return {
        abort: () => {
          controller.abort()
          abort()
        }
      }
    }
    
    error(new Error('Invalid source'))
    return { abort: () => {} }
  },
  revert: null, // Implement revert/delete if needed
}

const handleFilePondInit = () => {
  console.log('FilePond has initialized')
}

const handleProcessFile = (error, file) => {
    if (error) {
        console.error('Process File Error:', error)
        return
    }
}

const handleRemoveFile = (error, file) => {
    if (error) {
        console.error('Remove File Error:', error)
        return
    }
    
    // Remove from uploadedPaths
    const serverId = file.serverId
    if (serverId) {
        const index = uploadedPaths.value.indexOf(serverId)
        if (index > -1) {
            uploadedPaths.value.splice(index, 1)
        }
    }
    
    // Emit updated paths
    if (props.allowMultiple) {
        emit('removed', { paths: [...uploadedPaths.value] })
        emit('update:modelValue', [...uploadedPaths.value])
    } else {
        emit('removed', null)
        emit('update:modelValue', null)
    }
}
</script>

<style>
/* Override some FilePond styles to match theme if needed */
.filepond--panel-root {
  background-color: #f7fafc;
  border: 1px dashed #cbd5e0;
}
</style>
