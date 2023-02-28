<script setup lang="ts">
import { onActivated } from "@vue/runtime-core";
import { useHead } from '@vueuse/head'

import HomeArticles from "../components/home/HomeArticles.vue";
import HomeCategories from "../components/home/HomeCategories.vue";

// onActivated(() => console.log('HomeView Activated'))

useHead({
  title: 'ArtejucanA - Unidos pela Cultura de Ituiutaba!',
  meta: [
    {
      name: 'description',
      content: 'Coletivo para divulgação de artistas e eventos na cidade de Ituiutaba, MG.',
    },
  ],
});

</script>

<template>
  <main>
    <HomeArticles />
    <HomeCategories />
  </main>
</template>
