<template>
  <div class="container" v-on:click="display_picture()">

    <img class="container_img" :src="base_url + picture.photo">
    <div class="picture_text">
      <p class="text">{{ picture.caption}}</p>
    </div>
    <router-link :to="{ name: 'Travel_details', params: {id: picture.id}}">
<!--      <div class="picture_button"> Discover this trip </div> -->
    </router-link>

  </div>

</template>

<script>
import $ from 'jquery'
import PictureFullSize from "./PictureFullSize";
import {createApp, defineComponent} from "vue";

export default {
  name: "PictureView",
  components:{
  },
  data(){
    return{
      base_url : process.env.VUE_APP_API
    }
  },
  props:{
    picture: Object
  },
  methods: {
    display_picture: function (){
      let url = this.base_url + this.picture.photo
      const body = document.body
      var previous_picture = document.getElementById("image_container")
      if(document.body.contains(previous_picture)){
          previous_picture.remove()
        }
      const div = document.createElement('div')
      var picture = defineComponent({extends: PictureFullSize,
          data: () => ({
            url : url
          })
        })
      body.appendChild(div)
      createApp(picture).mount(div)
      $('#app').addClass('blurred')

    }
  }
}
</script>

<style scoped>
.container{
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;
  z-index: +1;
  overflow: hidden;
  position: relative;
}
.container:hover .container_img{
  transform: scale(1.2);
  filter: blur(8px);
  -webkit-filter: blur(8px);
}


.container img{
  z-index: -1;
  transition: transform 0.5s, filter 0.5s;
  width: 100%;
  height: 100%;
}
.picture_text{
  padding: 2.5% 6%;
  font-size: 15px;
  visibility: hidden;
  overflow: scroll;
  border-radius: 25px;
  max-width: 90%;
  max-height: 50%;
  z-index: -10;

  color: white;
  text-shadow: white 0px 0px 2px;
  background-color: rgba(129, 116, 116, 0.3);


  margin: -50% 5% 5% 5%;
}

.container:hover .picture_text{
  visibility: visible;
  transform: scale(1);
}
.container:hover .picture_button{
  visibility: visible;
  transform: scale(1);
}
::-webkit-scrollbar-corner{
  background: rgba(0,0,0,0);
}
::-webkit-scrollbar {
    width: 12px;
}
.picture_text p{
  max-height: 85%;
  margin: 5%;

}
.picture_button{
  visibility: hidden;
  width: 40%;
  margin: 5% 27.5%;
  padding: 5% 5%;
  border-radius: 25px;
  color: #1e3136ff;
  font-family: Impact;
  background-color: rgba(255, 255,255,0.5);
  box-shadow: 2px 2px 10px 2px grey;

}
</style>