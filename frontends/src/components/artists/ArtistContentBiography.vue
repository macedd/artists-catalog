<script setup lang="ts">
import type { Artist } from '../../stores/types';

const props = defineProps<{
  artist: Artist;
}>();

</script>

<template>
  <!-- Content Biography Start -->
  <div class="mt-8 md:mt-0 md:static md:w-3/5">
    <div class="ml-4 w-11/12">
      <div class="md:mt-8">
        <!-- Artist Name -->
        <h1 class="mb-2 font-bold uppercase text-[#C74005] text-3xl">
          {{ artist.name }}
        </h1>
        <!-- Artist Biography -->
        <p class="text-base whitespace-pre-line text-justify">
          {{ artist.biography }}
        </p>
      </div>

      <!-- Categories -->
      <ul class="my-4 flex flex-wrap">
        <li class="mr-4 font-bold lowercase"
          v-for="category in artist.categories"
          :key="category.slug">
          #{{ category.slug }}
        </li>
      </ul>
    </div>
    <!-- Artist Portfolio -->
    <!-- <div>
      <p class="mb-2 text-xl font-bold uppercase text-[#C74005] md:text-3xl">
        músicas em destaque
      </p>
      <div class="mt-4 pl-2">
        <div class="mb-8 flex items-center">
          <div class="w-[100px]">
            <img
              class="w-16 rounded-lg bg-green-400 p-2"
              src="../public/images/star.png"
              alt="star"
            />
          </div>
          <div class="ml-4">
            <div class="flex items-center">
              <img class="mr-2 w-7" src="../public/images/play.png" alt="play" />
              <p class="font-semibold">Fazendro Amor no Cemitério</p>
            </div>
            <div>
              <img
                class="mt-1 md:w-3/5"
                src="../public/images/wave.png"
                alt="wave"
              />
            </div>
          </div>
        </div>
        <div class="mb-8 flex items-center">
          <div class="w-[100px]">
            <img
              class="w-16 rounded-lg bg-green-400 p-2"
              src="../public/images/star.png"
              alt="star"
            />
          </div>
          <div class="ml-4">
            <div class="flex items-center">
              <img class="mr-2 w-7" src="../public/images/play.png" alt="play" />
              <p class="font-semibold">Fazendro Amor no Cemitério</p>
            </div>
            <div>
              <img
                class="mt-1 md:w-3/5"
                src="../public/images/wave.png"
                alt="wave"
              />
            </div>
          </div>
        </div>
        <div class="mb-8 flex items-center">
          <div class="w-[100px]">
            <img
              class="w-16 rounded-lg bg-green-400 p-2"
              src="../public/images/star.png"
              alt="star"
            />
          </div>
          <div class="ml-4">
            <div class="flex items-center">
              <img class="mr-2 w-7" src="../public/images/play.png" alt="play" />
              <p class="font-semibold">Fazendro Amor no Cemitério</p>
            </div>
            <div>
              <img
                class="mt-1 md:w-3/5"
                src="../public/images/wave.png"
                alt="wave"
              />
            </div>
          </div>
        </div>
        <div class="mb-8 flex items-center">
          <div class="w-[100px]">
            <img
              class="w-16 rounded-lg bg-green-400 p-2"
              src="../public/images/star.png"
              alt="star"
            />
          </div>
          <div class="ml-4">
            <div class="flex items-center">
              <img class="mr-2 w-7" src="../public/images/play.png" alt="play" />
              <p class="font-semibold">Fazendro Amor no Cemitério</p>
            </div>
            <div>
              <img
                class="mt-1 md:w-3/5"
                src="../public/images/wave.png"
                alt="wave"
              />
            </div>
          </div>
        </div>
      </div>
    </div> -->
  </div>
  <!-- Content Biography End -->
</template>