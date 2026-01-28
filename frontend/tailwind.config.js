/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./components/**/*.{js,vue,ts}",
    "./layouts/**/*.vue",
    "./pages/**/*.vue",
    "./plugins/**/*.{js,ts}",
    "./app.vue",
    "./error.vue",
  ],
  theme: {
    extend: {
      colors: {
        // Dark Mode Palette
        bg: {
          dark: '#0f1115',
        },
        card: {
          dark: '#161a22',
        },
        primary: {
          DEFAULT: '#4f8cff',
          hover: '#3a7bd5',
        },
        border: {
          dark: '#242b3a',
        },
        text: {
          DEFAULT: '#ffffff',
          muted: '#9ca3af',
        },
        // Existing colors to keep compatibility if needed, but primary overrides
        gray: {
          50: '#F9FAFB',
          100: '#F3F4F6',
          200: '#E5E7EB',
          300: '#D1D5DB',
          400: '#9CA3AF',
          500: '#6B7280',
          600: '#4B5563',
          700: '#374151',
          800: '#1F2937',
          900: '#111827',
          light: '#E5E7EB',
          dark: '#111111',
        },
      },
      fontFamily: {
        sans: ['Inter', 'SF Pro', 'Roboto', 'system-ui', 'sans-serif'],
      },
    },
  },
  safelist: [
    'text-gray-dark',
    'text-gray-light',
    'bg-gray-dark',
    'bg-gray-light',
    'border-gray-dark',
    'border-gray-light',
  ],
  plugins: [],
}




