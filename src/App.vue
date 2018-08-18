<template>
  <div id="app">
    <router-view/>
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
  background-color: black;
  padding: 0;
  margin: 0;
  position: fixed;
  width: 100%;
  height: 100%;
  overflow-x: hidden;
}

.container {
  padding: 0;
  margin: 0;
  width: 100%;
  height: 100%;
}
</style>

