<template>
  <router-link :to="{ name: 'Music_details', params: {id: album.id}}">
    <div class="album_card">
        <div class="album_title"><p>{{ album.title }}</p></div>
      <div class="album_content">
        <div class="album_details">
        <div class="album_cover"><img v-bind:src="base_url + album.cover" ></div>
        <div class="album_credits">Credits :<br> Artist : {{ album.artist }}</div>
        </div>
        <div class="album_songs">
          <div  class="song" :key="song.id" v-for="song in album.songs">
            <div class="song_number">{{ album.songs.indexOf(song) + 1}}</div>
            <div class="song_text">
              <div class="song_title">{{ song.title }}</div>
              <div class="song_artist"><small>{{ song.artists }}</small></div>
            </div>
            <div class="song_duration">1:22</div>
          </div>
        </div>
      </div>
    </div>
  </router-link>
</template>

<script>

export default {
  name: "AlbumVIew",
  components:{
  },
  data(){
    return{
      base_url : process.env.VUE_APP_API
    }
  },
  props:{
    album: Object
  },
  methods: {

  }
}
</script>

<style scoped>
.album_card{
  background-color: rgba(211, 211, 211, 0.5);
  border-radius: 3vh;
  padding: 4vh 1vw;
  display: block;
  height: 75vh;
  margin: 30px 0;
  overflow: hidden;
  box-shadow: 0px 10px 20px 5px grey;
}

.album_title{
  width: 93%;
  margin: 0 auto;
  border-radius: 25px;
  padding: 15px 20px;
  font-size: 35px;
  background-color: rgba(129, 116, 116, 0.7);

}
.album_title p{
  margin: 0;
  color: black;
}
.album_content{
  display: flex;
  flex-flow: column wrap;
  width: 100%;
  height: 100%;
}
.album_details{
  margin: 2.5% auto;
  width: 40%;
  height: 80%;

}
.album_cover{
  height: 60%;
  width: fit-content;
  max-width: 100%;
  overflow: hidden;
  border-radius: 15px;
  margin-bottom: 10% ;
}
.album_cover img{
  object-fit: cover;
  max-height: 100%;
  margin: 0 -140%;
}
.album_credits{
  padding: 5% 5%;
  margin: 7.5% 0;
  text-align: left;
  width: 90%;
  height: 25%;
  overflow: scroll;
  font-family: Impact;
  border-radius: 25px;
  background-color: rgba(140, 139, 139,0.5);
}

.album_songs{
  margin: 2.5% auto;
  padding: 2.5% 2.5%;
  border-radius: 1vw;
  width: 50%;
  height: 73.5%;
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

  @media only screen and (max-width: 600px) {
    .album_card{
      height: 140vh;
      overflow: scroll;
    }
    .album_title{
      height: fit-content;
      padding: 2% 5%;
      width: 85%;
      margin-top: 2%;
      margin-bottom: 2.5%;
      border-radius: 200px;


    }
    .album_title p{
      font-size: 70px;
    }

    .album_content{
      display: block;
      height: fit-content;
      padding: 0;
      overflow: hidden;

    }
    .album_details{
      display: flex;
      flex-flow: row nowrap;
      justify-content: space-between;
      width: 95%;
      height: 15%;
      overflow: hidden;

    }
    .album_cover{
      width: 60%;
      height: 50%;

    }
    .album_cover img{
      max-height: 100%;
      max-width: 100%;
      margin-bottom: 2.5%;
    }
    .album_credits{
      margin: 0  0;
      width: 25%;
      height: 250px;
      font-size: 25px;
    }
    .album_songs{
      border-radius: 30px;
      width: 90%;
      height: 40vh;
      margin-top: -10%;
      margin-bottom: 0;
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
      font-size: 40px;
      margin: 5px 5px;
    }
    .song_text{
      margin: 5px 5px;
      display: block;
    }
    .song_title{
      font-size: 50px;
    }
    .song_artist{
      font-size: 40px;
    }
    .song_duration{
      font-size: 35px;
    }
  }
</style>