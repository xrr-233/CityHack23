<script setup>

</script>

<template>
  <form action="">
    <div class="row">
      <div class="col-6">
        <input type="radio" id="strategy1" name="strategy1" value="A" />
        <label for="strategy1">A</label>
        <br>
        <input type="radio" id="strategy2" name="strategy2" value="B" />
        <label for="strategy2">B</label>
        <br>
        <input type="radio" id="strategy3" name="strategy3" value="C" />
        <label for="strategy3">C</label>
      </div>
      <div class="col-6" style="border-left: 1px solid rgb(89, 199, 194);">
        From:
        <br>
        <input type="date" id="from" name="from">
        <br>
        To:
        <br>
        <input type="date" id="to" name="from">
      </div>
    </div>
  </form>
</template>

<style scoped>

</style>