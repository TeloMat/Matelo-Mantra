<template>
  <router-link :to="{ name: 'Post_details', params: {id: post.id}}">
    <div class="post_card">
      <div class="post_cover"><img :src="base_url + post.thumbnail"></div>
      <div class="post_content">
        <div class="post_title"><p>{{ post.name }}</p></div>
        <div class="post_text"><p>{{post.text}}</p></div>
        <div class="post_credits">Credits :<div v-for="credit in post.credits" :key="credit.id"><br> {{credit.contribution}} : {{credit.contributor}}<br> Writer : Matelo Mantra</div></div>
      </div>
    </div>
  </router-link>
</template>

<script>
export default {
name: "PostView",
  components:{},
  props:{
    post: Object
  },
  data(){
    return{
      base_url: process.env.VUE_APP_API,
    }
  },
  methods:{}
}
</script>

<style scoped>
.post_card{
  background-color: rgba(211, 211, 211, 0.5);
  border-radius: 25px;
  padding: 2.5% 3%;
  display: flex;
  height: 60vh;
  margin: 30px 0;
  flex-flow: column wrap;
  box-shadow: 0px 10px 20px 5px grey;
}
.post_title{
  border-radius: 25px;
  padding: 15px 20px;
  font-size: 35px;
  max-height: 90%;
  margin: 5% 0;

  background-color: rgba(96, 121, 116, 0.7);
}
.post_title p{
  margin: 0;
  color: black;
}
.post_content{
  width: 50%;
  height: 100%;
  margin: 0;
}
.post_cover{
  height: 70%;
  margin: 6% 2%;
  width: fit-content;
  max-width: 40%;
  overflow: hidden;
  border-radius: 15px;
}
.post_cover img{
  object-fit: cover;
  max-height: 100%;
  margin: 0 -140%;
}
.post_text{
  padding: 5%;
  border-radius: 25px;
  color: white;
  background-color: rgba(32, 91, 80, 0.7);
  text-align: justify;
  max-height: 40%;
  overflow: scroll;
}
.post_credits{
  padding: 5% 5%;
  margin: 5% 0;
  text-align: left;
  width: 90%;
  height: 10%;
  overflow: scroll;
  font-family: Impact;
  border-radius: 25px;
  background-color: rgba(140, 139, 139,0.5);
}

::-webkit-scrollbar {
    width: 12px;
}
::-webkit-scrollbar-corner{
  background: rgba(0,0,0,0);
}
</style>