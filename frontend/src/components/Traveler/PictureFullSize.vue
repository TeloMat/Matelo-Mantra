<template>
  <div id="image_perimeter" v-on:click="remove_image"></div>
  <div id="image_container">
    <img id="image_content" v-bind:src="url">
  </div>
</template>

<script>
import $ from 'jquery'

export default {
  name: "PictureFullSize",
  data(){
    return{

    }
  },
  methods: {
    remove_image: function (){
      $('#image_perimeter').remove()
      $('#image_container').remove()
      $('#app').removeClass('blurred')
    }
  },
  created(){
  }
}
</script>

<style scoped>

#image_container{

}




</style>