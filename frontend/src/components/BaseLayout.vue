<template>
  <div class="container">
    <div class="p-2">
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MainBlock',
  props: {
    title: {
      type: String,
      required: false
    },
    subtitle: {
      type: String,
      required: false
    }
  }
}
</script>
