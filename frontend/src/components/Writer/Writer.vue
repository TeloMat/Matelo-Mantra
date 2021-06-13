<template>
<Background/>
  <Menu-bar/>
  <div class="wrapper">
    <div class="panel-title"><h1>Writings</h1></div>
    <PostView/>
    <PostView/>
    <PostView/>
    <PostView/>
    <PostView/>
    <PostView/>

  </div>
</template>

<script>
import Background from "@/components/Background";
import MenuBar from "@/components/MenuBar";
import PostView from "@/components/Writer/PostView";
export default {
name: "Writer",
  components: {PostView, MenuBar, Background}
}
</script>

<style scoped>

</style>