<template>
  <v-card height="100%" width="256" class="mx-left">
    <v-navigation-drawer permanent>
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="text-h6">
            検索条件を設定する
          </v-list-item-title>
          <!-- <v-list-item-subtitle> subtext </v-list-item-subtitle> -->
        </v-list-item-content>
      </v-list-item>
      <!-- {{ ledgers.order_no }} -->
      <v-divider></v-divider>

      <v-row align="center">
        <v-col cols="6">
          <v-subheader> 区分を選択する </v-subheader>
          <!-- <p>{{ ledgers }}</p> -->
        </v-col>
        <v-col cols="6">
          <v-select
            v-model="e1"
            :items="states"
            menu-props="auto"
            label="Select"
            hide-details
            prepend-icon="mdi-map"
            single-line
          ></v-select>
        </v-col>
        <v-col cols="6">
          <v-subheader> 日付を選択する </v-subheader>
        </v-col>
        <v-col cols="6">
          <v-select
            v-model="e2"
            :items="states"
            menu-props="auto"
            label="Select"
            hide-details
            prepend-icon="mdi-calendar"
            single-line
          ></v-select>
        </v-col>
      </v-row>
      <v-row justify="center">
        <v-btn v-on:click="$emit('onMapView')">検索する</v-btn>
      </v-row>
    </v-navigation-drawer>
  </v-card>
</template>
<script>
export default {
  name: "SideMenu",
  props: ["ledgers"],
  data() {
    return {
      right: null,
      e1: "Alabama",
      e2: "Texas",
      e3: null,
      e4: null,
      states: [
        "Alabama",
        "Alaska",
        "American Samoa",
        "Arizona",
        "Arkansas",
        "California",
        "Colorado",
        "Connecticut",
        "Delaware",
        "District of Columbia",
        "Federated States of Micronesia",
        "Florida",
        "Georgia",
        "Guam",
        "Hawaii",
        "Idaho",
        "Illinois",
        "Indiana",
        "Iowa",
        "Kansas",
        "Kentucky",
        "Louisiana",
        "Maine",
        "Marshall Islands",
        "Maryland",
        "Massachusetts",
        "Michigan",
        "Minnesota",
        "Mississippi",
        "Missouri",
        "Montana",
        "Nebraska",
        "Nevada",
        "New Hampshire",
        "New Jersey",
        "New Mexico",
        "New York",
        "North Carolina",
        "North Dakota",
        "Northern Mariana Islands",
        "Ohio",
        "Oklahoma",
        "Oregon",
        "Palau",
        "Pennsylvania",
        "Puerto Rico",
        "Rhode Island",
        "South Carolina",
        "South Dakota",
        "Tennessee",
        "Texas",
        "Utah",
        "Vermont",
        "Virgin Island",
        "Virginia",
        "Washington",
        "West Virginia",
        "Wisconsin",
        "Wyoming",
      ],
    };
  },
};
</script>
