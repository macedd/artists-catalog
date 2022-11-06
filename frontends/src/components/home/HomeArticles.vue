<script setup lang="ts">
import { onMounted } from "@vue/runtime-core";
import { useRoute } from "vue-router";

import { useArticleListStore } from '../../stores/article';
import ArticleSlider from '../articles/ArticlesCarousel.vue';

const store = useArticleListStore();
await store.load();

</script>

<template>
  <main>
    <div v-if="!!store.error?.code"
      class="error" />
    <ArticleSlider
      v-else-if="store.articles?.length"
      :articles="store.articles" />
  </main>
</template>
