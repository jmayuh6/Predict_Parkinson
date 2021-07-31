<template>
  <div id="app">

    <BaseNavigationBar/>

    <BaseLayout>

      <router-view/>

    </BaseLayout>

  </div>
</template>

<script>
import BaseNavigationBar from './components/BaseNavigationBar'
import BaseLayout from './components/BaseLayout'

export default {
  components: { BaseNavigationBar, BaseLayout }
}
</script>

<style lang="stylus">
  #app
    font-family 'Avenir', Helvetica, Arial, sans-serif
    -webkit-font-smoothing antialiased
    -moz-osx-font-smoothing grayscale
    color #808080
    background-color #1A1E24
    background-color #2f3a4a
</style>
