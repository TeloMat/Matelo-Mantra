<template>
  <div class="container">
    <div class="container_img">
      <img :src="base_url + album.thumbnail" />
    </div>
    <div class="album_text">
      <p class="text">{{ album.title }}</p>
    </div>
    <router-link :to="{ name: 'Travel_details', params: { id: album.id } }">
      <div class="album_button">Discover this trip</div>
    </router-link>
  </div>
</template>

<script>
export default {
  name: "PictureAlbumView",
  components: {},
  data() {
    return {
      base_url: process.env.VUE_APP_API,
    };
  },
  props: {
    album: Object,
  },
  methods: {},
};
</script>

<style scoped>
.container {
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;
  overflow: hidden;
  position: relative;
}
.container:hover .container_img {
  transform: scale(1.2);
  filter: blur(8px);
  -webkit-filter: blur(8px);
}

.container_img {
  overflow: hidden;
  height: 100%;
}
.container_img img {
  z-index: -1;
  transition: transform 0.5s, filter 0.5s;
  /* width: 100%; */
  height: 100%;
}
.album_text {
  padding: 2.5% 6%;
  font-size: 15px;
  visibility: hidden;
  overflow: scroll;
  border-radius: 25px;
  max-width: 90%;
  max-height: 30%;
  z-index: -10;

  color: white;
  text-shadow: white 0px 0px 2px;
  background-color: rgba(129, 116, 116, 0.3);

  margin: -50% 5% 5% 5%;
}

.container:hover .album_text {
  visibility: visible;
  transform: scale(1);
}
.container:hover .album_button {
  visibility: visible;
  transform: scale(1);
}
::-webkit-scrollbar-corner {
  background: rgba(0, 0, 0, 0);
}
::-webkit-scrollbar {
  width: 12px;
}
.album_text p {
  max-height: 85%;
  margin: 5%;
}
.album_button {
  visibility: hidden;
  width: 40%;
  margin: 5% 27.5%;
  padding: 5% 5%;
  border-radius: 25px;
  color: #1e3136ff;
  font-family: Impact;
  background-color: rgba(255, 255, 255, 0.5);
  box-shadow: 2px 2px 10px 2px grey;
}
</style>