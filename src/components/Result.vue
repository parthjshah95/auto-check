<template>
<div>
    <h6 class="mt-3 text-muted">Raw detections:</h6>
    <blockquote class="text-muted">{{raw_detection}}</blockquote>
    <h5 class="mt-3 result-match">Words matching with the expected answer:</h5>
    <blockquote class="result-match">{{matched_answer}}</blockquote>
</div>
</template>
<script>
export default {
    name: 'Result',
    props: ['result'],
    computed: {
        raw_detection(){
            return this.result? this.result.detected_words.join(" "): null
        },
        matched_answer(){
            return this.result? this.result.matches.join(" "): null
        }
    }
}
</script>
<style lang="scss" scoped>
.result-match{
  color: darkgreen
}
</style>
