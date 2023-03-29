<script setup lang="ts">
// import { ref, computed } from "vue";

import type { ArtistPortfolio } from '../../stores/types';

// Properties
const props = defineProps<{
  item: ArtistPortfolio;
}>();
</script>

<template>
    <div class="mx-3 mt-3 text-center">
        <img :alt="item.title"
            class="aspect-square object-cover"
            :src="item.thumbnail"
            v-if="item.thumbnail" />
        <img :alt="item.title"
            class="aspect-square object-contain"
            src="@/assets/images/logo-1.png"
            v-else />
        <!-- <h4 class="text-lg font-bold uppercase md:text-xl line-clamp-2">
            {{ item.title }}</h4> -->
    </div>
</template>
