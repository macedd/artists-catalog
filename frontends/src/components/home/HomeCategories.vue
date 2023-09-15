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
    <h3
      class="bg-[#ed702d] py-2 px-8 mt-8 md:mt-8 -mb-2 md:-mb-4 text-xl font-bold uppercase text-white text-center md:text-3xl">
      Artistas de Ituiutaba
    </h3>
    <CategoryCarousel
      v-for="category in categories"
      :key="category.slug"
      :category="category" />
  </section>
</template>
