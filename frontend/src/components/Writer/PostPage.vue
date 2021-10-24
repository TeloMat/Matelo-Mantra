<template>
  <background/>
  <menu-bar/>
  <div class="wrapper">
    <router-link to=post_details><div class="post_title"><p>{{ post.name}} </p></div>
      <div class="post_card">
         <div class="post_content">
          <div class="post_cover"><img :src="base_url + post.thumbnail"></div>
          <div class="post_info">
            <div class="post_credits">Credits :<br>
              <div class="post_credits_item" :key="credit.id" v-for="credit in post.credits">
                <b>{{credit.contributor}}</b> - {{credit.contribution}}
              </div>
            </div>
          </div>
        </div>
      <div class="post_text"> {{ post.text }}</div>
      </div>
    </router-link>
  </div>
</template>

<script>
import Background from "@/components/Background";
import MenuBar from "@/components/MenuBar";
export default {
  name: "PostPage",
  components: {MenuBar, Background},
  data(){
    return{
      post: Object,
      isFetching: true,
      base_url: process.env.VUE_APP_API,
    }
  },
    methods:{
    async fetchData(id){

      const res = await fetch(process.env.VUE_APP_API +"/api/travels/albums/"+ id +"/")

      return await res.json()
    },
  },
  async created() {
      this.post= await this.fetchData(this.$route.params.id)
      this.isFetching = false
  }
}
</script>

<style scoped>
.post_card{
  background-color: rgba(211, 211, 211, 0.5);
  border-radius: 25px;
  padding: 2.5% 3%;
  height: 80vh;
  margin: 30px 0;
}
.post_title{
  border-radius: 25px;
  padding: 15px 20px;
  font-size: 35px;
  max-width: 100%;
  max-height: 45%;
  margin: 5% 0;

  background-color: rgba(96, 121, 116, 0.7);
}
.post_title p{
  margin: 0;
  color: black;
}
.post_credits{
  padding: 2.5%;
  margin: 5% 0;
  text-align: left;
  width: 95%;
  height: 60%;
  overflow: scroll;
  font-family: Impact;
  border-radius: 25px;
  background-color: rgba(140, 139, 139,0.5);
}
.post_info{
  width: 55%;
  margin: 0;
  padding: 0;
  height: fit-content;
}
.post_content{

  display: flex;
  flex-flow: column wrap;
  width: 100%;
  height: 50%;
  margin: 0;
}
.post_cover{
  height: 100%;
  margin: 2.5% 2%;
  max-width: 40%;
}
.post_cover img{
  object-fit: cover;
  max-width: 100%;
  overflow: hidden;
  border-radius: 25px;
  margin: 0 -140%;
}
.post_text{
  padding: 2.5%;
  border-radius: 25px;
  color: white;
  background-color: rgba(32, 91, 80, 0.7);
  text-align: justify;
  width: 95%;
  height: 40%;

  overflow: scroll;
}

::-webkit-scrollbar {
    width: 12px;
}
::-webkit-scrollbar-corner{
  background: rgba(0,0,0,0);
}

</style>