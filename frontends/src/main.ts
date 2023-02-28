import { createApp } from "vue";
import { createPinia } from "pinia";
import { createHead } from "@vueuse/head"

import Index from "./Index.vue";
import router from "./router";

import "./index.css";

const app = createApp(Index);

app.use(createPinia());
app.use(router);
app.use(createHead())

app.mount("#app");
