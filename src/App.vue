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
        <button class="w-100 btn btn-primary" v-on:click="test_image()">Submit image as answer</button>
      </div>

      <div class="card-block p-3 flex-col flex-fill col-md-4 col-lg-7">
        <!-- flex-wrap col-sm-3 col-md-4 col-lg-6 -->
        Submit the image to see whether the answer is correct.
        <hr>
        <h6>Expected answer:</h6>
        "History is a coherent account of the significant past events in the progress of human culture."
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
      demo_answer: true
    }
  },
  methods:{
    test_image(){
      this.isLoading = true
      this.$image2base64(this.demo_image)
      .then(
          (response) => {
              var base64Image = response
              var body = {
                "question":"demo",
                "image": base64Image
              }
              this.$http.post("http://localhost:5000/assessImage", body).then(
                function success(response){
                  console.log(response)
                  this.isLoading = false
                },
                function error(e){
                  console.error(e)
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
    },
    test(x){
      console.log(x)
      console.log(this.$refs.myFiles.files[0])
      this.$http.get('http://localhost:5000/heartbeat').then(response => {
        console.log(response.body)
      });
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
