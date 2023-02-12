<script setup>
import TheItem from './TheItem.vue'
import TheInput from './TheInput.vue'
</script>

<template>
  <TheItem title="Strategy & Backtest Period">
    <template #slot>
      <the-input></the-input>
    </template>
  </TheItem>
  <TheItem title="Backtesting Report"></TheItem>
</template>
