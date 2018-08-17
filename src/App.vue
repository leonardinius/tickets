<template>
  <div id="app">
    <router-view/>
    <!-- 
      <div id="nav">
      <router-link to="/">Scanner</router-link> |
      <router-link to="/about">About</router-link>
    </div>  
    -->
  </div>
</template>

<style lang="scss">
@import "~bootstrap/scss/bootstrap.scss";

#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  // padding-bottom: 15px;
}
// #nav {
//   padding: 30px;
// }

// #nav a {
//   font-weight: bold;
//   color: #2c3e50;
// }

// #nav a.router-link-exact-active {
//   color: #42b983;
// }
</style>

