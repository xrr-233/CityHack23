<script setup>
import { ref } from 'vue'

defineProps({
  title: {
    type: String,
    required: true
  }
})

let state = ref(false)

function changeState() {
  this.state = !this.state
}
</script>

<template>
  <div class="item" style="height: 50px">
    <div class="row">
      <div class="offset-3 col-6 text-center">
        <h2 style="line-height: 50px">{{ title }}</h2>
      </div>
      <div class="col-3 position-relative">
        <div @click="changeState()" class="my-button position-absolute top-50 start-50 translate-middle"
          style="border: 1px solid rgb(89, 199, 194); height: 30px; width: 30px">
          <i class="position-absolute top-50 start-50 translate-middle">
            <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" v-if="state === false">
              <polygon points="5 10 25 10 15 20" stroke="rgb(89, 199, 194)" fill="rgb(89, 199, 194)" stroke-width="1" />
            </svg>
            <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" v-else>
              <polygon points="5 20 25 20 15 10" stroke="rgb(89, 199, 194)" fill="rgb(89, 199, 194)" stroke-width="1" />
            </svg>
          </i>
        </div>
      </div>
    </div>
  </div>
  <div class="details p-3" v-if="state === true">
    <slot name="slot"></slot>
  </div>
</template>

<style scoped>
.item {
  margin-top: 2rem;
  border: 2px solid rgb(89, 199, 194);
}

.details {
  margin-top: 1rem;
  border: 1px solid rgb(89, 199, 194);
}

h2 {
  margin-bottom: 0;
}

.my-button:hover {
  cursor: pointer;
}
</style>
