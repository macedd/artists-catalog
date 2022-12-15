<script setup lang="ts">
</script>

<template>
  <!-- Logo and Search Section Start -->
  <div class="container mx-auto my-4 md:my-6 flex flex-col md:flex-row items-center justify-between">
    <!-- Logo -->
    <div class="mx-auto md:mx-0">
      <router-link :to="{ name: 'home' }">
        <img class="w-64" src="@/assets/images/logo-1.png" alt="logo" />
      </router-link>
    </div>
    <!-- Search box -->
    <!-- <div class="flex flex-col mt-4 md:mt-0">
      <div
        class="flex items-center justify-between rounded-full border-[3px] border-black py-2 px-4">
        <input
          class="mr-2 text-sm font-medium uppercase text-gray-500 outline-none"
          placeholder="Estilo nome do artista trecho da obra" />
        <img
          class="h-8 w-8"
          src="@/assets/images/header-search.png"
          alt="search" />
      </div>
    </div> -->
  </div>
  <!-- Logo and Search Section End -->
</template>

<style scoped>
</style>
