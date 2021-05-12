<template>
  <div class="bar">
    <div class="bar_msg">
      <p>
      Like my content? consider sharing it with your friends!
      </p>
    </div>

    <div class="bar_social">
    <a href="#" class="fa fa-instagram"></a>

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
</template>

<script>
export default {
name: "Footer"
}
</script>

<style scoped>

  .bar{
    display: inline-block;
    text-align: left;
    width: 100%;
  }
  .bar p{
    font-family: "Brush Script MT";
    text-align: left;
    font-size: 35px;
  }
  .bar_msg{
    order: 1;

  }

  .bar_social{
    display: flex;
    flex-direction: row;
    font-size: 20px;
    width: 50px;
    height: 50px;
    text-align: center;
    text-decoration: none;
    margin: 5px 2px;
  }
  .fa{
    order: 2;

    padding-top: 25px;
    padding-right: 10px;
    padding-left: 10px;

    border-radius: 100%;
    text-align: center;
    height: 100%;
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

</style>