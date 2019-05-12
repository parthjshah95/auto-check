<template>
  <div id="app">
    <!-- <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div>
    <router-view/> -->
    <nav class="navbar navbar-dark bg-dark">
      <h3 class="m-2" v-bind:class="[alive? 'service_alive': 'service_dead']">Auto Assessor</h3>
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
      <div class="card-block flex-col card-img col-sm-10 col-md-8 col-lg-6 p-0">
        <img v-bind:src="demo.image" class="card-img" alt="image not found">
        <button class="w-100 btn btn-primary" v-on:click="test_demo_image()">Submit image as answer</button>
      </div>

      <div class="card-block p-3 flex-col flex-fill col-md-4 col-lg-6">
        Submit the image to see whether the answer is correct.
        <hr>
        <h5>Expected answer:</h5>
          {{demo.template.answer}}
        <div v-if="demo.result">
          <h5 class="mt-3">We found following words in your answer:</h5>
          {{demo.result}}
        </div>
      </div>
    </div>
    <div class="card m-4 flex-row flex-wrap">
      <div class="card-header w-100">
        <h4 class="m-0">Upload your own answer</h4>
      </div>
      <div class="card-block flex-col card-img col-sm-10 col-md-8 col-lg-6 p-0">
          <vue-base64-file-upload
          input-class=""
          image-class="card-img"/>
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
      alive:false,
      demo: {
        image: demo_image,
        result: null,
        template: {
          "question": "demo",
          "answer": "History is a coherent account of the significant past events in the progress of human culture."
        }
      },
      isLoading: false,
      fullPage: true,
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
    heartbeat(){
      this.$http.get(this.url("heartbeat")).then(
        function success(response){this.alive = true},
        function failure(response){this.alive = false}
      )
    },
    addTemplate(template){
      function success(response){
        console.log(response)
      }
      function failure(response){
        console.log(response)
      }
      this.$http.post(this.url("addTemplate"), template).then(success, failure)
    },
    test_image(image, question){
      console.log("sending demo image..")
      this.isLoading = true
      this.$image2base64(image)
      .then(
          (response) => {
              var base64Image = response
              var body = {
                "question": question,
                "image": base64Image
              }
              this.$http.post(this.url("assessImage"), body).then(
                function success(response){
                  console.log(response)
                  this.isLoading = false
                  this.demo.result = response.body.matches.join(" ")
                },
                function error(e){
                  console.error(e)
                  this.isLoading = false
                  this.demo.result = null
                }
              )
          }
      )
      .catch(
          (error) => {
              console.log(error);
              this.isLoading = false
              alert('sorry, something went wrong')
          }
      )
    },
    test_demo_image(){
      var response = null
      this.addTemplate(this.demo.template)
      response = this.test_image(this.demo.image, this.demo.template.question)
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
.service_alive {
  color: lightblue;
}
.service_dead{
  color: lightgray;
}
</style>
