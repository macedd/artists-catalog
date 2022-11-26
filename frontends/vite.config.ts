import { fileURLToPath, URL } from "node:url";

import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import vueJsx from "@vitejs/plugin-vue-jsx";

const { resolve } = require('path');

// https://vitejs.dev/config/

export default defineConfig(({ command, mode }) => {
  return {
    plugins: [vue(), vueJsx()],
    resolve: {
      alias: {
        "@": fileURLToPath(new URL("./src", import.meta.url)),
      },
    },
    build: {
      manifest: true,
      // outDir: '../static/dist',
      emptyOutDir: true,
      rollupOptions: {
        input: {
          main: resolve(__dirname, 'src/main.ts')
        },
      }
    },
    base: (process.env.NODE_ENV == 'production') ? '/static/' : '',
  }
});
