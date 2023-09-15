<script setup lang="ts">
import { onMounted } from "@vue/runtime-core";
import { useRoute } from "vue-router";
import { useHead } from '@vueuse/head'

import { useArtistDetailStore } from '../stores/artist';
import PageNotFoundView from './PageNotFound.vue';
import ArtistContent from '../components/artists/ArtistContent.vue';

const route = useRoute();
let artist_slug: string = route.params.artist as string;

const store = useArtistDetailStore();
await store.load(artist_slug);

const artist = store.artist

if (artist) {
  useHead({
    title: `${artist.name}, ${artist.title} - ArtejucanA`,
    meta: [
      // {
      //   name: 'description',
      //   content: `${artist.name}, ${artist.title}, natural de ${artist.birth_city}.`,
      // },
    ],
    link: [
      {
        rel: 'canonical',
        href: artist.permalink
      }
    ]
  })
}


</script>

<template>
  <main>
    <PageNotFoundView
      v-if="!!store.error?.code || !store.artist" />
    <ArtistContent v-else
      :artist="store.artist" />
  </main>
</template>
