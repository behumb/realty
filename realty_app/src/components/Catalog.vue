<template>
  <div class="houses-section my-20 relative">
    <div class="flex lg:flex-row justify-between flex-col">
      <h1 class="section-headline relative lg:text-4xl text-gray-500 ml-20 text-2xl">Our houses</h1>
      <div>
        <Listbox class="inline-block w-48 houses-sort ml-20 mt-10 lg:ml-0 lg:mr-10 lg:mt-0" as="div" v-model="selected">
          <div class="relative mt-1">
            <ListboxButton
                class="relative w-full cursor-pointer rounded-md border hover:border-green-500 border-gray-300 bg-white py-2 pl-3 pr-10 text-left shadow-sm focus:border-green-500 focus:outline-none focus:ring-1 focus:ring-green-500 sm:text-sm text-base leading-6 text-gray-500 hover:text-gray-900">
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
                  <li @click="orderCatalog(option.value)"
                      :class="[active ? 'text-white bg-green-500' : 'text-gray-900', 'relative cursor-default select-none py-2 pl-3 pr-9']">
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
        <a @click="showFilters = !showFilters"
           class="inline-block ml-20 mt-10 lg:ml-0 lg:mr-10 lg:mt-0 cursor-pointer rounded-md border border-gray-300 bg-white py-2 pl-5 pr-2 px-5 hover:border-green-500 text-left shadow-sm sm:text-sm text-base leading-6 text-gray-500 hover:text-gray-900">
          Filters
          <ChevronUpDownIcon class="inline-block ml-5 h-5 w-5 text-gray-400" aria-hidden="true"/>
        </a>
      </div>
    </div>
    <div class="shadow sm:rounded-md filters flex flex-col items-center" v-show="showFilters">
      <div class="space-y-6 bg-white px-4 py-5 sm:p-6">
        <p>Square</p>
        <div class="flex flex-row">
          <input id="email-address" name="minSquare" type="number" required="" v-model="minSquare"
                 class="relative block mr-7 w-2/5 appearance-none rounded border border-gray-300 px-3 py-2 text-gray-900 placeholder-gray-500 focus:z-10 focus:border-indigo-500 focus:outline-none focus:ring-indigo-500 sm:text-sm"
                 placeholder="Min"/>
          <input id="email-address" name="maxSquare" type="number" required="" v-model="maxSquare"
                 class="relative block w-2/5 appearance-none rounded border border-gray-300 px-3 py-2 text-gray-900 placeholder-gray-500 focus:z-10 focus:border-indigo-500 focus:outline-none focus:ring-indigo-500 sm:text-sm"
                 placeholder="Max"/>
        </div>
        <p>Price</p>
        <div class="flex flex-row">
          <input id="email-address" name="minPrice" type="number" required="" v-model="minPrice"
                 class="relative block mr-7 w-2/5 appearance-none rounded border border-gray-300 px-3 py-2 text-gray-900 placeholder-gray-500 focus:z-10 focus:border-indigo-500 focus:outline-none focus:ring-indigo-500 sm:text-sm"
                 placeholder="Min"/>
          <input id="email-address" name="maxPrice" type="number" required="" v-model="maxPrice"
                 class="relative block w-2/5 appearance-none rounded border border-gray-300 px-3 py-2 text-gray-900 placeholder-gray-500 focus:z-10 focus:border-indigo-500 focus:outline-none focus:ring-indigo-500 sm:text-sm"
                 placeholder="Max"/>
        </div>
        <div class="text-base font-medium text-gray-900" aria-hidden="true">Bedrooms</div>
        <div class="flex flex-row">
          <div class="mt-4 space-y-4 mr-5" v-for="number in [1,2,3,4,5,6,7]" v-bind:key="number">
            <div class="flex items-start">
              <div class="flex h-5 items-center">
                <input name="bedrooms" type="checkbox" :value="number" v-model="bedroomCheck"
                       class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500"/>
              </div>
              <div class="ml-3 text-sm">
                <label for="comments" class="font-medium text-gray-700">{{ number }}</label>
              </div>
            </div>
          </div>
        </div>
        <div class="text-base font-medium text-gray-900" aria-hidden="true">Bathrooms</div>
        <div class="flex flex-row">
          <div class="mt-4 space-y-4 mr-5" v-for="number in [1,2,3,4,5,6,7,8,9]" v-bind:key="number">
            <div class="flex items-start">
              <div class="flex h-5 items-center">
                <input name="bedrooms" type="checkbox" :value="number" v-model="bathroomCheck"
                       class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500"/>
              </div>
              <div class="ml-3 text-sm">
                <label for="comments" class="font-medium text-gray-700">{{ number }}</label>
              </div>
            </div>
          </div>
        </div>
      </div>
        <button @click="filterCatalog()"
                class="rounded-md mb-5 bg-green-500 px-3.5 py-1.5 text-base font-semibold leading-7 text-white shadow-sm hover:bg-green-400 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">
          See available units
        </button>
    </div>
    <div class="houses mt-20 flex flex-col lg:px-20 px-5 gap-y-20 w-5/6 m-auto">
      <p v-if="catalog === []">No results</p>
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
          <p class="text-gray-500 pb-5">Price: {{ house.cost.toLocaleString("de-DE", {style: "currency", currency: "USD"}) }}</p>
          <a class="more-btn text-xs text-green-500 hover:bg-green-500 hover:text-gray-50">More info</a>
        </div>
      </div>
    </div>
  </div>


</template>

<style lang="sass">
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
      bedroomCheck: [],
      bathroomCheck: [],
      showFilters: false,
      minSquare: '',
      maxSquare: '',
      minPrice: '',
      maxPrice: ''
    }
  },
  mounted() {
    this.$store.dispatch('catalog/getAll').then(response => {
      this.catalog = response.data
    })
    this.filterCatalog()
  },
  methods: {
    orderCatalog(value) {
      this.$store.dispatch('catalog/orderByCost', value).then(response => {
        this.catalog = response.data
      })
    },
    filterCatalog() {
      const data = {
        'ordering': this.selected.value,
        'property_type': '',
        'city': '',
        'min_price': this.minPrice,
        'max_price': this.maxPrice,
        'min_square': this.minSquare,
        'max_square': this.maxSquare,
        'bedrooms': this.bedroomCheck,
        'bathrooms': this.bathroomCheck,

      }
      this.$store.dispatch('catalog/filterCatalog', data).then(response => {
        this.catalog = response.data
      })
    }
  }
}

</script>
