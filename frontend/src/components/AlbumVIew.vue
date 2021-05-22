<template>
  <div class="album_card">
    <div class="album_title"><p>Music to be murdered by - Side B</p></div>
    <div class="album_content">
      <div class="album_cover"><img src="../assets/album1.jpg"></div>
      <div class="album_credits">Credits :<br> producer : Matelo Mantra <br> Writer : Matelo Mantra</div>
      <div class="album_songs">
        <div class="song">
          <div class="song_number">1</div>
          <div class="song_text">
            <div class="song_title">Alfred - intro</div>
            <div class="song_artist"><small>Matelo mantra</small></div>
          </div>

          <div class="song_duration">1:22</div>
        </div>
        <div class="song">
          <div class="song_number">2</div>
          <div class="song_text">
            <div class="song_title">Alfred - intro</div>
            <div class="song_artist"><small>Matelo mantra</small></div>
          </div>

          <div class="song_duration">1:22</div>
        </div>
        <div class="song">
          <div class="song_number">3</div>
          <div class="song_text">
            <div class="song_title">Alfred - intro</div>
            <div class="song_artist"><small>Matelo mantra</small></div>
          </div>

          <div class="song_duration">1:22</div>
        </div>
        <div class="song">
          <div class="song_number">4</div>
          <div class="song_text">
            <div class="song_title">Alfred - intro</div>
            <div class="song_artist"><small>Matelo mantra</small></div>
          </div>

          <div class="song_duration">1:22</div>
        </div>
        <div class="song">
          <div class="song_number">5</div>
          <div class="song_text">
            <div class="song_title">Alfred - intro</div>
            <div class="song_artist"><small>Matelo mantra</small></div>
          </div>

          <div class="song_duration">1:22</div>
        </div>
        <div class="song">
          <div class="song_number">6</div>
          <div class="song_text">
            <div class="song_title">Alfred - intro</div>
            <div class="song_artist"><small>Matelo mantra</small></div>
          </div>

          <div class="song_duration">1:22</div>
        </div>
        <div class="song">
          <div class="song_number">7</div>
          <div class="song_text">
            <div class="song_title">Alfred - intro</div>
            <div class="song_artist"><small>Matelo mantra</small></div>
          </div>

          <div class="song_duration">1:22</div>
        </div>
        <div class="song">
          <div class="song_number">8</div>
          <div class="song_text">
            <div class="song_title">Alfred - intro</div>
            <div class="song_artist"><small>Matelo mantra</small></div>
          </div>

          <div class="song_duration">1:22</div>
        </div>
        <div class="song">
          <div class="song_number">9</div>
          <div class="song_text">
            <div class="song_title">Alfred - intro</div>
            <div class="song_artist"><small>Matelo mantra</small></div>
          </div>

          <div class="song_duration">1:22</div>
        </div><div class="song">
          <div class="song_number">10</div>
          <div class="song_text">
            <div class="song_title">Alfred - intro</div>
            <div class="song_artist"><small>Matelo mantra</small></div>
          </div>

          <div class="song_duration">1:22</div>
        </div>
<div class="song">
          <div class="song_number">11</div>
          <div class="song_text">
            <div class="song_title">Alfred - intro</div>
            <div class="song_artist"><small>Matelo mantra</small></div>
          </div>

          <div class="song_duration">1:22</div>
        </div>
        <div class="song">
          <div class="song_number">12</div>
          <div class="song_text">
            <div class="song_title">Alfred - intro</div>
            <div class="song_artist"><small>Matelo mantra</small></div>
          </div>

          <div class="song_duration">1:22</div>
        </div>
        <div class="song">
          <div class="song_number">13</div>
          <div class="song_text">
            <div class="song_title">Alfred - intro</div>
            <div class="song_artist"><small>Matelo mantra</small></div>
          </div>

          <div class="song_duration">1:22</div>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
export default {
name: "AlbumVIew"
}
</script>

<style scoped>
.album_card{
  background-color: #D3D3D3;
  border: 2px outset #966F33;
  border-radius: 3vh;
  padding: 1vw 1vw;
  display: block;
  height: 70vh;
  margin: 30px 0;
}
.album_title{
  width: 93%;
  margin: 0 auto;
  border-radius: 1vw;
  border: outset 1px;
  padding: 15px 20px;
  font-size: 35px;
  background-color: #8c8b8b;
}
.album_title p{
  margin: 0;
}
.album_content{
  display: flex;
  flex-flow: column wrap;
  width: 100%;
  height: 100%;
}
.album_cover{
  margin: 1vw 1vw;
  height: 350px;
  width: 350px;
  overflow: hidden;
  border-radius: 1vw;
}
.album_cover img{
  object-fit: cover;
  max-height: 100%;
  margin: 0 -140%;
}
.album_credits{
  padding: 15px 15px;
  margin-top: 1vw;
  margin-bottom: auto;
  margin-left: 1vw;
  text-align: left;
  width: 320px;
  height: auto;
  overflow: scroll;
  border-radius: 1vw;
  border: 2px outset #333333;
  background-color: #dddddd;
}

.album_songs{
  margin: 15px auto;
  padding: 15px 15px;
  border-radius: 1vw;
  width: 50%;
  height: 77%;
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
  margin: 5px 5px;
  display: block;
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