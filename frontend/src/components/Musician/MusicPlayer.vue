<template>
  <audio id="audio" :src="song.track" preload="auto"> </audio>

  <div class="player">
    <div class="player_Music_cover"><img :src="cover"></div>
    <div class="player_Music_text">
      <div class="player_Music_name">
        {{song.title}}
      </div>
      <div class="player_Music_artist">
         <small> {{song.artists}}</small>
      </div>
    </div>
    <div class='btns'>
      <div v-on:click="play_pause()" id="play-pause" class="iconfont  icon-play"></div>
      <div id="duration" v-on:click="move_head">
        <div id="progress"></div>
      </div>
      <div class="iconfont next icon-next"></div>
      <div class="iconfont volume icon-next"></div>
      <div id="max_volume" v-on:click="move_head">
        <div id="current_vol"></div>
      </div>
    </div>
  </div>

</template>

<script>
import $ from 'jquery'



//   $('.next').on('click', function(){
//   aud.src = 'another audio source';
// })


export default {
  name: "MusicPlayer",
  data:()=>({

  }),
  methods:{
    getLeft(str) {
      var el = document.getElementById(str)
      return el.getBoundingClientRect().left;
    },
    getRight(str) {
      var el = document.getElementById(str)
      return el.getBoundingClientRect().right;
    },
    getTargetProgress(x){
      var target =  (x - this.getLeft("progress")) /
          (this.getRight("duration") - this.getLeft("progress"))
      return target
    },
    play_pause: function(){
      var aud = $('audio')[0];

      if (aud.paused) {
        aud.play();
        $('#play-pause').removeClass('icon-play');
        $('#play-pause').addClass('icon-stop');
      }
      else {
        aud.pause();
        $('#play-pause').removeClass('icon-stop');
        $('#play-pause').addClass('icon-play');
      }
      $('audio')[0].ontimeupdate = function(){
        $('#progress').css('width', (aud.currentTime / aud.duration) * 100 + '%')
      }

    },
    move_head: function(event){
      var aud = $('audio')[0];
      var target = this.getTargetProgress(event.clientX)
      aud.currentTime = aud.duration * target
      $('#progress').css('width', (aud.currentTime / aud.duration) * 100 + '%')
      console.log(target + "*" + aud.duration)

    },

    /*,
    next : function (){
      var aud = $('audio')[0]
      aud.src = "new source"
    }*/



  },
  async created() {
    var aud = $('audio')[0];
    if (aud.paused) {
        aud.play();
        $('#play-pause').removeClass('icon-play');
        $('#play-pause').addClass('icon-stop');
      }
  }

}
</script>

<style >



  .player{
    width: 100%;
    padding: 15px 15vw 10px 15vw ;
    display: flex;
    background-color: rgba(51, 51, 51, 0.9);
    z-index: +10000;
    box-shadow: 0px 10px 20px 5px #000000;


  }
  .player_Music_text{
    padding: 10px;
  }
  .player_Music_cover{
    margin:0  20px;
    margin-bottom: 10px;
    width:50px;
    height:50px;
    overflow: hidden;
  }
  .player_Music_cover img{
    max-height: 100%;
    max-width: 100%;
  }

  #progress {
    /*position: absolute;*/
    /*height: 5px;*/
    /*left: 0;*/
    /*top: 0;*/
    margin-top: -1px;
    width: 0;
    background-color: #000000;
    height: 7px;
    border-radius: 10px;


  }
  #duration{
    width: 40vw;
    margin: 10px 5vw;
    height: 5px;
    background-color: #8c8b8b;
    border-radius: 10px;
  }
  #duration:hover{
    cursor: pointer;
  }

  .btns {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 16px;
    flex-flow: row nowrap;

  }
  .iconfont:hover{
    cursor: pointer;
  }
  #play-pause{
    height: 25px;
    width: 25px;
    background-size: 25px 25px ;

    background-repeat: no-repeat;
    background-position: center;

  }

  .icon-play{
    background-image: url("../../assets/play-button-arrowhead.png");
  }
  .icon-stop{

    background-image: url("../../assets/pause.png");
  }
  .next{
    padding: 5px;
    height: 25px;
    width: 25px;
    background-size: 25px 25px;
    background-image: url("../../assets/next.png");
    background-repeat: no-repeat;
    background-position: center;

  }



</style>