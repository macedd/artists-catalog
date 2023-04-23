<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted } from "vue";

import 'vue3-carousel/dist/carousel.css'
import { Carousel, Slide, Pagination, Navigation } from 'vue3-carousel'
import { breakpointsTailwind, useBreakpoints } from '@vueuse/core'

import type { ArtistPortfolio } from '../../stores/types';
import { ArtistPortfolioType } from '../../stores/types';
import PortfolioImage from './PortfolioImage.vue';
import PortfolioGallery from './PortfolioGallery.vue';

// Properties
const props = defineProps<{
  title: string;
  portfolio: ArtistPortfolio[];
}>();

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

// Gallery Modal
const gallery = ref<typeof PortfolioGallery>(null)
function openGallery(index: number) {
  gallery.value.openModal(index);
}
</script>

<template>
  <!-- category -->
  <div class="my-8">
    <h3
      class="bg-[#212121] py-2 px-8 text-xl font-medium uppercase text-white md:text-3xl">
      {{ title }}
    </h3>
    <!-- gallery -->
    <Carousel
      :items-to-show="itemsToShow"
      :items-to-scroll="itemsToShow"
      :transition=500
      :wrap-around="false"
      :key="`carousel-${itemsToShow}`"
      snap-align="start"
      ref="carousel">
      <Slide v-for="(item, index) in portfolio" :key="index"
        class="items-start px-3 pt-3 text-center cursor-pointer"
      >
        <!-- <router-link :to="`p/${item.upload_type}/${item.id}`"
          class=""> -->
        <a :href="item.media"
          @click.prevent="openGallery(index)">
          <PortfolioImage
            :item="item" />
        </a>
        <!-- </router-link> -->
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

    <PortfolioGallery
      :title="title"
      :portfolio="portfolio"
      ref="gallery" />
  </div>
</template>

<style scoped>
</style>