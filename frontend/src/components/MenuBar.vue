<template>
<div class="topnav">
  <router-link to="/"><div class="home" ><img src="../assets/Matelo_Mantra_VF_(2).png"> </div></router-link>
  <router-link to=music><div> Musician </div></router-link>
  <router-link to=travels><div> Traveler </div></router-link>
  <router-link to=writer><div> Writer </div></router-link>
  <div id="icon_container">
    <img class="bar-icon" src="../assets/logo.png">
  </div>
</div>

</template>

<script>

export default {
name: "MenuBar"
}
</script>

<style scoped>
body {
  margin: 0;
  font-family: Avenir, Helvetica, Arial, sans-serif;
}

.topnav {
  overflow: hidden;
  background-color: #737880;
  height: 80px;
}

.topnav div {
  float: left;
  color: #f2f2f2;
  padding: 15px 20px;
  text-align: center;
  text-decoration: none;
  font-size: 40px;
  height: 100%;
  font-family: Impact;
}

.topnav div:hover {
  background-color: #ddd;
  color: black;
}

.topnav div.active {
  background-color: #2c7363;
  color: white;
}
.home{
  width: 350px;
  height: 100%;
  background-color: #8c8b8b;
}
.home img{
  max-width: 100%;
  max-height: 100%;
  display: block;
  margin: 2vh 0;
}
#icon_container{
  float: right;
  height: 100%;
  width: 50px;
  padding: 15px 15px;
}
#icon_container img{
  max-height: 100%;
  max-width: 100%;

}
#icon_container:hover{

}


</style>