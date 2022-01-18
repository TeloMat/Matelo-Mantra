<template>
  <Background />
  <MenuBar />
  <div class="wrapper">
    <div class="panel-title"><h1>Music</h1></div>
    <div class="recycler-view" v-if="isFetching == false">
      <AlbumVIew v-for="album in albums" :key="album.id" :album="album" />
    </div>
  </div>
</template>

<script>
import Background from "@/components/Background";
import AlbumVIew from "@/components/Musician/MusicAlbumVIew";
import MenuBar from "@/components/MenuBar";
export default {
  name: "Musician",
  components: { MenuBar, AlbumVIew, Background },
  data() {
    return {
      albums: [],
      isFetching: true,
    };
  },
  methods: {
    async fetchAlbums() {
      const res = await fetch(
        process.env.VUE_APP_API + "/api/music/Albums/list/"
      );

      return await res.json();
    },
  },
  async created() {
    this.albums = await this.fetchAlbums();
    this.albums.forEach((album) => {
      album.songs.forEach((song) => {
        song.seconds = parseInt(song.track_duration) % 60;
        song.mins = (parseInt(song.track_duration) - song.seconds) / 60;
      });
    });

    this.isFetching = false;
  },
};
</script>



<style scoped>
@media only screen and (max-width: 600px) {
  .panel-title {
    margin-top: 25vh;
  }
  .panel-title h1 {
    font-size: 90px;
  }
}
</style>