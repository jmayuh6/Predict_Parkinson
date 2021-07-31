<template>
  <div id="nav" class="py-4 lead">
    <router-link to="/">Home</router-link>
    |
    <router-link to="/audio">Audio</router-link>
  </div>
</template>

<script>
export default {
  name: 'BaseNavigationBar'
}
</script>

<style lang="stylus">
  #nav
    text-align center
    a
      color #808080
      &:hover
        text-decoration none
        color #F92672 !important
      &.router-link-exact-active
        color #A6E22E
        font-weight bold
        border-bottom 1px solid
</style>
