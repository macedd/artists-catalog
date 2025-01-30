<script setup lang="ts">
import { computed } from 'vue'
import type { Artist, ArtistCategory } from '../../stores/types';
import { LayoutHelpers } from '../../stores/layout';
import CategoryArtistsList from './CategoryArtistsList.vue';

const props = defineProps<{
  category: ArtistCategory;
  artists: Artist[];
}>();

const responsiveItemsCount = LayoutHelpers.carouselItemsToShow()

const popularArtists = computed(() => props.artists.slice(0, responsiveItemsCount.value))
const latestArtists = computed(() => props.artists.slice(responsiveItemsCount.value))
</script>

<template>
  <!-- category -->
  <div class="my-4 md:my-8">
    <h1
      class="bg-[#ed702d] py-2 px-8 mt-8 md:mt-8 -mb-2 md:-mb-4 text-xl font-bold uppercase text-white text-center md:text-3xl">
      Categoria: {{ category.title }}
    </h1>
    <h3
      class="bg-[#212121] py-2 px-8 text-xl mb-2 mt-6 uppercase text-white md:text-3xl">
      Mais clicados
    </h3>
    <CategoryArtistsList :artists="popularArtists" />

    <h3
      class="bg-[#212121] py-2 px-8 text-xl mb-2 mt-6 uppercase text-white md:text-3xl">
      Adicionados recentemente
    </h3>
    <CategoryArtistsList :artists="latestArtists" />
  </div>
</template>