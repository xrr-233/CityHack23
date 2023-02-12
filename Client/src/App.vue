<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header class="container-fluid fixed-top" style="height: 50px; background-color: black">
    <div class="row" style="width: 100%; height: 100%;">
      <div class="col-1"  style="height: 100%;">
        <img alt="Vue logo" class="logo mx-auto p-2" src="@/assets/logo.svg" style="height: 100%;" />
      </div>

      <div class="col-11 wrapper">
        <h2 style="line-height: 50px; color: rgb(89, 199, 194)">User-friendly Trading Platform</h2>

  <!--      <nav>-->
  <!--        <RouterLink to="/">Home</RouterLink>-->
  <!--        <RouterLink to="/about">About</RouterLink>-->
  <!--      </nav>-->

      </div>
    </div>
  </header>

  <div class="container">
    <RouterView />
  </div>

</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    /*padding-right: calc(var(--section-gap) / 2);*/
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>
