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
      <div class="col-6">
        <table class="table" style="color: rgb(181, 203, 198)">
          <tr>
            <th colspan="2" class="text-center">Basic Info</th>
          </tr>
          <tr>
            <td>Start Date: </td>
            <td class="table-data">{{ status.data[Object.keys(status.data)[1]].start }}</td>
          </tr>
          <tr>
            <td>End Date: </td>
            <td class="table-data">{{ status.data[Object.keys(status.data)[1]].end }}</td>
          </tr>
          <tr>
            <td>Total Return: </td>
            <td class="table-data">{{ status.data[Object.keys(status.data)[1]].total_return }}</td>
          </tr>
          <tr>
            <td>CAGR (Compound annual growth rate): </td>
            <td class="table-data">{{ status.data[Object.keys(status.data)[1]].cagr }}</td>
          </tr>
          <tr>
            <th colspan="2" class="text-center">Risk-adjusted Ratios</th>
          </tr>
          <tr>
            <td>Max Drawdown: </td>
            <td class="table-data">{{ status.data[Object.keys(status.data)[1]].max_drawdown }}</td>
          </tr>
          <tr>
            <td>Calmar ratio: </td>
            <td class="table-data">{{ status.data[Object.keys(status.data)[1]].calmar }}</td>
          </tr>
          <tr>
            <th colspan="2" class="text-center">Interest Rate</th>
          </tr>
          <tr>
            <td>MTD (Month to date): </td>
            <td class="table-data">{{ status.data[Object.keys(status.data)[1]].mtd }}</td>
          </tr>
          <tr>
            <td>Three months: </td>
            <td class="table-data">{{ status.data[Object.keys(status.data)[1]].three_month }}</td>
          </tr>
          <tr>
            <td>Six months: </td>
            <td class="table-data">{{ status.data[Object.keys(status.data)[1]].six_month }}</td>
          </tr>
          <tr>
            <td>YTD (Year to date): </td>
            <td class="table-data">{{ status.data[Object.keys(status.data)[1]].ytd }}</td>
          </tr>
          <tr>
            <td>One year: </td>
            <td class="table-data">{{ status.data[Object.keys(status.data)[1]].one_year }}</td>
          </tr>
          <tr>
            <td>Three years: </td>
            <td class="table-data">{{ status.data[Object.keys(status.data)[1]].three_year }}</td>
          </tr>
          <tr>
            <td>Five years: </td>
            <td class="table-data">{{ status.data[Object.keys(status.data)[1]].five_year }}</td>
          </tr>
          <tr>
            <td>Ten years: </td>
            <td class="table-data">{{ status.data[Object.keys(status.data)[1]].ten_year }}</td>
          </tr>
        </table>
      </div>
      <div class="col-6">
        <table class="table" style="color: rgb(181, 203, 198)">
          <tr>
            <th colspan="4" class="text-center">Measures</th>
          </tr>
          <tr>
            <td></td>
            <td>Daily</td>
            <td>Monthly</td>
            <td>Yearly</td>
          </tr>
          <tr>
            <td>Sharpe: </td>
            <td class="table-data">{{ status.data[Object.keys(status.data)[1]].daily_sharpe }}</td>
            <td class="table-data">{{ status.data[Object.keys(status.data)[1]].monthly_sharpe }}</td>
            <td class="table-data">{{ status.data[Object.keys(status.data)[1]].yearly_sharpe }}</td>
          </tr>
          <tr>
            <td>Sortino: </td>
            <td class="table-data">{{ status.data[Object.keys(status.data)[1]].daily_sortino }}</td>
            <td class="table-data">{{ status.data[Object.keys(status.data)[1]].monthly_sortino }}</td>
            <td class="table-data">{{ status.data[Object.keys(status.data)[1]].yearly_sortino }}</td>
          </tr>
          <tr>
            <td>Mean: </td>
            <td class="table-data">{{ status.data[Object.keys(status.data)[1]].daily_mean }}</td>
            <td class="table-data">{{ status.data[Object.keys(status.data)[1]].monthly_mean }}</td>
            <td class="table-data">{{ status.data[Object.keys(status.data)[1]].yearly_mean }}</td>
          </tr>
          <tr>
            <td>Vol: </td>
            <td class="table-data">{{ status.data[Object.keys(status.data)[1]].daily_vol }}</td>
            <td class="table-data">{{ status.data[Object.keys(status.data)[1]].monthly_vol }}</td>
            <td class="table-data">{{ status.data[Object.keys(status.data)[1]].yearly_vol }}</td>
          </tr>
          <tr>
            <td>Skew: </td>
            <td class="table-data">{{ status.data[Object.keys(status.data)[1]].daily_skew }}</td>
            <td class="table-data">{{ status.data[Object.keys(status.data)[1]].monthly_skew }}</td>
            <td class="table-data">{{ status.data[Object.keys(status.data)[1]].yearly_skew }}</td>
          </tr>
          <tr>
            <td>Daily kurt: </td>
            <td class="table-data">{{ status.data[Object.keys(status.data)[1]].daily_kurt }}</td>
            <td class="table-data">{{ status.data[Object.keys(status.data)[1]].monthly_kurt }}</td>
            <td class="table-data">{{ status.data[Object.keys(status.data)[1]].yearly_kurt }}</td>
          </tr>
        </table>
        <table class="table" style="color: rgb(181, 203, 198)">
          <tr>
            <th colspan="2" class="text-center">Others</th>
          </tr>
          <tr>
            <td>Best day: </td>
            <td class="table-data">{{ status.data[Object.keys(status.data)[1]].best_day }}</td>
          </tr>
          <tr>
            <td>Best month: </td>
            <td class="table-data">{{ status.data[Object.keys(status.data)[1]].best_month }}</td>
          </tr>
          <tr>
            <td>Best year: </td>
            <td class="table-data">{{ status.data[Object.keys(status.data)[1]].best_year }}</td>
          </tr>
          <tr>
            <td>Worst day: </td>
            <td class="table-data">{{ status.data[Object.keys(status.data)[1]].worst_day }}</td>
          </tr>
          <tr>
            <td>Worst month: </td>
            <td class="table-data">{{ status.data[Object.keys(status.data)[1]].worst_month }}</td>
          </tr>
          <tr>
            <td>Worst year: </td>
            <td class="table-data">{{ status.data[Object.keys(status.data)[1]].worst_year }}</td>
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