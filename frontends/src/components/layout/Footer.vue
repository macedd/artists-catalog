<script setup lang="ts">
</script>

<template>
<footer class="p-4 bg-[#212121] md:px-6 md:py-8">
  <div class="container mx-auto">
    <div class="sm:flex sm:items-center sm:justify-between">
      <!-- Logo -->
      <a class="flex items-center mb-4 sm:mb-0">
          <img src="@/assets/images/artejucana-UFU.png"
            class="mr-3 h-8"
            alt="Artejucana e UFU" />
      </a>

      <!-- Social icons -->
      <div
        class="mb-2 flex items-center rounded-full border-2 border-white py-1 px-16">
        <span class="mr-2 font-medium text-white">SIGA</span>

        <a href="https://www.facebook.com/ArtejucanA-105285695477540"
          target="_blank">
          <img
            class="mr-2 h-8 w-8"
            src="@/assets/images/facebook.png"
            alt="Facebook" />
        </a>
        <a href="https://www.instagram.com/artejucana/"
          target="_blank">
          <img class="mr-2 h-8 w-8"
            src="@/assets/images/instagram.png"
            alt="Instagram" />
        </a>
        <a href="https://wa.me/5534996664244"
          target="_blank">
          <img
            class="mr-2 h-8 w-8"
            src="@/assets/images/whatsapp.png"
            alt="Whatsapp" />
        </a>
        <a href="https://www.youtube.com/@ArtejucanA/videos"
          target="_blank">
          <img class="h-8 w-8"
            src="@/assets/images/youtube.png"
            alt="Youtube" />
        </a>
      </div>

      <!-- Menu -->
      <ul class="flex flex-wrap items-center mb-6 uppercase text-sm text-white sm:mb-0 dark:text-gray-400">
          <li>
              <a href="#" class="mr-4 hover:underline md:mr-6 ">Sobre Nós</a>
          </li>
          <li>
              <a href="#" class="mr-4 hover:underline md:mr-6">Contato</a>
          </li>
      </ul>
    </div>
  </div>
  <hr class="my-6 border-gray-700 sm:mx-auto lg:my-8" />
  <span class="block text-sm sm:text-center text-gray-400">© 2022 <a href="https://flowbite.com/" class="hover:underline">
    Artejucana™</a>. All Rights Reserved.</span>
</footer>
</template>

<style scoped>
</style>
