<script setup lang="ts">
</script>

<template>
  <!-- Logo and Search Section Start -->
  <div class="mt-2 flex flex-col justify-between md:flex-row md:items-end">
    <div class="mx-auto md:mx-0">
      <img class="w-64 md:ml-8" src="@/assets/images/logo-1.png" alt="logo" />
    </div>
    <h1 class="mb-4 text-center text-xl font-semibold md:mb-0 md:text-left">
      SOBRE NÓS - CONTATO
    </h1>
    <div class="mr-4 flex flex-col items-center">
      <div
        class="mb-2 flex items-center rounded-full border-2 border-gray-200 py-1 px-16"
      >
        <span class="mr-2 font-medium text-gray-500">SIGA</span>

        <img
          class="mr-2 h-8 w-8"
          src="@/assets/images/facebook.png"
          alt="facebook"
        />
        <img class="mr-2 h-8 w-8" src="@/assets/images/instagram.png" alt="" />
        <img
          class="mr-2 h-8 w-8"
          src="@/assets/images/whatsapp.png"
          alt="whatsapp"
        />
        <img class="h-8 w-8" src="@/assets/images/youtube.png" alt="" />
      </div>
      <div
        class="flex items-center justify-between rounded-full border-[3px] border-black py-2 px-4"
      >
        <input
          class="mr-2 text-sm font-medium uppercase text-gray-500 outline-none"
          placeholder=" Estilo nome do artista trecho da obra"
        />

        <img
          class="h-8 w-8"
          src="@/assets/images/header-search.png"
          alt="search"
        />
      </div>
    </div>
  </div>
  <!-- Logo and Search Section End -->
</template>

<style scoped>
</style>
