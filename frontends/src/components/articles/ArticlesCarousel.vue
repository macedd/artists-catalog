<script setup lang="ts">
import 'vue3-carousel/dist/carousel.css'
import { Carousel, Slide, Pagination, Navigation } from 'vue3-carousel'
import { ref, computed } from "vue";

import type { Article } from '../../stores/types';


defineProps<{
  articles: [Article];
}>();

let currentSlide = ref(0);

function slideTo(val) {
  currentSlide.value = val
}

function articleUrl(article) {
  return `/news/${article.slug}/`;
}

</script>

<template>
  <main>
    <!-- active slide -->
    <Carousel
      :items-to-show="1"
      :wrap-around="false"
      v-model="currentSlide"
      class="md:w-9/12 mx-auto"
      id="gallery">
      <Slide v-for="article in articles" :key="article.slug">
        <a :href="articleUrl(article)" 
          class="relative bg-center bg-cover bg-indigo-300 aspect-[4/2] w-full"
          :style="{ backgroundImage: `url('${article.image}')` }">
          <p class="absolute w-full text-xl	uppercase font-serif text-left bottom-6 left-0 p-4 bg-white/70">
            {{ article.title }}</p>
        </a>
      </Slide>
    </Carousel>
    <!-- gallery -->
    <Carousel
      :items-to-show="4"
      :wrap-around="true"
      v-model="currentSlide"
      class="md:w-9/12 mx-auto">
      <Slide v-for="(article, index) in articles" :key="article.slug">
        <div class="relative bg-center bg-cover bg-indigo-300 aspect-[5/3] w-full border"
          :style="{ backgroundImage: `url('${article.image}')` }"
          @click="slideTo(index)">
          <p class="absolute w-full text-sm	uppercase font-serif text-left bottom-0 left-0 p-1 truncate bg-white">
            {{ article.title }}</p>
        </div>
      </Slide>
    </Carousel>
  </main>
</template>

<style scoped>
</style>