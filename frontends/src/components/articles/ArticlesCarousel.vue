<script setup lang="ts">
import 'vue3-carousel/dist/carousel.css'
import { Carousel, Slide, Pagination, Navigation } from 'vue3-carousel'
import { ref, computed, onMounted, onUnmounted } from "vue";
import { breakpointsTailwind, useBreakpoints } from '@vueuse/core'

import type { Article } from '../../stores/types';


defineProps<{
  articles: [Article];
}>();

// Carousel instance
const gallery = ref<typeof Carousel|null>(null)
let itemsToShow = ref(4);
const breakpoints = useBreakpoints(breakpointsTailwind)
function resolveItemsToShow() {
  // breakpoints on md
  if (breakpoints.isGreater('md')) {
    itemsToShow.value = 4
  } else {
    itemsToShow.value = 2
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


let currentSlide = ref(0);

function slideTo(val: number) {
  currentSlide.value = val
}
function goToArticle(article: Article) {
  window.open(articleUrl(article), '_blank');
}
function articleUrl(article: Article) {
  return `/news/${article.slug}/`;
}
</script>

<template>
  <div>
    <!-- active slide -->
    <Carousel
      :items-to-show="1"
      :wrap-around="false"
      :mouse-drag="false"
      v-model="currentSlide"
      class="md:w-9/12 mx-auto"
      ref="gallery">
      <Slide v-for="article in articles" :key="article.slug">
        <div class="relative cursor-pointer"
          @click="goToArticle(article)">
          <a :href="articleUrl(article)" 
            @click.prevent
            class="block bg-center bg-cover bg-indigo-300 aspect-[4/2] w-full"
            :style="{ backgroundImage: `url('${article.image}')` }"
            :title="article.title">
          </a>
          <p class="w-full text-lg md:text-xl	uppercase font-serif text-left p-2 md:p-4 line-clamp-2">
            {{ article.title }}</p>
        </div>
      </Slide>

      <!-- navigation -->
      <template #addons="{ slidesCount, currentSlide }">
        <div @click="gallery?.next"
          class="p-4 cursor-pointer absolute top-1/2 -right-4 md:-right-8 -translate-y-1/2"
          v-if="currentSlide < (slidesCount - 1)"
          tabindex="0">
          <img class="w-10 md:w-14"
            src="@/assets/images/carousel-arrow.png" alt="arrow-right" />
        </div>
        <div @click="gallery?.prev"
          class="p-4 cursor-pointer absolute top-1/2 -left-4 md:-left-8 -translate-y-1/2 rotate-180"
          v-if="currentSlide > 0"
          tabindex="0">
          <img class="w-10 md:w-14"
            src="@/assets/images/carousel-arrow.png" alt="arrow-left" />
        </div>
      </template>
    </Carousel>
    <!-- gallery -->
    <Carousel
      :items-to-show="itemsToShow"
      :wrap-around="true"
      v-model="currentSlide"
      class="md:w-9/12 mx-auto">
      <Slide v-for="(article, index) in articles" :key="article.slug">
        <div class="relative cursor-pointer"
          @click="slideTo(index)">
          <article class="bg-center bg-cover bg-indigo-300 aspect-[5/3] w-full border"
            :style="{ backgroundImage: `url('${article.image_thumbnail}')` }">
          </article>
          <p class="w-full text-sm	uppercase font-serif text-left bottom-0 left-0 p-1 line-clamp-1 bg-white">
            {{ article.title }}</p>
        </div>
      </Slide>
    </Carousel>
  </div>
</template>

<style scoped>
</style>