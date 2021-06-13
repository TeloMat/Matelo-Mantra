<template>
<div class="topnav">
  <div class="home" ><router-link to="/"><img src="../assets/Matelo_Mantra_VF_(2).png"> </router-link></div>

  <div class="menu_items">
  <router-link  class="item" to=music><div > Musician </div></router-link>
  <router-link class="item" to=travels><div > Traveler </div></router-link>
  <router-link class="item" to=writer><div> Writer </div></router-link>
  <div id="icon_container">
    <img class="bar-icon" src="../assets/logo.png">
  </div>
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
  width: 105vw;
  height: 80px;
  overflow: hidden;
  display: flex;
  flex-flow: row nowrap;
  padding: 0;
  margin: 0;
}

.home{
  max-width: 35%;
  height: auto;
  background-color: #8c8b8b;
}
.home img{
  max-width: 90%;
  max-height: 100%;
  display: block;
  margin: 3vh 2vw;

}
.topnav div {
  float: left;
  color: #f2f2f2;
  text-align: center;
  text-decoration: none;
  font-size: 40px;
  height: 100%;
}

.item{
  float: left;
  color: #f2f2f2;
  text-align: center;
  text-decoration: none;
  font-size: 40px;
  height: 100%;
  font-family: Impact;
}

.item div{
  padding: 2vh 4vw;

}

.menu_items{
  background-color: #737880;
  width: 60%;
  margin: 0;
  padding: 0;

}
.item:hover{
  background-color: #dddddd;
  color: #000;
}
.item:hover .item.div{
  background-color: #dddddd;
  color: #000;
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
  @media only screen and (max-width: 600px) {
  .topnav{
    display: block;
    height: 20vh;
    width: 100%;
    margin: 0;
    padding: 0;
    overflow: visible;
  }
  .topnav a{
    vertical-align: center;
  }

  .home{
    max-width: 90%;
    height: 50%;
    margin: 0;
    padding: 0 5%;

  }
  .home img{
    margin: 3.5% 5%;
  }
  .menu_items{
    display: flex;
    flex-flow: row nowrap;
    width: 135%;
    height: 50%;
  }
  .item{
    padding: 3% 1%;
    width: 22.7%;
    height: 37%;
    max-width: 25%;
    border-right: #333333 1px solid;
  }
  .item div{
    padding: 0;
    height: fit-content;

    max-width: 100%;

  }
  .item:hover{
    color: black;
    background-color: white;
  }
  #icon_container{
    display: none;
  }
  a.item div{
    width: 100%;
  }

}

</style>