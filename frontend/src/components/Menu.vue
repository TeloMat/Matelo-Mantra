<template>
  <div class="menu">
    <div class="title"><img src="../assets/Matelo_Mantra_VF.png"></div>
    <div class="grid_container">
      <div class="grid_background"><img src="../assets/background4.jpg" alt="Error loading img"> </div>
      <div class="grid_content">
        <div id="musician" class="grid_content_item"><img src="../assets/music.jpg" alt="Error loading img"> <div class="grid_content_item_text">Musician</div></div>
        <div id="traveler" class="grid_content_item"><img src="../assets/travel.jpg" alt="Error loading img"><div class="grid_content_item_text"> Traveler</div></div>
        <div id="writer" class="grid_content_item"><img src="../assets/writer.jpg" alt="Error loading img"><div class="grid_content_item_text">Writer</div></div>
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
    height: 30vh;
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
    height: 60vh;
    position: relative;
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
    margin : 0;
    display: grid;
    grid-auto-rows: 2fr;
    grid-template-columns: 1fr 1fr 1fr;
    height: 60vh;
  }
  .grid_content_item{
    overflow: hidden;
    position: relative;
    margin:  0% 10%;
    align-content: center;
    border-radius: 10px;
    transition: transform .2s; /* Animation */

  }
  .grid_content_item :hover{
        transform: scale(1.5);

  }
  .grid_content_item:hover .grid_content_item_text{
    transform: scale(1.5);
  }
  .grid_content_item_text:hover .grid_content_item{
    transform: scale(1.5);
  }

  .grid_content_item img{
    min-width: 100%;
    max-width: none;
    height: 100%;
    margin: 0 -140%;
    transition: transform .2s; /* Animation */

  }
  /*.grid_content_item img *:hover{*/
  /*  transform: scale(1.5);*/

  /*}*/




  .grid_content_item_text{
    display: inline-block;
    position: relative;
    color: white;
    mix-blend-mode: difference;
    font-size: 25px;
    width: 100%;
    top: -55%;
    text-align: center;
    padding: 0;
    transition: transform .2s; /* Animation */


  }


</style>