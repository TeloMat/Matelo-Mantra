<template>
  <div class="menu">
    <div class="title">
      <img src="../assets/Matelo_Mantra_VF.png">
    </div>
    <div class="grid_container">
      <div class="grid_content">
        <div class="grid_content_item">
          <router-link :to="{ name: 'Musician'}">
            <img v-bind:src="'http://127.0.0.1:8000/'+ description.musician">
<!--            <img v-else src="../assets/music.jpg" alt="Error loading img">-->
          </router-link>
          <div class="grid_content_item_text" id="musician">Musician</div>
        </div>
        <div class="grid_content_item">
          <router-link :to="{ name: 'Travels'}">
            <img v-bind:src="'http://127.0.0.1:8000/'+ description.traveler">
<!--            <img v-else src="../assets/travel.jpg" alt="Error loading img">-->
          </router-link>
          <div class="grid_content_item_text" id="traveler"> Traveler</div>
        </div>
        <div class="grid_content_item">
          <router-link :to="{ name: 'Writer'}">
            <img v-bind:src="'http://127.0.0.1:8000/'+ description.writer">
<!--            <img v-else src="../assets/writer.jpg" alt="Error loading img">-->
          </router-link>
          <div class="grid_content_item_text" id="writer">Writer</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Menu",
  components:{},
  props:{
    description: Object
  },methods: {

  },
  async created() {
    
  }
}
</script>

<style scoped>
  .menu{
    height: 100vh;
  }

  .title{
    margin: 0px 30px;
  }

  .title img{
    min-width: 100%;
    max-width: none;
    height: 100%;
    margin: 0 -140%;

  }

  .grid_container{
    margin: 0;
    position: relative;
    width: 100%;
  }

  .grid_background{
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    filter: blur(8px);
    /*z-index: -1;*/
    overflow: hidden;
  }

  .grid_background img{
    min-width: 100%;
    max-width: none;
    height: 100%;
    margin: 0 -140%;
  }

  .grid_content{
    width: 100%;
    margin : 0;
    display: grid;
    grid-auto-rows: 2fr;
    grid-template-columns: 1fr 1fr 1fr;
    height: 60vh;
  }

  .grid_content_item{
    overflow: hidden;
    position: relative;
    margin:  0 10%;
    align-content: center;
    border-radius: 10px;
    transition: all 0.5s; /* Animation */
    z-index: 0;
  }

  .grid_content_item:hover{
    transform: scale(1.3);
    z-index: +1;
  }

  .grid_content_item:hover .grid_content_item_text{
    transform: scale(1.3);
  }

  .grid_content_item img{
    /*position: absolute;*/
    min-width: 100%;
    max-width: none;
    height: 100%;
    transition: transform 0.5s; /* Animation */
    margin: 0 -110%;
    left: -30%;
  }

  /*.grid_content_item img *:hover{*/
  /*  transform: scale(1.5);*/

  /*}*/

  .grid_content_item_text{
    display: inline-block;
    position: absolute;
    color: white;
    mix-blend-mode: difference;
    font-size: 35px;
    width: 100%;
    top: 45%;
    right: 0;
    text-align: center;
    padding: 0;
    transition: transform 0.5s;
    /* Animation */
  }

  /*#musician{*/
  /*  margin: 0 -110%;*/
  /*  left: -30%;*/
  /*}*/

  /*#writer{*/
  /*  top: -46%;*/
  /*  left: 10%;*/

  /*!*}*!*/
  /*#traveler{*/
  /*  top: -47%;*/
  /*  left: 10%;*/
  /* }*/
</style>