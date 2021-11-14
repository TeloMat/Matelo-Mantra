<template>
  <Background/>
  <Menu-bar/>
  <div class="wrapper">
    <div class="panel-title"><h1>Travels</h1></div>
    <div class="main-container">
      <div class="album_info">

        <div class="album_thumbnail">
          <img v-bind:src="base_url+ album.thumbnail">
        </div>
        <div class="album_text">
          <div class="album_title">
            <p>{{album.title}}</p>
          </div>
          <div class="album_description">
            <p>{{album.description}}</p>
          </div>
        </div>
      </div>

    </div>
     <div class="grid-view">
      <div class="grid_case" v-for="picture in album.pictures" :key="picture.id" ><PictureView :picture="picture"/></div>
    </div>
  </div>
</template>

<script>
import Background from "@/components/Background";
import MenuBar from "@/components/MenuBar";
import PictureView from "@/components/Traveler/PictureView";

export default {
  name: "PicAlbumPage",
  components: {PictureView, MenuBar, Background},
  props: ['id'],
  data(){
    return{
      album:[],
      base_url : process.env.VUE_APP_API
    }
  },
  methods:{
    async fetchData(id){

      const res = await fetch(process.env.VUE_APP_API +"/api/travels/albums/"+ id +"/")

      return await res.json()
    },
  },
  async created() {
      this.album = await this.fetchData(this.$route.params.id)
  }
}
</script>

<style scoped>
.main-container{
  width: 100%;
  height: 100%;
  border-radius: 25px;
  box-shadow: 5px 5px 20px 5px grey;
  background-color: rgba(179, 160, 111, 0.5);
}

.album_info{
  display: flex;
  flex-flow:  column wrap;
  height: 40vh;

}
.album_thumbnail{
  max-width: 45%;
  width: fit-content;
  height: 80%;
  overflow: hidden;
  margin: 2.5% 2.5%;
  box-shadow: 5px 5px 20px 5px grey;
}
.album_thumbnail img{
  max-height: 100%;
  max-width: 100%;
}
.album_text{
  margin: 2.5% 2.5% 5% 2.5%;
  width: 50%;
  height: 70%;
}
.album_text p{
  margin-top: 5px;
  font-size: 24px;
  text-align: center;
}
.album_title{
  padding: 2.5% 0%;
  margin-bottom: 3%;
  border-radius: 25px;
  background-color: rgba(255, 255,255,0.3);
  height: 15%;
  color: #1e3136ff;
  font-size: 25px;
  font-family: Impact;
}
.album_description p{
  text-align: justify;

}

.album_description{
  padding: 2% 5%;
  height: 68%;
  overflow: scroll;
  border-radius: 25px;
  color: #1e3136ff;
  background-color: rgba(255, 255,255,0.3);

}

::-webkit-scrollbar-corner{
  background: rgba(0,0,0,0);
}
::-webkit-scrollbar {
    width: 12px;
}
.grid-view{
  margin: 50px 0;
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