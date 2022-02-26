<template>
  <v-app id="app">
    <v-main>
      <Map />
    </v-main>
  </v-app>
</template>

<script>
import Map from "./components/Map";
// import NavBar from "./components/NavBar.vue";

export default {
  name: "App",

  components: {
    Map,
    // NavBar,
  },

  data: () => ({
    //
  }),
};
</script>
