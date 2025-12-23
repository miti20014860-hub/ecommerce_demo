import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'
import path from 'path'

export default defineConfig({
  base: process.env.NODE_ENV === 'production' ? '/static/' : '/',
  plugins: [react(), tailwindcss()],
  server: {
    port: 5173,
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,              // Avoid CORS and Hosting issues
        secure: false,                   // Errors caused by ignoring HTTPS credentials during development
      },
    },
  },
  build: {
    manifest: true,
    outDir: path.resolve(__dirname, '../static/dist'),
    rollupOptions: {
      input: path.resolve(__dirname, 'src/main.tsx'),
    },
  },
})