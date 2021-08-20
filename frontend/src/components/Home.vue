<template>
    <Background/>
    <div class="wrapper">
      <Menu :description="description"></Menu>
    </div>
    <Footer :description="description"></Footer>
</template>

<script>
import Menu from "@/components/Menu";
import Footer from "@/components/Footer";
import Background from "@/components/Background";
export default {
  name: "Home",
  components: {Background, Footer, Menu},
  data(){
    return{
      description: null
    }
  },
  methods:{
    async fetchData(){
      const res = await fetch('http://localhost:8000/api/descriptions/rest/')
      console.log("test")
      return res.json()
    }
  },
  async create(){
    this.description = await this.fetchData()
  }
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