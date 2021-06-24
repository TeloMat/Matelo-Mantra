<template>
<div class="player">
  <audio controls>
  <source :src="song.track">
  Your browser does not support the audio tag.
</audio>
</div>
</template>

<script>
export default {
  name: "MusicPlayer",
  data:()=>({

  }),
  methods:{

  }
}
</script>

<style scoped>

</style>