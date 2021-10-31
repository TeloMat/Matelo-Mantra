<template>
  <router-view/>
  <div :ref="container"></div>
</template>

<script>


// const Home = {template: '<Body></Body>'}


// const routes = {
//   '/': Home
// }

// new Vue({
//   el: '#app',
//   data: {
//     currentRoute: window.location.pathname
//   },
//   computed:{
//     ViewComponent (){
//       return routes[this.currentRoute]
//     }
//   },
//   render(h){
//     return h(this.ViewComponent)
//   }
// })
// import Vue from 'vue'
// import axios from 'axios'
// import VueAxios from 'vue-axios'
// Vue.use(VueAxios, axios)
export default {
  name: 'App',
  components: {
  // },
  // mounted()
  // {
    // Vue.axios.get('127.0.0.1:8000/api/music/list/')
    // .then((resp) => {
    //   console.warn(resp)
    // })
  }
}
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
  font-family: 'Play', sans-serif;
  max-width: 2560px;
  margin: 0 auto;
  min-width: 960px;
  height:100%;
  padding:0;
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
}
.wrapper{
    margin-right: auto; /* 1 */
    margin-left:  auto; /* 1 */

    max-width: 1060px; /* 2 */

    padding-right: 10px; /* 3 */
    padding-left:  10px;
  }
.panel-title h1{
  font-family: Arial, Helvetica, sans-serif;
  font-size: 45px;
}
p{
  margin: 0;
}
a{
  text-decoration: none;
  color: white;
}







#player-container{
  position: fixed;
  height: 120px;
  bottom: 0;
  left: 0;
  width: 100%;
  transition: bottom 0.5s;
}


</style>
