<template>
  <router-view />
  <!-- <div :ref="container"></div> -->
</template>

<script>
export default {
  name: "App",
  components: {
    // },
    // mounted()
    // {
    // Vue.axios.get('127.0.0.1:8000/api/music/list/')
    // .then((resp) => {
    //   console.warn(resp)
    // })
  },
};
</script>

<style>
html {
  position: relative;
  min-height: 100vh;
}

body {
  position: absolute;
  top: -60px;
  right: 0;
  left: 0;
  color: white;
  font-family: "Play", sans-serif;
  max-width: 2560px;
  margin: 0 auto;
  min-width: 960px;
  height: 100%;
  padding: 0;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  z-index: -20;
  width: 100%;
  overflow: hidden;
  transition: filter 0.5s;
}
.wrapper {
  margin-right: auto; /* 1 */
  margin-left: auto; /* 1 */

  max-width: 1060px; /* 2 */

  padding-right: 10px; /* 3 */
  padding-left: 10px;
}
.panel-title h1 {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 45px;
}
p {
  margin: 0;
}
a {
  text-decoration: none;
  color: white;
}

.image {
  overflow: scroll;
  height: fit-content;
}

#player_container {
  position: fixed;
  height: 120px;
  bottom: 0;
  left: 0;
  width: 100vw;
  transition: bottom 0.5s;
}
#image_container {
  position: absolute;
  top: 0;
  left: 15vw;
  z-index: +10;
  height: auto;
  width: 70vw;
  margin: 20vh 0;
  transition: display 0.5s;
}

.blurred {
  filter: blur(10px);
}

#image_perimeter {
  position: fixed;
  top: 0;
  z-index: +1;
  height: 1000vh;
  width: 1000vw;
}

#image_container img {
  width: 100%;
  height: 100%;
}
</style>
