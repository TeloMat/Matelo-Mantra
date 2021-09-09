<template>
    <Background/>
    <div class="wrapper" v-if="!isFetching">
      <Menu :description="description"></Menu>
      <Description-view :description="description"></Description-view>
    </div>
</template>

<script>
import Menu from "@/components/Menu";
import Background from "@/components/Background";
import DescriptionView from "./DescriptionView";
export default {
  name: "Home",
  components: {DescriptionView, Background, Menu},
  data(){
    return{
      description: null,
      isFetching: true,
    }
  },
  methods:{
    async fetchData(){
      const res = await fetch('http://localhost:5001/api/descriptions/rest/')
      // const res = await fetch('http://localhost:8000/api/descriptions/rest/')
      return res.json()
    }
  },
  async created(){
    this.description = await this.fetchData()
    this.isFetching = false
  }
}
</script>

<style scoped>



  .wrapper{
    margin-top: 0;
    margin-right: auto; /* 1 */
    margin-left:  auto; /* 1 */

    max-width: 1060px; /* 2 */

    padding-right: 10px; /* 3 */
    padding-left:  10px;
  }
</style>