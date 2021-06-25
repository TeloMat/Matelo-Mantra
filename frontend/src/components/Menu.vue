<template>
  <div class="menu">
    <div class="title"><img src="../assets/Matelo_Mantra_VF.png"></div>
    <div class="grid_container">
<!--      <div class="grid_background"><img src="../assets/background4.jpg" alt="Error loading img"> </div>-->
      <div class="grid_content">
        <div class="grid_content_item">        <router-link to=music>
<img id="musician" src="../assets/music.jpg" alt="Error loading img"> </router-link><div class="grid_content_item_text">Musician</div></div>
        <div class="grid_content_item"><router-link to=travels> <img src="../assets/travel.jpg" alt="Error loading img"></router-link><div class="grid_content_item_text"> Traveler</div></div>
        <div class="grid_content_item"><router-link to=writer><img src="../assets/writer.jpg" alt="Error loading img"></router-link><div class="grid_content_item_text">Writer</div></div>
      </div>

    </div>
  </div>
</template>

<script>
export default {
  name: "Menu"
}
</script>

<style scoped>
  .menu{
    height: 100vh;
  }

  .title{
    height: 20vh;
    margin: 20px 30px;
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
    transition: transform 0.5s; /* Animation */
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
    position: relative;
    color: white;
    mix-blend-mode: difference;
    font-size: 35px;
    width: 100%;
    top: -55%;
    text-align: center;
    padding: 0;
    transition: transform 0.5s; /* Animation */
  }

  #musician{
    margin: 0 -110%;
    left: -30%;
  }


</style>