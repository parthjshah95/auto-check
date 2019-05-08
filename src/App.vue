<template>
  <div id="app">
    <!-- <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div>
    <router-view/> -->
    <nav class="navbar navbar-dark bg-dark">
      <a class="navbar-brand">Auto Assessor</a>
    </nav>
    <loading :active.sync="isLoading" 
    :can-cancel="false" 
    :is-full-page="fullPage"></loading>
    <div class="m-5 ml-10 mr-10">
      <h5>Automatic checking of answer papers</h5>
      The Auto-assessor can automatically evaluate a student's answer paper through <br> <b>handwriting recognition</b> and a dynamic knowledge base. 
    </div>
    <div class="card m-4 flex-row flex-wrap">
      <div class="card-header w-100">
        <h4 class="m-0">Try it out!</h4>
      </div>

      <div class="card-block flex-col card-img col-md-8 col-lg-5">
        <img v-bind:src="demo_image" class="card-img" alt="image not found">
        <button class="w-100 btn btn-primary" v-on:click="test_image(demo_image)">Submit image as answer</button>
      </div>

      <div class="card-block p-3 flex-col flex-fill col-md-4 col-lg-7">
        <!-- flex-wrap col-sm-3 col-md-4 col-lg-6 -->
        Submit the image to see whether the answer is correct.
        <hr>
        <h5>Expected answer:</h5>
        "History is a coherent account of the significant past events in the progress of human culture."
        <div v-if="results.card_1">
          <h5 class="mt-3">We found following words in your answer:</h5>
          {{results.card_1}}
        </div>
      </div>
      
    </div>
  </div>
</template>

<script>
import demo_image from "@/assets/1_cropped.jpg";
import Loading from 'vue-loading-overlay';
import 'vue-loading-overlay/dist/vue-loading.css';
import VueBase64FileUpload from 'vue-base64-file-upload';


export default {
  name: "app",
  components: {
    Loading, VueBase64FileUpload
  },
  data(){
    return {
      demo_image : demo_image,
      isLoading: false,
      fullPage: true,
      results:{
        card_1 : null
      },
      endpoints: {
        heartbeat: "/heartbeat",
        assessImage: "/assessImage",
        addTemplate:"/addTemplate"
      }
    }
  },
  methods:{
    url(endpoint){
      return process.env.VUE_APP_SERVICE_URL + this.endpoints[endpoint]
    },
    test_image(image){
      this.isLoading = true
      this.$image2base64(image)
      .then(
          (response) => {
              var base64Image = response
              var body = {
                "question":"demo",
                "image": base64Image
              }
              this.$http.post(this.url("assessImage"), body).then(
                function success(response){
                  console.log(response)
                  this.isLoading = false
                },
                function error(e){
                  console.error(e)
                  alert('sorry, something went wrong')
                  this.isLoading = false
                }
              )
          }
      )
      .catch(
          (error) => {
              console.log(error);
              this.isLoading = false
          }
      )
    }
  }
}
</script>


<style lang="scss">
@import "../node_modules/bootstrap/scss/bootstrap.scss";

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
nav {
  color: white;
}

</style>
