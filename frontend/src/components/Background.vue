<template>
<div id="background">
    <img src="../assets/W9.jpg">
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

  }
</style>