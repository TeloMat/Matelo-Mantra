<template>

  <router-view/>
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

export default {
  name: 'App',
  components: {
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
  top: -70px;
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
</style>
