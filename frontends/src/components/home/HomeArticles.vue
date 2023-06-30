<script setup lang="ts">
import { useArticleListStore } from '../../stores/article';
import ArticleSlider from '../articles/ArticlesCarousel.vue';

const store = useArticleListStore();

</script>

<template>
  <section>
    <div v-if="!!store.error?.code"
      class="error" />
    <ArticleSlider
      v-else-if="store.articles?.length"
      :articles="store.articles" />
  </section>
</template>
