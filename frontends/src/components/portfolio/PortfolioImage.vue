<script setup lang="ts">
// import { ref, computed } from "vue";

import type { ArtistPortfolio } from '../../stores/types';
import { ArtistPortfolioType } from '../../stores/types';
import { isLocalVideo, getCachedVideoCover } from '../../stores/helpers';

// Properties
const props = defineProps<{
  item: ArtistPortfolio;
}>();

if (props.item.upload_type === ArtistPortfolioType.VIDEO && isLocalVideo(props.item.media)) {
    props.item.thumbnail = await getCachedVideoCover(props.item.media);
}
</script>

<template>
    <div class="">
        <img :alt="item.title"
            class="aspect-square object-cover max-w-full"
            :src="item.thumbnail"
            v-if="item.thumbnail" />
        <img :alt="item.title"
            class="aspect-square object-contain max-w-full"
            src="@/assets/images/logo-1.png"
            v-else />
        <!-- <h4 class="text-lg font-bold uppercase md:text-xl break-words line-clamp-2q">
            {{ item.title }}</h4> -->
    </div>
</template>
