<template>
    <DescriptionView :description = "description"/>
</template>

<script>
import DescriptionView from "./DescriptionView";
export default {
name: "Footer",
  components: {DescriptionView},
  props:{
    description: Object
  },
}
</script>

<style scoped>

  .bar{
    width: 100vw;
    background: #ebdeca;
    height: fit-content;
    text-align: center;
    padding-top: 5px;
    padding-bottom: 15px;
    margin-right: 0;
    font-family: "Brush Script MT";
    font-size: 35px;
  }


  .bar_msg{
    margin-top: 5px;
    margin-bottom: 0;
    padding: 0;
  }
  .bar_msg img{
    width: 40px;
    height: 40px;
    padding-bottom: -5px;
  }
  .bar_content{
    margin: 0;
    display: grid;
    grid-row: 1;
    grid-template-columns: 10% 10% 10% 10%;
    grid-column-gap: 20%;

  }
  .bar_content div{
    float: left;
  }
  .bar_msg{
    order: 1;
  }

  .bar_social{
    font-size: 25px;
    width: 50px;
    height: 50px;
    text-align: center;
    text-decoration: none;
    margin: 5px 2px;
  }
  .fa{
    order: 2;
    padding: 10px 0;
    border-radius: 10px;
    text-align: center;
    margin: 20% 20%;
    width: 100%;
  }
  .fa-instagram{
    background: #125688;
    color: white;
  }
  .fa-twitter{
    background: #55ACEE;
    color: white;
  }
  .fa-youtube{
    background: #bb0000;
    color: white;
  }
  .fa-facebook{
    background: #3B5998;
    color: white;
  }
  .wrapper{
    margin-right: auto; /* 1 */
    margin-left:  auto; /* 1 */

    max-width: 960px; /* 2 */

    padding-right: 10px; /* 3 */
    padding-left:  10px;
  }

</style>