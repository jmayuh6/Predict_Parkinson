<template>
  <div class="base-header-title">
    <h2 v-if="title" class="text-center font-weight-bold"> {{ title }} </h2>
    <h5 v-if="subtitle1" class="text-center text-muted">{{ subtitle1 }}</h5>
    <h5 v-if="subtitle2" class="text-center text-muted">{{ subtitle2 }}</h5>

    <hr class="my-5">
  </div>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      required: false
    },
    subtitle1: {
      type: String,
      required: false
    },
    subtitle2: {
      type: String,
      required: false
    }
  }
}
</script>

<style scoped>

</style>
