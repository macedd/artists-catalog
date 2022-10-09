import { createApp } from "vue";
import { createPinia } from "pinia";

import App from "./App.vue";
import Index from "./Index.vue";
import router from "./router";

import "./index.css";

const app = createApp(Index);

app.use(createPinia());
app.use(router);

app.mount("#app");
