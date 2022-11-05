<script setup lang="ts">
import { RouterLink, RouterView } from "vue-router";
import HomePlaceholder from './views/HomePlaceholder.vue';
import Header from './components/layout/Header.vue'
import Footer from './components/layout/Footer.vue'
</script>

<template>
<div>
  <Header />
  <div class="container mx-auto my-4 md:my-8">
    <Suspense>
      <RouterView />
    </Suspense>
  </div>
  <Footer />
</div>
</template>

<style scoped>
</style>
