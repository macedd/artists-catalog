<script setup lang="ts">
import type { Artist } from '../stores/types';

defineProps<{
  artist: Artist;
}>();

</script>

<template>
  <div class="artist-detail">
    <h1 class="text-3xl font-bold underline">
      Hello world! {{ artist.name }}
    </h1>
  </div>
</template>

<style scoped>
</style>
