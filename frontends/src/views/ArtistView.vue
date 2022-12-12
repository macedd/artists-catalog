<script setup lang="ts">
import { onMounted } from "@vue/runtime-core";
import { useRoute } from "vue-router";

import { useArtistDetailStore } from '../stores/artist';
import PageNotFoundView from './PageNotFound.vue';
import ArtistContent from '../components/artists/ArtistContent.vue';

// const props = defineProps({
//   foo: { type: String, required: true },
//   bar: Number
// })

const route = useRoute();
let artist_slug: string = route.params.artist as string;

const store = useArtistDetailStore();
await store.load(artist_slug);

</script>

<template>
  <main>
    <PageNotFoundView
      v-if="!!store.error?.code || !store.artist" />
    <ArtistContent v-else
      :artist="store.artist" />
  </main>
</template>
