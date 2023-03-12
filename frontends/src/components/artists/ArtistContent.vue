<script setup lang="ts">
import type { Artist } from '../../stores/types';
import { ArtistPortfolioType } from '../../stores/types';
import ArtistContentSide from './ArtistContentSide.vue';
import ArtistContentBiography from './ArtistContentBiography.vue';
import PortfolioCarousel from '../portfolio/PortfolioCarousel.vue';
import { useArtistHelpers } from '../../stores/artist';

const props = defineProps<{
  artist: Artist;
}>();

const artistHelpers = useArtistHelpers();

const drawings = artistHelpers.portfolioByType(props.artist, ArtistPortfolioType.DRAWING);
const photos = artistHelpers.portfolioByType(props.artist, ArtistPortfolioType.PHOTO);

</script>

<template>
  <div class="ml-2 md:ml-10 mr-2 md:mr-10">
    <div class="md:flex md:justify-between">
      <ArtistContentSide :artist="artist" />
      <ArtistContentBiography :artist="artist" />
    </div>
    <PortfolioCarousel
      title="Desenhos"
      :portfolio="drawings"
      v-if="drawings.length" />
    <PortfolioCarousel
      title="Fotos"
      :portfolio="photos"
      v-if="photos.length" />
    <router-view></router-view>
  </div>
</template>