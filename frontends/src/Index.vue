<script setup lang="ts">
import { RouterLink, RouterView } from "vue-router";
import HomePlaceholder from './views/HomePlaceholder.vue';
import Header from './components/layout/Header.vue'
</script>

<template>
<div>
  <Header />
  <div class="container mx-auto">
    <Suspense>
      <RouterView />
    </Suspense>
  </div>
</div>
</template>

<style scoped>
</style>
