<script setup lang="ts">
import { onMounted } from "@vue/runtime-core";
import { useRoute } from "vue-router";

import { useCategoryListStore } from '../../stores/category';
import { useArtistsListStore } from '../../stores/artist';
import CategoryCarousel from '../categories/CategoryCarousel.vue';

const categoriesStore = useCategoryListStore();
const artistsStore = useArtistsListStore();

await Promise.all([
  categoriesStore.load(),
  artistsStore.load()
])

const categories = categoriesStore.categoriesRoot()

</script>

<template>
  <section>
    <div v-if="!!categoriesStore.error?.code"
      class="error" />
    <CategoryCarousel
      v-else-if="categories?.length"
      v-for="category in categories"
      :key="category.slug"
      :category="category" />
  </section>
</template>
