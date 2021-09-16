<template>
<Background/>
  <Menu-bar/>
  <div class="wrapper">
    <div class="panel-title"><h1>Writings</h1></div>
    <PostView v-for="post in posts" :key="post.id" :post="post"/>
  </div>
</template>

<script>
import Background from "@/components/Background";
import MenuBar from "@/components/MenuBar";
import PostView from "@/components/Writer/PostView";
export default {
  name: "Writer",
  components: {PostView, MenuBar, Background},
  data(){
    return{posts:[]}
  },
  methods:{
    async fetchPosts(){
      const res = await fetch('http://localhost:8080/api/post/rest/list/')
      // const res = await fetch('http://localhost:5001/api/post/rest/list/')
      return res.json();
    }
  },
  async created(){
    this.posts = await this.fetchPosts()
  }

}
</script>

<style scoped>

</style>