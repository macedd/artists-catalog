<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted } from "vue";

import 'vue3-carousel/dist/carousel.css'
import { Carousel, Slide, Pagination, Navigation } from 'vue3-carousel'
import { breakpointsTailwind, useBreakpoints } from '@vueuse/core'

import type { ArtistCategory, Artist } from '../../stores/types';
import { useArtistsListStore } from '../../stores/artist';

// Properties
const props = defineProps<{
  category: ArtistCategory;
}>();

// Store loading artists
const store = useArtistsListStore();
const artists = store.artistsByCategory(props.category.slug)

// Carousel configuration
const carousel = ref<typeof Carousel|null>(null)
let itemsToShow = ref(3);

// Responsive breakpoints
const breakpoints = useBreakpoints(breakpointsTailwind)
function resolveItemsToShow() {
  // breakpoints on md
  if (breakpoints.isGreater('md')) {
    itemsToShow.value = 5
  } else {
    itemsToShow.value = 3
  }
}
// Listen to resize event
onMounted(() => {
  window.addEventListener("resize", resolveItemsToShow);
  resolveItemsToShow();
});
onUnmounted(() => {
  window.removeEventListener("resize", resolveItemsToShow);
});
</script>

<template>
  <!-- category -->
  <div class="my-4 md:my-8">
    <h3
      class="bg-[#212121] py-2 px-8 text-xl mb-2 mt-6 uppercase text-white md:text-3xl">
      {{ category.title }}
    </h3>
    <!-- gallery -->
    <Carousel
      :items-to-show="itemsToShow"
      :items-to-scroll="itemsToShow"
      :transition=500
      :wrap-around="false"
      :mouse-drag="false"
      :key="`carousel-${itemsToShow}`"
      snap-align="start"
      ref="carousel">
      <Slide v-for="(artist, index) in artists" :key="artist.slug"
        class="items-start px-3 pt-3 text-center"
        >
        <router-link :to="`/a/${artist.slug}/`"
          class="max-w-full">
          <img :alt="artist.name"
            class="aspect-square object-cover max-w-full"
            :src="artist.photo_thumbnail"
            v-if="artist.photo_thumbnail" />
          <img alt="Artejucana"
            class="aspect-square object-contain max-w-full"
            v-else
            src="@/assets/images/logo-1.png" />
          <h4 class="text-sm md:text-lg font-bold uppercase md:text-xl break-word line-clamp-2">
            {{ artist.name }}</h4>
          <em class="text-sm md:text-base text-gray-500 md:text-lg break-all line-clamp-2">
            {{ artist.title }}</em>
        </router-link>
      </Slide>

      <!-- navigation -->
      <template #addons="{ slidesCount, currentSlide }">
        <div @click="carousel?.next"
          class="p-4 cursor-pointer absolute top-1/2 -right-4 md:-right-8 -translate-y-1/2"
          v-if="currentSlide < (slidesCount - itemsToShow)">
          <img class="w-10 md:w-14"
            src="@/assets/images/carousel-arrow.png" alt="arrow-right" />
        </div>
        <div @click="carousel?.prev"
          class="p-4 cursor-pointer absolute top-1/2 -left-4 md:-left-8 -translate-y-1/2 rotate-180"
          v-if="currentSlide > 0">
          <img class="w-10 md:w-14"
            src="@/assets/images/carousel-arrow.png" alt="arrow-left" />
        </div>
      </template>
    </Carousel>
  </div>
</template>

<style scoped>
</style>