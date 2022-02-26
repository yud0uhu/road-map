<template>
  <div style="height: 100%; width: 100%">
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
      <SideMenu @onMapView="onMapView" />
      <l-tile-layer :url="url" :attribution="attribution" />
      <div v-for="ledger in ledgers" :key="ledger.order_no">
        {{ ledgers.length }}
        <!-- </v-col> -->
        <!-- TIPS:lat-lngは配列の第一要素、第二要素を緯度、経度とし直接渡すことができる -->
        <l-marker :lat-lng="markerLatLng">
          <l-tooltip :options="{ permanent: true, interactive: true }">
            <!-- ポップアップメニュー -->
            <div>
              <v-card>
                <v-card-text>
                  <!-- {{ ledger.order_no }}<br /> -->
                  {{ ledger.datatime }}<br />
                  {{ ledger.primary_category }}<br />
                  {{ ledger.secondary_category }}<br />
                  <!-- {{ ledger.contents }}<br /> -->
                  <!-- {{ ledger.answer }}<br /> -->
                </v-card-text>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-icon large> mdi-chevron-right </v-icon>
                </v-card-actions>
              </v-card>
            </div>
          </l-tooltip>
        </l-marker>
      </div>
    </l-map>
  </div>
</template>

<script>
import { latLng } from "leaflet";
import { LMap, LTileLayer, LMarker, LTooltip } from "vue2-leaflet";
// import LDrawToolbar from "vue2-leaflet-draw-toolbar";
import axios from "axios";
import SideMenu from "./SideMenu.vue";
export default {
  name: "Map",
  components: {
    LMap,
    LTileLayer,
    LMarker,
    LTooltip,
    SideMenu,
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
          // lat: 42.8209,
          // lng: 141.6508,
        },
      ],
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
      // 初期値は非表示
      onView: false,
    };
  },
  methods: {
    zoomUpdate(zoom) {
      this.currentZoom = zoom;
    },
    centerUpdate(center) {
      this.currentCenter = center;
    },
    onViewMode(onView) {
      this.onView = !onView;
    },
    // markerLatLngを引数で受け取った値に更新
    latLngUpdate(lat, lng) {
      this.markerLatLng[0] += lat * 0.1 + 0.1;
      this.markerLatLng[1] -= lng * 0.1 - 0.1;
      console.log(this.markerLatLng);
    },
    onMapView(onView) {
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
            });
            console.log(this.ledgers);
            // Triger切り替え
            this.onViewMode(onView);
            // TODO: lat/lngは毎回一意の値にしたい
            // ここで更新したい一意の値を渡す
            this.latLngUpdate(0.1, 0.1);
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
