<script setup lang="ts">
import { RouterLink, RouterView } from "vue-router";
import HomePlaceholder from './views/HomePlaceholder.vue';
import Header from './components/layout/Header.vue'
import Footer from './components/layout/Footer.vue'
</script>

<template>
<div>
  <!-- Layout Header -->
  <Header />
  <div class="container mx-auto my-4 md:my-8">
    <Suspense>
      <RouterView v-slot="{ Component }">
        <keep-alive include="HomeView,">
          <component
            :is="Component"
            :key="$route.fullPath">
          </component>
        </keep-alive>
      </RouterView>
    </Suspense>
  </div>
  <!-- Layout Footer -->
  <Footer />
</div>
</template>

<style scoped>
</style>
