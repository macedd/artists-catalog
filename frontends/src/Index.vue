<script setup lang="ts">
import { RouterLink, RouterView } from "vue-router";
import HomePlaceholder from './views/HomePlaceholder.vue';
import Header from './components/layout/Header.vue'
</script>

<template>
  <Header />
  <div class="container px-4 h-screen">
    <Suspense>
      <RouterView />
    </Suspense>
  </div>
</template>

<style scoped>
</style>
