<template>
  <div id="player_container">
    <audio
      id="audio"
      :src="base_url + song.track"
      preload="auto"
      autoplay
    ></audio>
    <div id="btn_hide_player" class="down" v-on:click="hide_show_player"></div>
    <div id="player">
      <div class="player_Music_cover">
        <img v-bind:src="base_url + cover" />
      </div>
      <div class="player_Music_text">
        <div class="player_Music_name">
          {{ song.title }}
        </div>
        <div class="player_Music_artist">
          <small> {{ song.artists }}</small>
        </div>
      </div>
      <div class="btns">
        <div
          v-on:click="play_pause()"
          id="play-pause"
          class="iconfont icon-stop"
        ></div>
        <div id="duration">
          <input
            type="range"
            min="1"
            max="1000"
            id="progress"
            step="1"
            v-on:change="move_head()"
          />
        </div>
        <div class="iconfont next icon-next"></div>
        <div class="iconfont volume icon-next"></div>
        <div id="max_volume" v-on:click="move_head">
          <div id="current_vol"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import $ from "jquery";

//   $('.next').on('click', function(){
//   aud.src = 'another audio source';
// })

export default {
  name: "MusicPlayer",
  props: ["id"],
  data() {
    return {
      hidden: false,
      base_url: process.env.VUE_APP_API,
    };
  },
  methods: {
    getLeft(str) {
      var el = document.getElementById(str);
      return el.getBoundingClientRect().left;
    },
    getRight(str) {
      var el = document.getElementById(str);
      return el.getBoundingClientRect().right;
    },
    getTargetProgress(x) {
      var target =
        (x - this.getLeft("progress")) /
        (this.getRight("duration") - this.getLeft("progress"));
      return target;
    },
    play_pause: function () {
      var aud = $("#audio")[0];
      // aud.ontimeupdate = function () {
      //   document.getElementById("progress").value = aud.currentTime * 1000;
      // };
      console.log((aud.currentTime / aud.duration) * 1000);
      if (aud.paused) {
        aud.play();
        $("#play-pause").removeClass("icon-play");
        $("#play-pause").addClass("icon-stop");
      } else {
        aud.pause();
        $("#play-pause").removeClass("icon-stop");
        $("#play-pause").addClass("icon-play");
      }
    },

    move_head: function () {
      let aud = document.getElementById("audio");
      let target = document.getElementById("progress").value / 1000;

      $("#play-pause").addClass("loading");
      $("#play-pause").removeClass("icon-stop");
      $("#play-pause").removeClass("icon-play");
      aud.pause();
      aud.load();
      aud.currentTime = this.song.track_duration * target;
      aud.play();
      $("#play-pause").removeClass("loading");
      $("#play-pause").removeClass("icon-play");
      $("#play-pause").addClass("icon-stop");
    },

    hide_show_player() {
      if (this.hidden !== true) {
        $("#player_container").css("bottom", "-80px");
        $("#btn_hide_player").removeClass("down");
        $("#btn_hide_player").addClass("up");
        this.hidden = true;
      } else {
        $("#player_container").css("bottom", "0");
        $("#btn_hide_player").removeClass("up");
        $("#btn_hide_player").addClass("down");
        this.hidden = false;
      }
    },
    async created() {},
  },
};
</script>

<style >
#player {
  width: 100%;
  padding: 15px 15vw 10px 15vw;
  display: flex;
  background-color: rgba(255, 255, 255, 0.2);
  z-index: +10000;
  box-shadow: 0px 10px 20px 5px #000000;
}
.player_Music_text {
  padding: 10px;
}
.player_Music_cover {
  margin: 0 20px;
  width: 50px;
  height: 50px;
  overflow: hidden;
}
.player_Music_cover img {
  height: 100%;
}
/* #progress {
  margin-top: -1px;
  width: 0;
  background-color: #333333;
  height: 7px;
  border-radius: 10px;
} */
#duration {
  width: 40vw;
}
/* #duration input {
  width: 100%;
} */
#progress {
  margin: 10px 5vw;
  height: 5px;
  background-color: #8c8b8b;
  border-radius: 10px;
  width: 60%;
  padding: 0;
}
#duration:hover {
  cursor: pointer;
}
#btn_hide_player {
  position: relative;
  height: 40px;
  width: 40px;
  background-size: 40px 40px;
  background-repeat: no-repeat;
  background-position: center;
  left: 95%;
  transition: background-image 0.5s;
}
#btn_hide_player img {
  height: 100%;
  /*width: 100%;*/
}
.down {
  background-image: url("../../assets/arrow_down.png");
}
.up {
  background-image: url("../../assets/arrow_up.png");
}

.btns {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 16px;
  flex-flow: row nowrap;
}
.iconfont:hover {
  cursor: pointer;
}
#play-pause {
  height: 25px;
  width: 25px;
  background-size: 25px 25px;

  background-repeat: no-repeat;
  background-position: center;
}

.icon-play {
  background-image: url("../../assets/Play.png");
}
.icon-stop {
  background-image: url("../../assets/Pause.png");
}
.loading {
  background-image: url("../../assets/loading.png");
  -webkit-animation: rotating 2s linear infinite;
  -moz-animation: rotating 2s linear infinite;
  -ms-animation: rotating 2s linear infinite;
  -o-animation: rotating 2s linear infinite;
  animation: rotating 2s linear infinite;
}
.next {
  padding: 5px;
  height: 25px;
  width: 25px;
  background-size: 25px 25px;
  background-image: url("../../assets/Next.png");
  background-repeat: no-repeat;
  background-position: center;
}
@-webkit-keyframes rotating /* Safari and Chrome */ {
  from {
    -webkit-transform: rotate(0deg);
    -o-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  to {
    -webkit-transform: rotate(360deg);
    -o-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}
@keyframes rotating {
  from {
    -ms-transform: rotate(0deg);
    -moz-transform: rotate(0deg);
    -webkit-transform: rotate(0deg);
    -o-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  to {
    -ms-transform: rotate(360deg);
    -moz-transform: rotate(360deg);
    -webkit-transform: rotate(360deg);
    -o-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}
</style>