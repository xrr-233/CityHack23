<script setup>
import TheItem from './TheItem.vue'
import TheInput from './TheInput.vue'
import TheOutput from "./TheOutput.vue";
import { ref } from 'vue'

let status = ref(null)

function loadingStatus(s) {
  status.value = s
  console.log(s)
}
</script>

<template>
  <TheItem title="Strategy & Backtest Period">
    <template #slot>
      <the-input @loadingStatus='loadingStatus'></the-input>
    </template>
  </TheItem>
  <TheItem title="Backtesting Report" v-if="status !== null">
    <template #slot>
      <the-output :status="status"></the-output>
    </template>
  </TheItem>
</template>
