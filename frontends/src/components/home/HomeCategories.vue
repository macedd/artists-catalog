<script setup lang="ts">
import { onMounted } from "@vue/runtime-core";
import { useRoute } from "vue-router";

import { useCategoryListStore } from '../../stores/category';
import CategoryBar from '../categories/CategoryBar.vue';
import CategoryCarousel from '../categories/CategoryCarousel.vue';

const store = useCategoryListStore();
await store.load();

</script>

<template>
  <section>
    <div v-if="!!store.error?.code"
      class="error" />
    <CategoryCarousel
      v-else-if="store.categories?.length"
      v-for="category in store.categories"
      :key="category.slug"
      :category="category" />
  </section>
</template>
