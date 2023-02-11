<script setup lang="ts">
</script>

<template>
  <!-- Player Section Start-->
  <div class="bg-[#212121] py-2 text-white">
    <div
      class="container mx-auto md:max-w-2xl flex items-center justify-center overflow-hidden sm:justify-between md:px-0 lg:w-4/5">
      <div
        class="flex flex-col-reverse items-start pl-8 sm:items-center md:flex-row md:justify-between">
        <!-- Controls -->
        <div class="mt-2 flex items-center justify-center">
          <img
            src="@/assets/svgs/rewind.svg"
            class="mr-4 w-4 cursor-pointer md:mr-6"
          />
          <img
            src="@/assets/svgs/pause.svg"
            class="mr-4 w-6 cursor-pointer md:mr-6"
          />
          <img
            src="@/assets/svgs/rewind.svg"
            class="mr-8 w-4 rotate-180 cursor-pointer"
          />
          <img
            src="@/assets/images/speaker.png"
            class="mr-4 w-4 cursor-pointer md:mr-8"
          />
          <img
            src="@/assets/svgs/favourite.svg"
            class="mr-4 w-4 cursor-pointer md:mr-8"
          />
        </div>
        <!-- Display -->
        <div class="ml-4 flex flex-col">
          <p class="pl-8 text-[12px] font-bold">DIDO DAMIAO - NOME DA MúSICA</p>
          <div class="flex items-center">
            <p class="text-[12px] font-semibold">00:18</p>
            <span
              class="mx-2 mt-1 h-[1px] w-56 border border-gray-600 sm:w-60 md:w-40"
            ></span>
            <p class="text-[12px] font-semibold">02:31</p>
          </div>
        </div>
      </div>
      <div
        class="relative top-6 right-28 flex items-center sm:static sm:right-40 sm:pr-8 lg:ml-8 lg:pr-0">
        <img
          src="@/assets/images/shuffle.png"
          class="mr-4 w-5 cursor-pointer md:mr-6"
        />
        <img
          src="@/assets/images/repeat.png"
          class="mr-4 w-5 cursor-pointer md:mr-6"
        />
        <img
          src="@/assets/images/download.png"
          class="mr-4 w-3 cursor-pointer md:mr-6"
        />
        <img src="@/assets/images//playlist.png" class="w-5 cursor-pointer" />
      </div>
      <!-- <p
        class="ml-8 hidden rounded-full border border-white py-1 px-2 text-[12px] lg:block lg:px-8 lg:text-[15px]"
      >
        EDITAR MINHA PLAYLIST
      </p> -->
    </div>
  </div>
  <!-- Player Seection End -->
</template>

<style scoped>
</style>
