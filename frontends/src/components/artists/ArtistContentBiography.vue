<script setup lang="ts">
import type { Artist } from '../../stores/types';

const props = defineProps<{
  artist: Artist;
}>();

function whatsappEditLink() {
  props.artist.name
  const message = `Olá, gostaria de solicitar as seguintes mudanças no perfil do artista ${props.artist.name} (${window.location.href}):\n`;
  const link = `https://wa.me/5534996664244?text=${message}`;
  return link;
}
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

      <div
        class="py-4">
        <a
          :href="whatsappEditLink()"
          target="_blank"
          class="py-2.5 px-5 mr-2 mb-2 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-4 focus:ring-gray-200"
          title="Acrescentar ou editar informações neste perfil">
          Editar Informações</a>
      </div>
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