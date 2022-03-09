<template>
  <div style="height: 100%; width: 100%">
    <!-- {{ ledgers.length }} -->
    <v-card class="mx-auto overflow-hidden">
      <NavBar />
      <side-menu @onMapView="onMapView" :ledgers="ledgers" />
    </v-card>
    <v-card class="overflow-hidden"> </v-card>
    <l-map
      ref="map"
      v-if="showMap"
      :zoom="zoom"
      :center="center"
      :options="mapOptions"
      style="height: 100%"
      @update:center="centerUpdate"
      @update:zoom="zoomUpdate"
    >
      <l-tile-layer :url="url" :attribution="attribution" />

      <div v-for="ledger in ledgers" :key="ledger.order_no">
        <!-- </v-col> -->
        <!-- TIPS:lat-lngは配列の第一要素、第二要素を緯度、経度とし直接渡すことができる -->
        <l-marker :lat-lng="markerLatLng">
          <l-popup>
            <!-- ポップアップメニュー -->
            <!-- <v-card>
              <v-card-text> -->
            <!-- {{ ledger.order_no }}<br /> -->
            {{ ledger.datatime }}<br />
            {{ ledger.primary_category }}<br />
            {{ ledger.secondary_category }}<br />
            {{ ledger.contents }}<br />
            {{ ledger.answer }}<br />
            <!-- </v-card-text> -->
            <!-- <v-card-actions> -->
            <!-- <v-spacer></v-spacer> -->
            <!-- <v-icon large> mdi-chevron-right </v-icon> -->
            <!-- </v-card-actions> -->
            <!-- </v-card> -->
          </l-popup>
        </l-marker>
      </div>
    </l-map>
  </div>
</template>

<script>
import { latLng } from "leaflet";
import { LMap, LTileLayer, LMarker, LPopup } from "vue2-leaflet";
// import LDrawToolbar from "vue2-leaflet-draw-toolbar";
import axios from "axios";
import NavBar from "./NavBar.vue";
import SideMenu from "./SideMenu.vue";
export default {
  name: "Map",
  components: {
    LMap,
    LTileLayer,
    LMarker,
    LPopup,
    NavBar,
    SideMenu,
  },
  data() {
    return {
      latitude: 0,
      longitud: 0,
      collapseOnScroll: true,
      ledgers: [],
      zoom: 13,
      center: latLng(42.8209, 141.6508),
      url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
      attribution:
        '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      markerLatLng: [42.8209, 141.6508],
      // currentZoom: 11.5,
      // currentCenter: latLng(42.8209, 141.6508),
      showParagraph: false,
      mapOptions: {
        zoomSnap: 0.5,
      },
      showMap: true,
      counter: 0,
    };
  },
  methods: {
    zoomUpdate(zoom) {
      this.currentZoom = zoom;
    },
    centerUpdate(center) {
      this.currentCenter = center;
    },

    // markerLatLngを引数で受け取った値に更新
    latLngUpdate(lat, lng) {
      this.markerLatLng[0] = lat;
      this.markerLatLng[1] = lng;
      console.log(this.markerLatLng);
    },
    onMapView() {
      for (var i = 1; i <= 20; i++) {
        axios
          .get(`https://road-map-analyze.herokuapp.com/ledger/${i}/`)
          .then((response) => {
            this.ledgers.push({
              order_no: response.data.order_no,
              datatime: response.data.datatime,
              primary_category: response.data.primary_category,
              secondary_category: response.data.secondary_categorye,
              contents: response.data.contents,
              answer: response.data.answer,
              latitude: response.data.latitude,
              longitud: response.data.longitud,
            });
            // console.log(response.data.latitude, response.data.longitud);
            this.latitude = response.data.latitude;
            this.longitud = response.data.longitud;
            console.log(this.latitude, this.longitud);
            // TODO: lat/lngは毎回一意の値にしたい
            // ここで更新したい一意の値を渡す
            this.latLngUpdate(this.latitude, this.longitud);
          })
          .catch((error) => {
            console.log(error);
            this.errored = true;
          })
          .finally(() => (this.loading = false));
      }
    },
  },
};
</script>

<style></style>
