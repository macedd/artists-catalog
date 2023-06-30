<script setup lang="ts">
import { onMounted } from "@vue/runtime-core";
import { useRoute } from "vue-router";

import { useCategoryListStore } from '../../stores/category';
import { useArtistsListStore } from '../../stores/artist';
import CategoryCarousel from '../categories/CategoryCarousel.vue';

const categoriesStore = useCategoryListStore();
const artistsStore = useArtistsListStore();

const categories = categoriesStore.categoriesRoot()

</script>

<template>
  <section>
    <div v-if="!!categoriesStore.error?.code"
      class="error" />
    <h2
      class="mb-2 mt-6 font-bold uppercase text-center text-[#C74005] text-3xl">
      Artistas de Ituiutaba</h2>
    <CategoryCarousel
      v-for="category in categories"
      :key="category.slug"
      :category="category" />
  </section>
</template>
