<template>
  <Background/>
  <MenuBar/>
  <div class="wrapper">
    <div class="album_card">
    <div class="album_title"><p>{{album.title}}</p></div>
    <div class="album_content">
      <div class="album_cover"><img :src="album.cover"></div>
      <div class="album_text">
      <div class="album_credits">Credits :<br>Artist : {{ album.artist }}</div>
      <div class="album_description"><p>
        {{album.description}}
      </p>
      </div>
      </div>
    </div>

    <div class="album_songs">
        <div class="song" :key="song.id" v-for="song in album.songs" >
          <div class="song_number">{{ album.songs.indexOf(song) + 1}}</div>
          <div class="song_text">
            <div class="song_title"><p>{{ song.title }}</p></div>
            <div class="song_artist"><small>{{ song.artists }}</small></div>
          </div>
          <button  v-on:click="play(song.id)">
            Play
          </button>
          <div class="song_duration">1:22</div>
        </div>

        </div>

    </div>
  </div>


</template>

<script>
import Background from "@/components/Background";
import MenuBar from "@/components/MenuBar";
import MusicPlayer from "./MusicPlayer";
import { defineComponent, createApp } from 'vue'
export default {
  name: "MusicPage",
  components: {MenuBar, Background},
  props:['id'],
  data(){
    return{
      album: []
    }
  },
  methods:{
    async fetchData(id){
      const res = await fetch("http://localhost:8000/api/music/Albums/"+ id+ "/")
      return await res.json()
    },
    async fetchSong(id) {
      const res = await fetch("http://localhost:8000/api/music/Albums/songs/" + id + "/")
      return await res.json()
    },
    play: async function (id){
      var previous_player = document.getElementById("player-container")
      if(document.body.contains(previous_player)){
        previous_player.remove()
      }
      var song = await this.fetchSong(id)
      const body = document.body
      var audio_player = defineComponent({extends: MusicPlayer,
        data: () => ({
        song : song,
        cover: this.album.cover
        })
      })
      const div = document.createElement('div');
      div.id = "player-container"
      body.appendChild(div);
      createApp(audio_player).mount(div)

    }
  },
  async created(){
    this.album = await this.fetchData(this.$route.params.id)
  },

}
</script>

<style scoped>
.album_card{
  background-color: rgba(211, 211, 211, 0.5);
  border-radius: 3vh;
  padding: 1vw 1vw;
  display: block;
  height: 150vh;
  margin: 30px 0;
  box-shadow: 0px 10px 20px 5px grey;

}
.album_title{
  width: 90%;
  margin: 0 auto;
  border-radius: 1vw;
  padding: 15px 20px;
  font-size: 35px;
  background-color: rgba(129, 116, 116, 0.7);

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


  @media only screen and (max-width: 600px) {
    .album_card{
      margin-top: 100px;
      height: fit-content;
      display: inline-block;
      width: 90%;

      padding: 5% 2%;
    }

    .album_title{
      height: fit-content;
      width: 80%;
      padding: 5%;
      border-radius: 200px;
    }
    .album_title p{
      font-weight: bold;
      font-size: 50px;
    }
    .album_content{
      flex-flow: row wrap;
      height: 90%;
    }
    .album_text{
      width: 45%;
      height: 50vh;
    }
    .album_credits{
      font-size: 35px;
      width: 100%;
    }
    .album_description {
      width: 100%;

      overflow: scroll;
    }
    .album_description p{
      font-size: 35px;
    }
    .album_cover{
      border-radius: 35px;
      width: auto;
      height: 50vh;
      margin-left: 2.5%;

    }
    .album_songs{
      border-radius: 30px;
      width: 90%;
      height: 80vh;
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