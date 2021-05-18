<template>
  <div class="bar">
    <div class="bar_msg wrapper">
      <img src="../assets/thumbsup.png">          Like my content? consider sharing it with your friends!
    </div>
    <div class="bar_content wrapper">

      <div class="bar_social">
      <a class="fa fa-instagram"></a>

      </div>

      <div class="bar_social">
         <a href="#" class="fa fa-facebook"></a>
      </div>
      <div class="bar_social">
        <a href="#" class="fa fa-twitter"></a>

      </div>
      <div class="bar_social">
        <a href="#" class="fa fa-youtube"></a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
name: "Footer"
}
</script>

<style scoped>

  .bar{
    width: 100vw;
    background: #ebdeca;
    text-align: left;
    height: fit-content;
    padding-top: 5px;
    padding-bottom: 15px;
    margin-right: 0;
    font-family: "Brush Script MT";
    text-align: center;
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