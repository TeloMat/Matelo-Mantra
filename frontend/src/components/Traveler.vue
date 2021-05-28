<template>
  <Background/>
  <MenuBar/>
  <div class="wrapper">
    <div class="panel-title"><h1>Travels</h1></div>
    <div class="grid-view">
      <div class="grid_case"><PictureAlbumView/></div>
      <div class="grid_case"><PictureAlbumView/></div>
      <div class="grid_case"><PictureAlbumView/></div>
      <div class="grid_case"><PictureAlbumView/></div>
      <div class="grid_case"><PictureAlbumView/></div>
      <div class="grid_case"><PictureAlbumView/></div>
      <div class="grid_case"><PictureAlbumView/></div>
      <div class="grid_case"><PictureAlbumView/></div>
      <div class="grid_case"><PictureAlbumView/></div>
      <div class="grid_case"><PictureAlbumView/></div>
      <div class="grid_case"><PictureAlbumView/></div>
    </div>
  </div>
</template>

<script>
import Background from "@/components/Background";
import MenuBar from "@/components/MenuBar";
import PictureAlbumView from "@/components/PictureAlbumView";
export default {
name: "Traveler",
  components: {PictureAlbumView, MenuBar, Background},
  methods:{

  }
}
</script>

<style scoped>
.grid-view{
  display: grid;
  width: auto;
  height: fit-content;
  grid-template-columns: 1fr 1fr 1fr ;
  grid-auto-rows: 1fr;
}
.grid_case{
  margin: 2% 2%;
  max-width: 100%;
  height: 33vh;
  border: 2px outset #333333 ;
  box-shadow: 10px 10px 10px 5px grey;
  transition: margin 0.5s;
}
.grid_case:hover{
  margin: 0;
}
</style>