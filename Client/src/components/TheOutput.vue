<script setup>
defineProps({
  status: {
    type: Object,
    required: true
  }
})
</script>

<template>
  <div v-if="status.statusText === 'loading'">
    Waiting for the response of the server...
  </div>
  <div v-else-if="status.statusText === 'finished'">
    <div class="row">
      <div class="offset-3 col-6">
        <table class="table" style="color: rgb(181, 203, 198)">
          <tr>
            <th colspan="2" class="text-center">Basic Info</th>
          </tr>
          <tr>
            <td>Start Date: </td>
            <td class="table-data">{{ status.data.Strategy.start }}</td>
          </tr>
          <tr>
            <td>End Date: </td>
            <td class="table-data">{{ status.data.Strategy.end }}</td>
          </tr>
          <tr>
            <td>Total Return: </td>
            <td class="table-data">{{ status.data.Strategy.total_return }}</td>
          </tr>
          <tr>
            <td>CAGR (Compound annual growth rate): </td>
            <td class="table-data">{{ status.data.Strategy.cagr }}</td>
          </tr>
          <tr>
            <th colspan="2" class="text-center">Risk-adjusted Ratios</th>
          </tr>
          <tr>
            <td>Max Drawdown: </td>
            <td class="table-data">{{ status.data.Strategy.max_drawdown }}</td>
          </tr>
          <tr>
            <td>Calmar ratio: </td>
            <td class="table-data">{{ status.data.Strategy.calmar }}</td>
          </tr>
          <tr>
            <th colspan="2" class="text-center">Interest Rate</th>
          </tr>
          <tr>
            <td>MTD (Month to date): </td>
            <td class="table-data">{{ status.data.Strategy.mtd }}</td>
          </tr>
          <tr>
            <td>Three months: </td>
            <td class="table-data">{{ status.data.Strategy.three_month }}</td>
          </tr>
          <tr>
            <td>Six months: </td>
            <td class="table-data">{{ status.data.Strategy.six_month }}</td>
          </tr>
          <tr>
            <td>YTD (Year to date): </td>
            <td class="table-data">{{ status.data.Strategy.ytd }}</td>
          </tr>
          <tr>
            <td>One year: </td>
            <td class="table-data">{{ status.data.Strategy.one_year }}</td>
          </tr>
          <tr>
            <td>Three years: </td>
            <td class="table-data">{{ status.data.Strategy.three_year }}</td>
          </tr>
          <tr>
            <td>Five years: </td>
            <td class="table-data">{{ status.data.Strategy.five_year }}</td>
          </tr>
          <tr>
            <td>Ten years: </td>
            <td class="table-data">{{ status.data.Strategy.ten_year }}</td>
          </tr>
          <tr>
            <th colspan="2" class="text-center">Measures</th>
          </tr>
          <tr>
            <td>Daily sharpe: </td>
            <td class="table-data">{{ status.data.Strategy.daily_sharpe }}</td>
          </tr>
          <tr>
            <td>Daily sortino: </td>
            <td class="table-data">{{ status.data.Strategy.daily_sortino }}</td>
          </tr>
          <tr>
            <td>Daily mean: </td>
            <td class="table-data">{{ status.data.Strategy.daily_mean }}</td>
          </tr>
          <tr>
            <td>Daily vol: </td>
            <td class="table-data">{{ status.data.Strategy.daily_vol }}</td>
          </tr>
          <tr>
            <td>Daily skew: </td>
            <td class="table-data">{{ status.data.Strategy.daily_skew }}</td>
          </tr>
          <tr>
            <td>Daily kurt: </td>
            <td class="table-data">{{ status.data.Strategy.daily_kurt }}</td>
          </tr>
          <tr>
            <td>Monthly sharpe: </td>
            <td class="table-data">{{ status.data.Strategy.monthly_sharpe }}</td>
          </tr>
          <tr>
            <td>Monthly sortino: </td>
            <td class="table-data">{{ status.data.Strategy.monthly_sortino }}</td>
          </tr>
          <tr>
            <td>Monthly mean: </td>
            <td class="table-data">{{ status.data.Strategy.monthly_mean }}</td>
          </tr>
          <tr>
            <td>Monthly vol: </td>
            <td class="table-data">{{ status.data.Strategy.monthly_vol }}</td>
          </tr>
          <tr>
            <td>Monthly skew: </td>
            <td class="table-data">{{ status.data.Strategy.monthly_skew }}</td>
          </tr>
          <tr>
            <td>Monthly kurt: </td>
            <td class="table-data">{{ status.data.Strategy.monthly_kurt }}</td>
          </tr>
          <tr>
            <td>Yearly sharpe: </td>
            <td class="table-data">{{ status.data.Strategy.yearly_sharpe }}</td>
          </tr>
          <tr>
            <td>Yearly sortino: </td>
            <td class="table-data">{{ status.data.Strategy.yearly_sortino }}</td>
          </tr>
          <tr>
            <td>Yearly mean: </td>
            <td class="table-data">{{ status.data.Strategy.yearly_mean }}</td>
          </tr>
          <tr>
            <td>Yearly vol: </td>
            <td class="table-data">{{ status.data.Strategy.yearly_vol }}</td>
          </tr>
          <tr>
            <td>Yearly skew: </td>
            <td class="table-data">{{ status.data.Strategy.yearly_skew }}</td>
          </tr>
          <tr>
            <td>Yearly kurt: </td>
            <td class="table-data">{{ status.data.Strategy.yearly_kurt }}</td>
          </tr>
          <tr>
            <th colspan="2" class="text-center">Others</th>
          </tr>
          <tr>
            <td>Best day: </td>
            <td class="table-data">{{ status.data.Strategy.best_day }}</td>
          </tr>
          <tr>
            <td>Best month: </td>
            <td class="table-data">{{ status.data.Strategy.best_month }}</td>
          </tr>
          <tr>
            <td>Best year: </td>
            <td class="table-data">{{ status.data.Strategy.best_year }}</td>
          </tr>
          <tr>
            <td>Worst day: </td>
            <td class="table-data">{{ status.data.Strategy.worst_day }}</td>
          </tr>
          <tr>
            <td>Worst month: </td>
            <td class="table-data">{{ status.data.Strategy.worst_month }}</td>
          </tr>
          <tr>
            <td>Worst year: </td>
            <td class="table-data">{{ status.data.Strategy.worst_year }}</td>
          </tr>
        </table>
      </div>
    </div>
  </div>
</template>
<style scoped>
.table-data {
  border: 2px solid rgb(89, 199, 194);
}
table {
  padding: 5px
}
</style>