<template>
    <div v-if="uploaded.result">
          <h5 class="mt-3">We found following words in your answer:</h5>
          <blockquote>{{uploaded.result}}</blockquote>
    </div>
</template>
<script>
export default {
    name: 'Result'
}
</script>
