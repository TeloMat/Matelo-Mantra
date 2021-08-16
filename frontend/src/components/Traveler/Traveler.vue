<template>
  <Background/>
  <MenuBar/>
  <div class="wrapper">
    <div class="panel-title"><h1>Travels</h1></div>
    <div class="grid-view">
      <div v-for="album in albums" :key="album.id" class="grid_case">
        <PictureAlbumView :album="album"/>
      </div>
    </div>
  </div>
</template>

<script>
import Background from "@/components/Background";
import MenuBar from "@/components/MenuBar";
import PictureAlbumView from "@/components/Traveler/PictureAlbumView";


export default {
name: "Traveler",
  components: {PictureAlbumView, MenuBar, Background},
  data(){
    return{albums: []}
  },
  methods:{
    async fetchAlbums(){
      const res = await fetch('http://localhost:8000/api/travels/albums/list/')
      return await res.json()
    }
  },
   async created() {
    this.albums = await this.fetchAlbums()
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
  box-shadow: 10px 10px 10px 5px grey;
  transition: margin 0.5s;
}
.grid_case:hover{
  margin: 0;
}
</style>