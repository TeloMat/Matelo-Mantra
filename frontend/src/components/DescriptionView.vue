<template>
  <div class="sub-title">
    <img src="../assets/Matelo_Mantra_VF.png" />
  </div>
  <div class="description-box">
    <div v-if="description.picture" class="description-image">
      <img v-bind:src="base_url + description.picture" />
    </div>
    <div class="description-content">
      <div class="description-content_title">About the artist</div>
      <div class="description-content_quote">
        {{ description.quote }}
      </div>
      <textarea
        class="description-content_text"
        v-text="description.text"
        disabled
      />
    </div>
  </div>
</template>

<script>
export default {
  name: "DescriptionView",
  components: {},
  data() {
    return {
      base_url: process.env.VUE_APP_API,
    };
  },
  props: {
    description: Object,
  },
  methods: {},
};
</script>

<style scoped>
.sub-title {
  max-width: 700px;
  width: fit-content;
  height: 15vh;
  margin-top: 15vh;
}

.sub-title img {
  max-width: 100%;
  max-height: 100%;
}

.description-box {
  height: 70vh;
  width: 100%;
  /*border: 5px solid red;*/
  display: grid;
  grid-template-columns: 1fr 3fr;
}

.description-image {
  width: 95%;
  height: 50%;
  margin: 50% 5%;
  border-radius: 50%;
  overflow: hidden;
}

.description-image img {
  /*position: absolute;*/
  min-width: 100%;
  max-width: none;
  height: 100%;
  transition: transform 0.5s; /* Animation */
  margin: 0 -110%;
  left: -30%;
}

.description-content {
  max-width: 100%;
  padding: 5%;
}

.description-content_title {
  font-weight: bold;
  text-transform: uppercase;
  margin-bottom: 5%;
  text-align: center;
  font-size: 35px;
}

.description-content_quote {
  font-style: italic;
  margin-bottom: 2.5%;
  padding: 2% 0;
  font-size: 30px;
  text-align: justify;
  width: 100%;
}

.description-content_text {
  resize: none;
  height: 37%;
  background: transparent;
  border: 0px;
  overflow: hidden;
  font-size: 25px;
  text-align: justify;
  width: 100%;
  color: black;
  font-size: 20px;
}
</style>