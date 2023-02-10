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
    <div class="houses-section my-20">
      <h1 class="section-headline text-4xl text-gray-500 ml-20">Our houses</h1>
      <div class="houses mt-20 flex flex-col lg:px-20 px-5 gap-y-20 w-3/4 m-auto">
        <div v-for="house in catalog" v-bind:key="house.id"
             class="houses__item grid lg:grid-cols-2 grid-cols-1 gap-x-5">
          <div class="house__image-group">
            <img class="house__image" :src="house.get_image">
            <p class="house__name text-lg font-semibold">{{house.name}}</p>
          </div>

          <div class="flex flex-col justify-end">
            <p class="house__descr text-gray-400 text-sm lg:w-2/3 py-10">{{house.description}}</p>
            <a class="more-btn text-xs text-green-500">More info</a>
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

//.houses
//  display: flex
//  flex-direction: column
//  width: 70%
//  align-items: center
//  &__item
//    display: flex
//    flex-direction: row
//  &-section
//    padding: 100px 50px !important
//
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


<script>

export default {
  data() {
    return {
      catalog: []
    }
  },
  mounted() {
    this.$store.dispatch('catalog/getAll').then(response => {
      console.log(response.data)
      this.catalog = response.data
    })
  }
}

</script>