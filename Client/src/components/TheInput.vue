<script setup>
import axios from "axios";

const emit = defineEmits(["loadingStatus"]);
async function getYahooFinance() {
  emit("loadingStatus", {
    'statusText': 'loading'
  });
  const strategies = document.getElementsByName('strategy');
  let res;
  if(strategies[0].checked)
    res = await axios.get(`http://localhost:8080/SMA`);
  else if(strategies[1].checked)
    res = await axios.get(`http://localhost:8080/OLS`);
  else if(strategies[2].checked)
    res = await axios.get(`http://localhost:8080/SVM`);
  else if(strategies[3].checked)
    res = await axios.get(`http://localhost:8080/DNN`);
  res.statusText = 'finished'
  emit("loadingStatus", res);
}
</script>

<template>
  <form action="" onsubmit="return false">
    <div class="row">
      <div class="col-6">
        <div>
          <label for="code">Stock Code:</label>
          <br>
          <input type="text" id="code" name="code" placeholder="AAPL">
        </div>
        <div class="mt-3">
          Quantitative Trading Strategy:
          <br>
          <div class="position-relative">
            <input type="radio" id="strategy1" name="strategy" value="A" checked>
            <label for="strategy1">Simple moving average</label>
          </div>
          <div class="position-relative">
            <input type="radio" id="strategy2" name="strategy" value="B">
            <label for="strategy2">Linear OLS Regression</label>
          </div>
          <div class="position-relative">
            <input type="radio" id="strategy3" name="strategy" value="C">
            <label for="strategy3">Naïve Bayes, Logistic Regression, Support Vector Machine</label>
          </div>
          <div class="position-relative">
            <input type="radio" id="strategy4" name="strategy" value="C">
            <label for="strategy4">Deep Neural Network</label>
          </div>
        </div>
      </div>
      <div class="col-6" style="border-left: 1px solid rgb(89, 199, 194);">
        <div>
          <div>
            <label for="from">From:</label>
            <br>
            <input type="date" id="from" name="from">
          </div>
          <div>
            <label for="to">To:</label>
            <br>
            <input type="date" id="to" name="from">
          </div>
        </div>
        <div class="mt-3">
          <input type="submit" value="Submit" @click="getYahooFinance()">
        </div>
      </div>
    </div>
  </form>
</template>

<style scoped>
input[type="text"] {
  width: 200px;
  background-color: unset;
  color: rgb(181, 203, 198);
  text-indent: 5px;
  border: 1px solid rgb(89, 199, 194);
}
input[type="date"] {
  width: 200px;
  background-color: unset;
  color: rgb(181, 203, 198);
  text-indent: 5px;
  border: 1px solid rgb(89, 199, 194);
}
input[type="submit"] {
  width: 200px;
  height: 50px;
  background-color: unset;
  color: rgb(181, 203, 198);
  border: 1px solid rgb(89, 199, 194);
}
input[type="submit"]:hover {
  border: 1px solid rgb(101, 170, 107);
}
input[type="radio"] {
  margin-right: 5px;
}
</style>