<template>
  <audio id="audio" :src="base_url + song.track" preload="auto"> </audio>
  <div id="btn_hide_player" class="down" v-on:click="hide_show_player"></div>
  <div id="player">
    <div class="player_Music_cover"><img v-bind:src="base_url + cover"></div>
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
  props:['id'],
  data(){
    return{
      hidden: false,
      base_url: process.env.VUE_APP_API
    }
  },
  async created() {
    var aud = $('audio')[0];
    if (aud.paused) {
        aud.play();
        $('#play-pause').removeClass('icon-play');
        $('#play-pause').addClass('icon-stop');
    }
  },

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
      let aud = $('audio')[0];
      let target = this.getTargetProgress(event.clientX);
      aud.currentTime = aud.duration * target
      $('#progress').css('width', (aud.currentTime / aud.duration) * 100 + '%')
      // console.log(target + "*" + aud.duration)
    },
    /*,
    next : function (){
      var aud = $('audio')[0]
      aud.src = "new source"
    }*/

    hide_show_player(){
      if(this.hidden !== true){
        $('#player-container').css('bottom', '-80px')
        $('#btn_hide_player').removeClass('down')
        $('#btn_hide_player').addClass('up')
        console.log("test")
        this.hidden = true
      }else{
        $('#player-container').css('bottom', '0')
        $('#btn_hide_player').removeClass('up')
        $('#btn_hide_player').addClass('down')
        this.hidden = false
      }
    },
  }

}
</script>

<style >



  #player{
    width: 100%;
    padding: 15px 15vw 10px 15vw ;
    display: flex;
    background-color: rgba(255, 255, 255, 0.2);
    z-index: +10000;
    box-shadow: 0px 10px 20px 5px #000000;

  }
  .player_Music_text{
    padding: 10px;
  }
  .player_Music_cover{
    margin:0  20px;
    width:50px;
    height:50px;
    overflow: hidden;
  }
  .player_Music_cover img{
    height: 100%;
  }
  #progress {
    margin-top: -1px;
    width: 0;
    background-color: #333333;
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
  #btn_hide_player{
    position: relative;
    height: 40px;
    width: 40px;
    background-size: 40px 40px ;
    background-repeat: no-repeat;
    background-position: center;
    left: 95%;
    transition: background-image 0.5s;
  }
  #btn_hide_player img{
    height: 100%;
    width: 100%;

  }
  .down{
    background-image: url("../../assets/arrow_down.png");
  }
  .up{
    background-image: url("../../assets/arrow_up.png");
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
    background-image: url("../../assets/Play.png");
  }
  .icon-stop{

    background-image: url("../../assets/Pause.png");
  }
  .next{
    padding: 5px;
    height: 25px;
    width: 25px;
    background-size: 25px 25px;
    background-image: url("../../assets/Next.png");
    background-repeat: no-repeat;
    background-position: center;

  }



</style>