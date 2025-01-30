<script setup lang="ts">
import type { Artist } from '../../stores/types';

const props = defineProps<{
  artists: Artist[];
}>();

console.log(props.artists)

</script>
<template>
    <ol class="flex">
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