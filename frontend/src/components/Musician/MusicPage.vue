<template>
  <Background/>
  <MenuBar/>
  <div class="wrapper">
    <div class="album_card">
    <div class="album_title"><p>Music to be murdered by - Side B</p></div>
    <div class="album_content">
      <div class="album_cover"><img src="../../assets/album1.jpg"></div>
      <div class="album_text">
      <div class="album_credits">Credits :<br> producer : Matelo Mantra <br> Writer : Matelo Mantra</div>
      <div class="album_description"><p>
        Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
      </p>
      </div>
      </div>
    </div>

    <div class="album_songs">
        <div class="song">
          <div class="song_number">1</div>
          <div class="song_text">
            <div class="song_title"><p>Alfred - intro</p></div>
            <div class="song_artist"><small>Matelo mantra</small></div>
          </div>

          <div class="song_duration">1:22</div>
        </div>
        <div class="song">
          <div class="song_number">2</div>
          <div class="song_text">
            <div class="song_title"><p>Alfred - intro</p></div>
            <div class="song_artist"><small>Matelo mantra</small></div>
          </div>

          <div class="song_duration">1:22</div>
        </div>
        <div class="song">
          <div class="song_number">3</div>
          <div class="song_text">
            <div class="song_title"><p>Alfred - intro</p></div>
            <div class="song_artist"><small>Matelo mantra</small></div>
          </div>

          <div class="song_duration">1:22</div>
        </div>
        <div class="song">
          <div class="song_number">4</div>
          <div class="song_text">
            <div class="song_title"><p>Alfred - intro</p></div>
            <div class="song_artist"><small>Matelo mantra</small></div>
          </div>

          <div class="song_duration">1:22</div>
        </div>
        <div class="song">
          <div class="song_number">5</div>
          <div class="song_text">
            <div class="song_title"><p>Alfred - intro</p></div>
            <div class="song_artist"><small>Matelo mantra</small></div>
          </div>

          <div class="song_duration">1:22</div>
        </div>
        <div class="song">
          <div class="song_number">6</div>
          <div class="song_text">
            <div class="song_title"><p>Alfred - intro</p></div>
            <div class="song_artist"><small>Matelo mantra</small></div>
          </div>

          <div class="song_duration">1:22</div>
        </div>
        <div class="song">
          <div class="song_number">7</div>
          <div class="song_text">
            <div class="song_title"><p>Alfred - intro</p></div>
            <div class="song_artist"><small>Matelo mantra</small></div>
          </div>

          <div class="song_duration">1:22</div>
        </div>
        <div class="song">
          <div class="song_number">8</div>
          <div class="song_text">
            <div class="song_title"><p>Alfred - intro</p></div>
            <div class="song_artist"><small>Matelo mantra</small></div>
          </div>

          <div class="song_duration">1:22</div>
        </div>
        <div class="song">
          <div class="song_number">9</div>
          <div class="song_text">
            <div class="song_title"><p>Alfred - intro</p></div>
            <div class="song_artist"><small>Matelo mantra</small></div>
          </div>

          <div class="song_duration">1:22</div>
        </div><div class="song">
          <div class="song_number">10</div>
          <div class="song_text">
            <div class="song_title"><p>Alfred - intro</p></div>
            <div class="song_artist"><small>Matelo mantra</small></div>
          </div>

          <div class="song_duration">1:22</div>
        </div>
        <div class="song">
          <div class="song_number">11</div>
          <div class="song_text">
            <div class="song_title"><p>Alfred - intro</p></div>
            <div class="song_artist"><small>Matelo mantra</small></div>
          </div>

          <div class="song_duration">1:22</div>
        </div>
        <div class="song">
          <div class="song_number">12</div>
          <div class="song_text">
            <div class="song_title"><p>Alfred - intro</p></div>
            <div class="song_artist"><small>Matelo mantra</small></div>
          </div>

          <div class="song_duration">1:22</div>
        </div>
        <div class="song">
          <div class="song_number">13</div>
          <div class="song_text">
            <div class="song_title"><p>Alfred - intro</p></div>
            <div class="song_artist"><small>Matelo mantra</small></div>
          </div>

          <div class="song_duration">1:22</div>
        </div>

    </div>
  </div>
  </div>

</template>

<script>
import Background from "@/components/Background";
import MenuBar from "@/components/MenuBar";
export default {
  name: "MusicPage",
  components: {MenuBar, Background}
}
</script>

<style scoped>
.album_card{
  background-color: #D3D3D3;
  border: 2px outset #966F33;
  border-radius: 3vh;
  padding: 1vw 1vw;
  display: block;
  height: 150vh;
  margin: 30px 0;
}
.album_title{
  width: 90%;
  margin: 0 auto;
  border-radius: 1vw;
  border: inset 1px #2c7363;
  padding: 15px 20px;
  font-size: 35px;
  background-color: #8c8b8b;
}
.album_title p{
  margin: 0;
}
.album_content{
  margin: 2% 2%;
  display: flex;
  flex-flow: column wrap;
  width: 100%;
  height: 33%;
  gap: 0;
  overflow: auto;
}
.album_cover{
  height: 100%;
  margin: 0 1%;
  width: 45%;
  max-width: 45%;
  overflow: hidden;
  border-radius: 1vw;
}
.album_cover img{
  object-fit: cover;
  max-height: 100%;
  margin: 0 -140%;
}
.album_text{
  margin: 0 1%;
  width: 50%;
  height: 100%;
}
.album_credits{
  padding: 2.5% 2.5%;
  margin-bottom: 2.5%;
  width: 85%;
  text-align: left;
  overflow: scroll;
  height: 30%;
  border-radius: 10px;
  border: 2px outset #333333;
  background-color: #dddddd;
}
.album_description{
  text-align: justify;
  margin-top: 2.5%;
  background-color: #1e3136ff;
  padding: 2.5% 2.5%;
  width: 85%;
  color: white;
  height: auto;
  max-height: 52.5%;
  border: 2px outset #966F33;
  border-radius: 10px;
  overflow: scroll;
}
.album_songs{
  margin: 2.5% 2.5%;
  padding: 2% 2%;
  border-radius: 25px;
  width: 90%;
  height: 55%;
  background-color: #333333;
  color: #dddddd;
  display: block;
  overflow: scroll;
}
.song{
  display: flex;
  width: 100%;
  flex-flow: row nowrap;
  float: left;
  justify-content: space-between;
}
.song_number{
  font-size: 2vw;
  margin: 5px 5px;
}
.song_text{
  width: 70%;
  margin: 5px 5px;
  display: block;
}
.song_artist{
  float: left;
  width: 100%;
}
.song_artist small{
  float: left;

}
.song_title{
  float: left;
  width: 100%;
}
.song_title p{
  margin: 0;
  float: left;
}
.song_duration{
  margin: 10px 10px;
}
::-webkit-scrollbar {
    width: 12px;
}

/*::-webkit-scrollbar-track {*/
/*    !*-webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.3);*!*/
/*    border-radius: 10px;*/
/*}*/

/*::-webkit-scrollbar-thumb {*/
/*    border-radius: 10px;*/
/*    !*-webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.5)*!*/
/*}*/
::-webkit-scrollbar-corner{
  background: rgba(0,0,0,0);
}
</style>