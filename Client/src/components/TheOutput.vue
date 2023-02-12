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
    Start Date: {{ status.data.start }}
    End Date: {{ status.data.end }}
    Total Return: {{ status.data.total_return }}

    CAGR (Compound annual growth rate): {{ status.data.cagr }}
    Max Drawdown: {{ status.data.max_drawdown }}
    Calmar ratio: {{ status.data.calmar }}

    mtd: {{ status.data.mtd }}
    three month: {{ status.data.three_month }}
    six m: {{ status.data.six_month }}
    ytd: {{ status.data.ytd }}
    one year: {{ status.data.one_year }}
    3 y: {{ status.data.three_year }}
    5 y: {{ status.data.six_year }}
    10 y: {{ status.data.ten_year }}

    daily sharpe {{ status.data.daily_sharpe }}
    daily sortino {{ status.data.daily_sortino }}
    daily mean {{ status.data.daily_mean }}
    daily vol {{ status.data.daily_vol }}
    daily skew {{ status.data.daily_skew }}
    daily kurt {{ status.data.daily_kurt }}
    monthly sharpe {{ status.data.monthly_sharpe }}
    monthly sortino {{ status.data.monthly_sortino }}
    monthly mean {{ status.data.monthly_mean }}
    monthly vol {{ status.data.monthly_vol }}
    monthly skew {{ status.data.monthly_skew }}
    monthly kurt {{ status.data.monthly_kurt }}
    yearly sharpe {{ status.data.yearly_sharpe }}
    yearly sortino {{ status.data.yearly_sortino }}
    yearly mean {{ status.data.yearly_mean }}
    yearly vol {{ status.data.yearly_vol }}
    yearly skew {{ status.data.yearly_skew }}
    yearly kurt {{ status.data.yearly_kurt }}

    best day {{ status.data.best_day }}
    best month {{ status.data.best_month }}
    best year {{ status.data.best_year }}
    worst day {{ status.data.worst_day }}
    worst month {{ status.data.worst_month }}
    worst year {{ status.data.worst_year }}

  </div>
</template>

<style scoped>

</style>