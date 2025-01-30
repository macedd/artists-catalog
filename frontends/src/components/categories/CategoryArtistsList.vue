<script setup lang="ts">
import { computed } from 'vue';
import type { Artist } from '../../stores/types';
import { LayoutHelpers } from '../../stores/layout';

const props = defineProps<{
  artists: Artist[];
}>();

const responsiveItemsCount = LayoutHelpers.carouselItemsToShow()
const gridTemplateColumns = computed(() => {
  return `repeat(${responsiveItemsCount.value}, minmax(0, 1fr))`;
});

</script>
<template>
  <ol :style="{ gridTemplateColumns: gridTemplateColumns }"
    class="grid gap-4">
      <li v-for="(artist, index) in props.artists" :key="artist.slug"
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
      </li>
    </ol>
</template>