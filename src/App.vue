<template>
  <v-app id="app">
    <NavBar />
    <v-navigation-drawer
      v-bind:permanent="true"
      v-bind:fixed="true"
      v-bind:app="true"
    >
      <SideMenu />
    </v-navigation-drawer>
    <v-main>
      <Map />
    </v-main>
  </v-app>
</template>

<script>
import Map from "./components/Map";
import NavBar from "./components/NavBar.vue";
import SideMenu from "./components/SideMenu.vue";

export default {
  name: "App",

  components: {
    Map,
    SideMenu,
    NavBar,
  },

  data: () => ({
    //
  }),
};
</script>
