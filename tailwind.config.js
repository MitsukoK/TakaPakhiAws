/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.html", "./node_modules/flowbite/**/*.js","./useraccount/templates/*.html",],
  theme: {
    extend: {},
  },
  plugins: [require("flowbite/plugin")],
};
