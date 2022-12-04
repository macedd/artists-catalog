<script setup lang="ts">
import { ref, computed } from "vue";

import 'vue3-carousel/dist/carousel.css'
import { Carousel, Slide, Pagination, Navigation } from 'vue3-carousel'
import { breakpointsTailwind, useBreakpoints } from '@vueuse/core'

import type { ArtistCategory, Artist } from '../../stores/types';
import { useArtistsCategoryStore } from '../../stores/artist';

// Properties
const props = defineProps<{
  category: ArtistCategory;
}>();

// Store loading artists
const store = useArtistsCategoryStore();
await store.load(props.category.slug);

// Carousel configuration
let itemsToShow = 3;
const carousel = ref(null)

// Responsive breakpoints
const breakpoints = useBreakpoints(breakpointsTailwind)
if (breakpoints.isGreater('md')) {
  itemsToShow = 5
}
</script>

<template>
  <!-- category -->
  <div class="my-8">
    <p
      class="bg-[#212121] py-2 px-8 text-xl font-medium uppercase text-white md:text-3xl">
      {{ category.title }}
    </p>
    <!-- gallery -->
    <Carousel
      :items-to-show="itemsToShow"
      :items-to-scroll="itemsToShow"
      transition="500"
      :wrap-around="true"
      ref="carousel">
      <Slide v-for="(artist, index) in store.artists" :key="artist.slug"
        style="align-items: flex-start;"
        >
        <router-link to="#"
          class="mx-3 mt-3 text-center">
          <img alt="pic"
            class="aspect-square object-cover"
            :src="artist.photo"
            v-if="artist.photo" />
          <img alt="pic"
            class="aspect-square object-contain"
            v-else
            src="@/assets/images/logo-1.png" />
          <p class="text-lg font-bold uppercase md:text-xl line-clamp-2">
            {{ artist.name }}</p>
          <p class="font-medium text-gray-500 md:text-lg line-clamp-2">
            {{ artist.title }}</p>
        </router-link>
      </Slide>
      <template #addons>
        <div @click="carousel.next"
          class="p-4 cursor-pointer absolute top-1/2 -right-4 md:-right-8 -translate-y-1/2"
          v-if="store.artists.length > itemsToShow">
          <img class="w-10 md:w-14"
            src="@/assets/images/carousel-arrow.png" alt="arrow-right" />
        </div>
        <div @click="carousel.prev"
          class="p-4 cursor-pointer absolute top-1/2 -left-4 md:-left-8 -translate-y-1/2 rotate-180"
          v-if="store.artists.length > itemsToShow">
          <img class="w-10 md:w-14"
            src="@/assets/images/carousel-arrow.png" alt="arrow-left" />
        </div>
      </template>
    </Carousel>
  </div>
</template>

<style scoped>
</style>