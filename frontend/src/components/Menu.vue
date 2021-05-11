<template>
  <div class="title">Matelo Mantra</div>
  <div class="grid_container">
    <div class="grid_background"><img src="../assets/background4.jpg" alt="Error loading img"> </div>
    <div class="grid_content">
      <div id="musician" class="grid_content_item"><img src="../assets/music.jpg" alt="Error loading img"> <div class="grid_content_item_text">Musician</div></div>
      <div id="traveler" class="grid_content_item"><img src="../assets/travel.jpg" alt="Error loading img"><div class="grid_content_item_text"> Traveler</div></div>
      <div id="writer" class="grid_content_item"><img src="../assets/writer.jpg" alt="Error loading img"><div class="grid_content_item_text">Writer</div></div>
    </div>

  </div>
</template>

<script>
export default {
  name: "Menu"
}
</script>

<style scoped>
  .title{
    font-size:70px;
    font-family: 'Brush Script MT';
    margin: 20px 30px;
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
    z-index: -1;
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
  }


  .grid_content_item img{
    min-width: 100%;
    max-width: none;
    height: 100%;
    margin: 0 -140%;
    transition: transform .2s; /* Animation */
  }
  .grid_content_item img:hover{
    transform: scale(1.5);

  }




  .grid_content_item_text{
    display: inline-block;
    position: relative;
    color: white;
    mix-blend-mode: difference;
    font-size: 25px;
    width: 100%;
    top: -65%;
    text-align: center;
    padding: 20% 20%;

  }


</style>