<script setup lang="ts">
import { ref, computed } from "vue";
import { useRouter } from "vue-router";
import 'vue-silentbox/dist/style.css'

import type { ArtistPortfolio } from '../../stores/types';

const props = defineProps<{
  title: string;
  portfolio: ArtistPortfolio[];
}>();

const router = useRouter();

const galleryImages = 
    props.portfolio.map((p) => ({
            src: p.media,
            description: p.title,
        })
    );

const lightbox = ref<unknown>(null)

function openModal(index: number) {
    // const { href } = router.resolve({ name: 'posts-modal' });
    lightbox.value.openOverlay(galleryImages[index], index)
}
function closeModal() {
    // router.go(-1);
    lightbox.value.close()
}

defineExpose({ openModal, closeModal });

</script>

<style lang="css">
a.silentbox-item {
    display: none;
}
</style>

<template>
    <silent-box
        :gallery="galleryImages"
        :lazy-loading="true"
        ref="lightbox" />
</template>