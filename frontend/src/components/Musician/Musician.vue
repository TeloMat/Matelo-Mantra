<template>
  <Background/>
  <MenuBar/>
  <div class="wrapper">
    <div class="panel-title"><h1>Music</h1></div>
    <div class="recycler-view">
    <AlbumVIew :key="album.id" v-for="album in albums" :album="album"/>

    </div>
  </div>
</template>

<script>
import Background from "@/components/Background";
import AlbumVIew from "@/components/Musician/MusicAlbumVIew";
import MenuBar from "@/components/MenuBar";
export default {
  name: "Musician",
  components: {MenuBar, AlbumVIew, Background},
  data(){
    return {
      albums: []
    }
  },
  methods:{
    async fetchAlbums(){
      const res = await fetch('http://127.0.0.1:8000/api/music/list/')
      const data = await res.json()
      return data
    }
  },
  async created() {
    this.albums = await this.fetchAlbums()
    console.log(this.albums)
  }
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