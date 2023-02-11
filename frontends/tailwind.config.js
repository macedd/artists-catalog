/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './index.html',
    './src/*.{jsx,tsx,vue}',
    './src/components/**/*.{jsx,tsx,vue}',
    './src/views/**/*.{jsx,tsx,vue}',
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/line-clamp'),
  ],
}
