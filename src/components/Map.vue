<template>
  <div style="height: 100%; width: 100%">
    <!-- <v-col cols="ledgers.length"> -->
    <!-- <v-select
        :items="ledgers[i].order_no"
        menu-props="auto"
        label="Select"
        hide-details
        prepend-icon="mdi-map"
        single-line
      ></v-select> -->
    <v-btn @click="onMapView()" markerLatLng>button</v-btn>
    {{ ledgers.length }}
    <!-- </v-col> -->
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

      <l-marker
        v-for="ledger in ledgers"
        :key="ledger.order_no"
        :lat-lng="[ledger.lat, ledger.lng]"
      >
        <l-tooltip :options="{ permanent: true, interactive: true }">
          <div>
            <v-card>
              <v-toolbar color="orange" dark dense flat>
                <v-toolbar-title class="text-body-2">
                  Memo Space
                </v-toolbar-title>
              </v-toolbar>
              <v-card-text><input placeholder="edit me" /> </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-icon large> mdi-chevron-right </v-icon>
              </v-card-actions>
            </v-card>
            <v-card>
              <v-card-text
                >受付番号:{{ ledger.order_no }}<br />
                日付:{{ ledger.datatime }}<br />
                大区分：{{ ledger.primary_category }}<br />
                中区分：{{ ledger.secondary_category }}<br />
                内容：{{ ledger.contents }}<br />
                回答：{{ ledger.answer }}<br />
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-icon large> mdi-chevron-right </v-icon>
              </v-card-actions>
            </v-card>
          </div>
        </l-tooltip>
      </l-marker>
    </l-map>
  </div>
</template>

<script>
import { latLng } from "leaflet";
import { LMap, LTileLayer, LMarker, LTooltip } from "vue2-leaflet";
// import LDrawToolbar from "vue2-leaflet-draw-toolbar";
import axios from "axios";
// import ToolBar from "./ToolBar";
// import SideMenu from "./SideMenu";
export default {
  name: "Map",
  components: {
    LMap,
    LTileLayer,
    LMarker,
    // LPopup,
    LTooltip,
    // LDrawToolbar,
    // ToolBar,
    // SideMenu,
  },
  data() {
    return {
      ledgers: [
        {
          // order_no: "",
          // datatime: "",
          // primary_category: "",
          // secondary_category: "",
          // contents: "",
        },
      ],
      zoom: 13,
      center: latLng(42.8209, 141.6508),
      url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
      attribution:
        '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      // markerLatLng: [42.8209, 141.6508],
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
    onMapView() {
      for (var i = 0; i <= 20; i++) {
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
              lat: 42.8209,
              lng: 141.6508,
            });
            console.log(this.ledgers);
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
