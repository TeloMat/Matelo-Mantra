<template>
  <Background/>
  <Menu-bar/>
  <div class="wrapper">
    <div class="panel-title"><h1>Travels</h1></div>
    <div class="main-container">
      <div class="album_info">

        <div class="album_thumbnail">
          <img src="../assets/album2.jpg">
        </div>
        <div class="album_text">
          <div class="album_title">
            <p>Album title</p>
          </div>
          <div class="album_description">
            <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.</p>
          </div>
        </div>
      </div>

    </div>
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
name: "PicAlbumPage",
  components: {PictureAlbumView, MenuBar, Background}
}
</script>

<style scoped>
.main-container{
  width: 100%;
  height: 100%;
  border: 2px outset #966F33;
  border-radius: 25px;
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
  height: 75%;
  overflow: hidden;
  margin: 2.5% 2.5%;
  box-shadow: 5px 5px 20px 5px grey;
}
.album_thumbnail img{
  max-height: 100%;
  max-width: 100%;
}
.album_text{
  margin: 2.5%;
  max-width: 47.5%
}
.album_text p{
  font-size: 24px;
  text-align: center;
}
.album_title{
  padding: 2% 10%;
  margin-bottom: 2.5%;
  border-radius: 25px;
  background-color: rgba(255, 255,255,0.3);

  color: #1e3136ff;
  font-size: 25px;
  font-family: Impact;
}
.album_description p{
  text-align: justify;

}

.album_description{
  padding: 2% 5%;
  height: 35%;
  margin: 5% 0;
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
  max-width: 33vw;
  height: 33vh;
  border: 2px outset #333333 ;
  box-shadow: 10px 10px 10px 5px grey;
  transition: margin 0.5s;
}
.grid_case:hover{
  margin: 0;
}
</style>