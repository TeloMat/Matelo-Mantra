<template>
    <Background/>
    <div class="wrapper">
      <Menu></Menu>
    </div>
    <Footer></Footer>
</template>

<script>
import Menu from "@/components/Menu";
import Footer from "@/components/Footer";
import Background from "@/components/Background";
export default {
  name: "Home",
  components: {Background, Footer, Menu}
}
</script>

<style scoped>



 .wrapper{
    margin-right: auto; /* 1 */
    margin-left:  auto; /* 1 */

    max-width: 1060px; /* 2 */

    padding-right: 10px; /* 3 */
    padding-left:  10px;
  }
</style>