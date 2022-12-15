<script setup lang="ts">
import type { Artist } from '../../stores/types';
import ArtistContentSide from './ArtistContentSide.vue';
import ArtistContentBiography from './ArtistContentBiography.vue';

defineProps<{
  artist: Artist;
}>();
</script>

<template>
  <div class="md:flex md:justify-between">
    <ArtistContentSide :artist="artist" />
    <ArtistContentBiography :artist="artist" />
  </div>
</template>