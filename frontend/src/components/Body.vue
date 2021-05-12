<template>
  <div id="page">
    <div class="wrapper">
      <Menu></Menu>
      <Description></Description>
      <Footer></Footer>
    </div>
  </div>
</template>

<script>
import Menu from "@/components/Menu";
import Description from "@/components/Description";
import Footer from "@/components/Footer";
export default {
  name: "Body",
  components: {Footer, Description, Menu}
}
</script>

<style scoped>
  #page{
    overflow: hidden;
    height: fit-content;
    background-image: url("../assets/background3.jpg");
    z-index: -2;
  }


 .wrapper{
    margin-right: auto; /* 1 */
    margin-left:  auto; /* 1 */

    max-width: 960px; /* 2 */

    padding-right: 10px; /* 3 */
    padding-left:  10px;
  }
</style>