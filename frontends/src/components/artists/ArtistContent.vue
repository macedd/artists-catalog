<script setup lang="ts">
import type { Artist } from '../../stores/types';

defineProps<{
  artist: Artist;
}>();
</script>

<template>
  <div class="md:flex md:justify-between">
    <!-- Artist Detail Side Section Start -->
    <div class="ml-2 md:ml-10 md:w-2/5">
      <div class="w-11/12 lg:w-3/4">
        <!-- Artist Photo -->
        <div class="inline-block w-1/2 md:block md:w-[100%]">
          <div>
            <img
              :src="artist.photo_thumbnail"
              :alt="artist.name"
              v-if="artist.photo_thumbnail"
              class="rounded-full border-[6px] border-[rgba(199,64,5,0.85)] drop-shadow-[-3.5px_3.5px_0px_#02090B] md:border-[10px] md:drop-shadow-[-5.54px_5.5px_0px_#02090B]"
            />
            <img
              class="rounded-full border-[6px] border-[rgba(199,64,5,0.85)] drop-shadow-[-3.5px_3.5px_0px_#02090B] md:border-[10px] md:drop-shadow-[-5.54px_5.5px_0px_#02090B]"
              alt="Artejucana"
              v-else
              src="@/assets/images/logo-1.png" />
          </div>
        </div>
        <!-- Artist Information -->
        <div
          class="relative bottom-40 -z-10 ml-5 mt-8 inline-block w-full -rotate-1 rounded-3xl border-2 border-[rgba(199,64,5,0.85)] px-4 pb-4 sm:mx-5 sm:ml-0 sm:mt-0 md:top-auto md:right-auto md:block"
        >
          <!-- Rotated Stroke -->
          <div class="rotate-1 rounded-3xl bg-[#CFCDCD] px-4 pt-32 pb-4 sm:pt-40">
            <div>
              <!-- Start Birth -->
              <dl class="mb-4 mt-2">
                <dt class="text-base font-medium md:text-lg">
                  NASCIMENTO - CIDADE
                </dt>
                <dd class="text-xs font-medium text-gray-600 md:text-sm">
                  <span v-if="artist.birth_date">
                    {{ artist.birth_date.toLocaleDateString('pt-BR') }} - 
                  </span>
                  {{ artist.birth_city }}
                </dd>
              </dl>
              <!-- Start Kinship -->
              <dl class="mb-4"
                v-if="artist.artistic_kinship">
                <dt class="text-base font-medium md:text-lg">
                  PARENTESCO ARTISTICO
                </dt>
                <dd class="text-xs font-medium text-gray-600 md:text-sm"
                  v-for='(item, i) in artist.artistic_kinship.split("\n")'
                  :key="i">
                  {{ item }}
                </dd>
              </dl>
            </div>
            <div>
              <!-- Start Affiliations -->
              <dl class="mb-4"
                v-if="artist.groups_affiliation">
                <dt class="text-base font-medium md:text-lg">
                  GRUPOS/FILIACOES
                </dt>
                <dd class="text-xs font-medium text-gray-600 md:text-sm"
                  v-for='(item, i) in artist.groups_affiliation.split("\n")'
                  :key="i">
                  {{ item }}
                </dd>
              </dl>
              <!-- Start Works -->
              <dl class="mb-4"
                v-if="artist.works">
                <dt class="text-base font-medium md:text-lg">
                  OBRAS
                </dt>
                <dd class="text-xs font-medium text-gray-600 md:text-sm"
                  v-for='(item, i) in artist.works.split("\n")'
                  :key="i">
                  {{ item }}
                </dd>
              </dl>
            </div>
            <div>
              <!-- Start Contact -->
              <dl class="mb-4">
                <dt class="text-base font-medium md:text-lg">
                  CONTATO
                </dt>
                <dd class="text-xs font-medium text-gray-600 md:text-sm">
                  {{ artist.website }}
                </dd>
              </dl>
              <div class="flex">
                <a :href="artist.facebook"
                  target="_blank"
                  v-if="artist.facebook">
                  <img
                    class="h-10 w-10"
                    src="@/assets/images/facebook.png"
                    alt="Facebook" />
                </a>
                <a :href="artist.instagram"
                  target="_blank"
                  v-if="artist.instagram">
                  <img class="h-10 w-10"
                    src="@/assets/images/instagram.png"
                    alt="Instagram" />
                </a>
                <a :href="artist.whatsapp"
                  target="_blank"
                  v-if="artist.whatsapp">
                  <img
                    class="h-10 w-10"
                    src="@/assets/images/whatsapp.png"
                    alt="Whatsapp" />
                </a>
                <a :href="artist.youtube"
                  target="_blank"
                  v-if="artist.youtube">
                  <img class="h-10 w-10"
                    src="@/assets/images/youtube.png"
                    alt="Youtube" />
                </a>
              </div>
              <!-- End Contact -->
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- Artist Detail Side Section End -->

    <!-- Content Detail Right Section Start -->
    <div class="relative bottom-28 md:static md:w-3/5">
      <div class="ml-4 w-11/12 md:pr-[20px]">
        <div class="md:mt-8">
          <!-- Artist Name -->
          <p class="mb-2 text-xl font-bold uppercase text-[#C74005] md:text-3xl">
            {{ artist.name }}
          </p>
          <!-- Artist Biography -->
          <p class="text-sm font-bold uppercase md:text-xl">
            {{ artist.biography }}
          </p>
        </div>

        <!-- Categories -->
        <ul class="my-4 flex flex-wrap">
          <li class="mr-4 text-sm font-bold uppercase md:text-lg"
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
    <!-- Content Detail Right Section End -->
  </div>
</template>