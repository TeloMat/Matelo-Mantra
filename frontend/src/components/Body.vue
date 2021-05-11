<template>
  <div id="page">
    <div class="wrapper">

      <Menu>    </Menu>
    </div>
  </div>
</template>

<script>
import Menu from "@/components/Menu";
export default {
  name: "Body",
  components: {Menu}
}
</script>

<style scoped>
  #page{
    overflow: hidden;
    height: fit-content;
    background-image: url("../assets/background3.jpg");
  }


 .wrapper{
    margin-right: auto; /* 1 */
    margin-left:  auto; /* 1 */

    max-width: 960px; /* 2 */

    padding-right: 10px; /* 3 */
    padding-left:  10px;
  }
</style>