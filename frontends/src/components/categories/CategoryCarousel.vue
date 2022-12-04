<script setup lang="ts">
import 'vue3-carousel/dist/carousel.css'
import { Carousel, Slide, Pagination, Navigation } from 'vue3-carousel'
import { ref, computed } from "vue";

import type { ArtistCategory, Artist } from '../../stores/types';
import { useArtistsCategoryStore } from '../../stores/artist';

const props = defineProps<{
  category: ArtistCategory;
}>();

const store = useArtistsCategoryStore();
await store.load(props.category.slug);

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
      :items-to-show="5"
      :wrap-around="true"
      v-model="currentSlide">
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
    </Carousel>
  </div>
</template>

<style scoped>
</style>