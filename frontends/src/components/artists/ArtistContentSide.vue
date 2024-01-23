<script setup lang="ts">
import type { Artist } from '../../stores/types';

const props = defineProps<{
  artist: Artist;
}>();

function hasContact(): Boolean {
  const artist = props.artist
  const contacts = [artist.facebook, artist.instagram,
                    artist.whatsapp, artist.youtube,
                    artist.website]
  return contacts.some(c=>!!c)
}
</script>

<template>
  <!-- Artist Detail Side Section Start -->
  <div class="md:w-2/5 px-4">
    <div class="">
      <!-- Artist Photo -->
      <div class="relative z-10 mx-auto w-1/2 md:w-[100%] -mb-32 sm:-mb-40">
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
      
      <!-- Artist Information -->
      <div class="z-0">
        <!-- Rotated Stroke -->
        <div class="-rotate-1 rounded-3xl border-2 border-[rgba(199,64,5,0.85)] p-4 py-2">
          <div class="rotate-1 rounded-3xl bg-[#CFCDCD]">
            <div class="px-4 pt-32 pb-4 sm:pt-40">
              <!-- Start Name -->
              <dl class="mb-4 mt-2 md:hidden">
                <dt class="font-medium text-lg uppercase">
                  Nome
                </dt>
                <dd class="text-base text-gray-600">
                  {{ artist.name }}
                </dd>
              </dl>
              <!-- Start Birth -->
              <dl class="mb-4 mt-2">
                <dt class="font-medium text-lg uppercase">
                  Nascimento - Cidade
                </dt>
                <dd class="text-base text-gray-600">
                  <span v-if="artist.birth_date">
                    {{ artist.birth_date.toLocaleDateString('pt-BR') }} - 
                  </span>
                  {{ artist.birth_city }}
                </dd>
              </dl>
              <!-- Start Kinship -->
              <dl class="mb-4"
                v-if="artist.artistic_kinship">
                <dt class="font-medium text-lg uppercase">
                  Parentesco Artístico
                </dt>
                <dd class="text-base text-gray-600"
                  v-for='(item, i) in artist.artistic_kinship.split("\n")'
                  :key="i">
                  {{ item }}
                </dd>
              </dl>
              <!-- Start Affiliations -->
              <dl class="mb-4"
                v-if="artist.groups_affiliation">
                <dt class="font-medium text-lg uppercase">
                  Grupos/Filiações
                </dt>
                <dd class="text-base text-gray-600"
                  v-for='(item, i) in artist.groups_affiliation.split("\n")'
                  :key="i">
                  {{ item }}
                </dd>
              </dl>
              <!-- Start Works -->
              <dl class="mb-4"
                v-if="artist.works">
                <dt class="font-medium text-lg uppercase">
                  Obras
                </dt>
                <dd class="text-base text-gray-600"
                  v-for='(item, i) in artist.works.split("\n")'
                  :key="i">
                  {{ item }}
                </dd>
              </dl>
              <!-- Start Contact -->
              <dl class="mb-4"
                v-if="hasContact()">
                <dt class="font-medium text-lg uppercase">
                  Contato
                </dt>
                <dd class="text-base text-gray-600">
                  <a :href="artist.website"
                    target="_blank">
                    {{ artist.website.replace(/https?:\/\//, '') }}
                  </a>
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
  </div>
  <!-- Artist Detail Side Section End -->
</template>