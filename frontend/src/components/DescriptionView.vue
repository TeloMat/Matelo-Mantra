<template>
<div class="description-box">
  <img v-if="description.picture" :src="description.picture">

</div>
</template>

<script>
export default {
  name: "DescriptionView",
  components:{
  },
  props:{
    description : Object
  },
  methods:{

  }
}
</script>

<style scoped>

</style>