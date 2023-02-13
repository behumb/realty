<template>
  <main>
    <div class="relative px-6 lg:px-8 intro-back">
      <div class="mx-auto max-w-2xl py-32 sm:py-48 lg:py-72">
        <div class="text-center">
          <h1 class="text-4xl font-bold tracking-tight text-gray-200 sm:text-6xl">It's a REAL Real Estate</h1>
          <p class="mt-6 text-lg leading-8 text-gray-400">Anim aute id magna aliqua ad ad non deserunt sunt. Qui irure
            qui lorem cupidatat commodo. Elit sunt amet fugiat veniam occaecat fugiat aliqua.</p>

        </div>
      </div>
    </div>
    <Catalog/>
  </main>

</template>

<style lang="sass">
.intro-back
  background: url("../assets/backimage.jpg") no-repeat center center
  background-size: cover
  position: absolute
</style>


<script>
import Catalog from '@/components/Catalog'

export default {
  components: {
    Catalog
  }
}

</script>
