<template>
 <div class="post_card">
    <div class="post_cover"><img src="../assets/album1.jpg"></div>
    <div class="post_content">

      <router-link to=post_details><div class="post_title"><p>Post title</p></div></router-link>
      <div class="post_text">Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.</div>
      <div class="post_credits">Credits :<br> producer : Matelo Mantra <br> Writer : Matelo Mantra</div>
    </div>
 </div>
</template>

<script>
export default {
name: "PostView"
}
</script>

<style scoped>
.post_card{
  background-color: rgba(211, 211, 211, 0.5);
  border-radius: 25px;
  padding: 2.5% 3%;
  display: flex;
  height: 60vh;
  margin: 30px 0;
  flex-flow: column wrap;

}
.post_title{
  border-radius: 25px;
  padding: 15px 20px;
  font-size: 35px;
  max-height: 90%;
  margin: 5% 0;

  background-color: rgba(96, 121, 116, 0.7);
}
.post_title p{
  margin: 0;
  color: black;
}
.post_content{
  width: 50%;
  height: 100%;
  margin: 0;
}
.post_cover{
  height: 70%;
  margin: 6% 2%;
  width: fit-content;
  max-width: 40%;
  overflow: hidden;
  border-radius: 15px;
}
.post_cover img{
  object-fit: cover;
  max-height: 100%;
  margin: 0 -140%;
}
.post_text{
  padding: 5%;
  border-radius: 25px;
  color: white;
  background-color: rgba(32, 91, 80, 0.7);
  text-align: justify;
  max-height: 40%;
  overflow: scroll;
}
.post_credits{
  padding: 5% 5%;
  margin: 5% 0;
  text-align: left;
  width: 90%;
  height: 10%;
  overflow: scroll;
  font-family: Impact;
  border-radius: 25px;
  background-color: rgba(140, 139, 139,0.5);
}

::-webkit-scrollbar {
    width: 12px;
}
::-webkit-scrollbar-corner{
  background: rgba(0,0,0,0);
}
</style>