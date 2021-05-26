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
import AlbumVIew from "@/components/MusicAlbumVIew";
import MenuBar from "@/components/MenuBar";
export default {
  name: "Musician",
  components: {MenuBar, AlbumVIew, Background}
}
</script>

<style scoped>



</style>