<template>
  <Background/>
  <MenuBar/>
  <div class="wrapper">
    <div class="panel-title"><h1>Music</h1></div>
    <div class="recycler-view">
    <AlbumVIew/>
    <AlbumVIew/>

    </div>
  </div>
</template>

<script>
import Background from "@/components/Background";
import AlbumVIew from "@/components/Musician/MusicAlbumVIew";
import MenuBar from "@/components/MenuBar";
export default {
  name: "Musician",
  components: {MenuBar, AlbumVIew, Background}
}
</script>



<style scoped>

  @media only screen and (max-width: 600px) {
  .panel-title{
    margin-top: 25vh;
  }
  .panel-title h1{
    font-size: 90px;

  }
}

</style>