<template>
  <div style="height: 100%; width: 100%">
    <v-btn @click="counterUpdate">Add memo</v-btn>
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
      <l-marker :lat-lng="withTooltip">
        <l-tooltip
          :options="{ permanent: true, interactive: true }"
          v-if="counter > 0"
        >
          <div>
            <v-card>
              <v-toolbar color="orange" dark dense flat>
                <v-toolbar-title class="text-body-2">
                  Memo Space
                </v-toolbar-title>
              </v-toolbar>
              <v-card-text
                ><input v-model="message" placeholder="edit me" />
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-icon large @click="next"> mdi-chevron-right </v-icon>
              </v-card-actions>
            </v-card>
            <v-card>
              <v-card-text
                >受付番号:{{ data.order_no }}<br />
                日付:{{ data.datatime }}<br />
                大区分：{{ data.primary_category }}<br />
                中区分：{{ data.secondary_category }}<br />
                内容：{{ data.contents }}<br />
                回答：{{ data.answer }}<br />
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-icon large @click="next"> mdi-chevron-right </v-icon>
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
      zoom: 13,
      center: latLng(42.8209, 141.6508),
      url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
      attribution:
        '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      withPopup: latLng(42.8209, 141.6508),
      withTooltip: latLng(42.8209, 141.6508),
      currentZoom: 11.5,
      currentCenter: latLng(42.8209, 141.6508),
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
    // showLongText() {
    //   this.showParagraph = !this.showParagraph;
    // },
    counterUpdate() {
      this.counter += 1;
      console.log("Update:" + this.counter);
    },
    // innerClick() {
    //   alert("Click!");
    // },
  },
  mounted() {
    axios
      .get("https://road-map-analyze.herokuapp.com/ledger/12/")
      .then((response) => {
        this.data = response.data;
        console.log(this.data);
      })
      .catch((error) => {
        console.log(error);
        this.errored = true;
      })
      .finally(() => (this.loading = false));
  },
};
</script>

<style></style>
