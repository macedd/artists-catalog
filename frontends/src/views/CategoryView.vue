<script setup lang="ts">
import { onMounted } from "@vue/runtime-core";
import { useRoute } from "vue-router";
import { useHead } from '@vueuse/head'

import { useCategoryListStore } from '../stores/category';
import { useArtistsListStore } from '../stores/artist';

import PageNotFoundView from './PageNotFound.vue';
import CategoryContent from '../components/categories/CategoryContent.vue';

const route = useRoute();
let category_slug: string = route.params.category as string;

const categoryStore = useCategoryListStore();
const artistsStore = useArtistsListStore();

await Promise.all([
  categoryStore.load(),
  artistsStore.load(category_slug)
])

const category = categoryStore.getCategoryBySlug(category_slug)

if (category) {
  useHead({
    title: `${category.title} - ArtejucanA`,
    meta: [
      // {
      //   name: 'description',
      //   content: `${artist.name}, ${artist.title}, natural de ${artist.birth_city}.`,
      // },
    ],
    link: [
      {
        rel: 'canonical',
        href: category.permalink
      }
    ]
  })
}

const artists = artistsStore.artists

</script>

<template>
  <main>
    <PageNotFoundView
      v-if="!!artistsStore.error?.code || !category" />
    <CategoryContent v-else
      :category="category"
      :artists="artists" />
  </main>
</template>
