<template>
  <main>
    <div class="relative px-6 lg:px-8 intro-back">
      <div class="mx-auto max-w-2xl py-32 sm:py-48 lg:py-56">
        <div class="text-center">
          <h1 class="text-4xl font-bold tracking-tight text-gray-200 sm:text-6xl">Data to enrich your online
            business</h1>
          <p class="mt-6 text-lg leading-8 text-gray-400">Anim aute id magna aliqua ad ad non deserunt sunt. Qui irure
            qui lorem cupidatat commodo. Elit sunt amet fugiat veniam occaecat fugiat aliqua.</p>
          <div class="mt-10 flex items-center justify-center gap-x-6">
            <a href="#"
               class="rounded-md bg-green-500 px-3.5 py-1.5 text-base font-semibold leading-7 text-white shadow-sm hover:bg-green-400 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Get
              started</a>
          </div>
        </div>
      </div>
    </div>
    <div class="houses-section my-20 relative">
      <div class="flex lg:flex-row justify-between flex-col">
        <h1 class="section-headline relative lg:text-4xl text-gray-500 ml-20 text-2xl">Our houses</h1>

        <Listbox class="inline-block w-48 houses-sort ml-20 mt-10 lg:ml-0 lg:mr-20 lg:mt-0" as="div" v-model="selected">
          <div class="relative mt-1">
            <ListboxButton
                class="relative w-full cursor-default rounded-md border border-gray-300 bg-white py-2 pl-3 pr-10 text-left shadow-sm focus:border-green-500 focus:outline-none focus:ring-1 focus:ring-green-500 sm:text-sm">
        <span class="flex items-center">
          <span class="ml-3 block truncate">{{ selected.name }}</span>
        </span>
              <span class="pointer-events-none absolute inset-y-0 right-0 ml-3 flex items-center pr-2">
          <ChevronUpDownIcon class="h-5 w-5 text-gray-400" aria-hidden="true"/>
        </span>
            </ListboxButton>

            <transition leave-active-class="transition ease-in duration-100" leave-from-class="opacity-100"
                        leave-to-class="opacity-0">
              <ListboxOptions
                  class="absolute z-10 mt-1 max-h-56 w-full overflow-auto rounded-md bg-white py-1 text-base shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none sm:text-sm">
                <ListboxOption as="template" v-for="option in sortOption" :key="option.id" :value="option"
                               v-slot="{ active, selected }">
                  <li @click="orderCatalog(option.value)" :class="[active ? 'text-white bg-green-500' : 'text-gray-900', 'relative cursor-default select-none py-2 pl-3 pr-9']">
                    <div class="flex items-center">
                      <span :class="[selected ? 'font-semibold' : 'font-normal', 'ml-3 block truncate']">{{
                          option.name
                        }}</span>
                    </div>

                    <span v-if="selected"
                          :class="[active ? 'text-white' : 'text-green-500', 'absolute inset-y-0 right-0 flex items-center pr-4']">
                <CheckIcon class="h-5 w-5" aria-hidden="true"/>
              </span>
                  </li>
                </ListboxOption>
              </ListboxOptions>
            </transition>
          </div>
        </Listbox>
      </div>
      <div class="houses mt-20 flex flex-col lg:px-20 px-5 gap-y-20 w-5/6 m-auto">
        <div v-for="house in catalog" v-bind:key="house.id"
             class="houses__item grid lg:grid-cols-2 grid-cols-1 gap-x-5">
          <div class="house__image-group">
            <img class="house__image" :src="house.get_image">
            <p class="house__name lg:text-lg text-sm font-semibold">{{ house.name }}</p>
          </div>

          <div class="flex flex-col justify-end">
            <p class="house__descr text-gray-400 text-sm lg:w-2/3 py-5">{{
                house.description.substr(0, 400) + '...'
              }}</p>
            <p class="text-gray-500 pb-5">Price: ${{ house.cost }}</p>
            <a class="more-btn text-xs text-green-500 hover:bg-green-500 hover:text-gray-50">More info</a>
          </div>
        </div>
      </div>
    </div>
  </main>

</template>

<style lang="sass">
.intro-back
  background: url("../assets/backimage.jpg") no-repeat center center
  background-size: cover
  position: absolute

.section-headline
  position: relative

  &:before
    content: ''
    height: 25px
    width: 7px
    background-color: theme('colors.green.500')
    display: inline-block
    margin-right: 10px

.house
  &__name
    position: absolute
    top: 0
    left: 0
    display: inline-block
    padding: 10px 42px
    background: #fff

  &__image-group
    position: relative

.more-btn
  display: inline-block
  border: 1px solid theme('colors.green.500')
  max-width: 131px
  padding: 14px 25px
  text-transform: uppercase
  background: transparent
  color: #12c7b8
  line-height: normal
  cursor: pointer
  text-align: center

</style>

<script setup>
import {Listbox, ListboxButton, ListboxLabel, ListboxOption, ListboxOptions} from '@headlessui/vue'
import {CheckIcon, ChevronUpDownIcon} from '@heroicons/vue/20/solid'
</script>

<script>
import { ref } from 'vue'

const sortOption = [
        {
          id: 1,
          name: 'All',
          value: ''
        },
        {
          id: 2,
          name: 'High to low',
          value: '-cost'
        },
        {
          id: 3,
          name: 'Low to high',
          value: 'cost'
        }
      ]

export default {
  data() {
    return {
      catalog: [],
      selected: sortOption[0],
    }
  },
  mounted() {
    this.$store.dispatch('catalog/getAll').then(response => {
      console.log(response.data)
      this.catalog = response.data
    })
  },
  methods: {
    orderCatalog(value) {
      this.$store.dispatch('catalog/orderByCost', value).then(response => {
        this.catalog = response.data
      })
    }
  }
}

</script>