import vueFilePond from 'vue-filepond'

// Import FilePond plugins
import FilePondPluginFileValidateType from 'filepond-plugin-file-validate-type'
import FilePondPluginImagePreview from 'filepond-plugin-image-preview'

// Import FilePond styles
import 'filepond/dist/filepond.min.css'
import 'filepond-plugin-image-preview/dist/filepond-plugin-image-preview.min.css'

export default defineNuxtPlugin((nuxtApp) => {
    // Create FilePond component with plugins
    const FilePond = vueFilePond(
        FilePondPluginFileValidateType,
        FilePondPluginImagePreview
    )

    // Register as global component
    nuxtApp.vueApp.component('file-pond', FilePond)
})
