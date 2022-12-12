<script setup lang="ts">
import { onActivated } from "@vue/runtime-core";

import HomeArticles from "../components/home/HomeArticles.vue";
import HomeCategories from "../components/home/HomeCategories.vue";

// onActivated(() => console.log('HomeView Activated'))

</script>

<template>
  <main>
    <HomeArticles />
    <HomeCategories />
  </main>
</template>
