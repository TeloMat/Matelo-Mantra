<template>
<div id="background">
    <img src="../assets/W13.jpg">
  </div>
</template>

<script>
export default {
name: "Background"
}
</script>

<style>
  #background{
    position: absolute;
    z-index: -2;
  }
  #background img{
    overflow: hidden;
    height: fit-content;
    position: fixed;
    z-index: -2;
    padding: 0;
    transform: scale(2);
  }
</style>