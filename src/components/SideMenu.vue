<template>
  <v-card height="100%" width="256" class="mx-left">
    <v-navigation-drawer
      v-bind:permanent="true"
      v-bind:fixed="true"
      v-bind:app="true"
    >
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="text-h6">
            検索条件を指定する
          </v-list-item-title>
          <!-- <v-list-item-subtitle> subtext </v-list-item-subtitle> -->
        </v-list-item-content>
      </v-list-item>
      <!-- {{ ledgers }} -->
      <v-divider></v-divider>
      <v-treeview :items="items"></v-treeview>
      <v-row justify="center">
        <!-- ボタンが発火されたタイミングでAPIからデータを取得する -->
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
      // 初期値は非表示
      // onView: false,
      items: [
        {
          id: 1,
          name: "施設区分 :",
          children: [
            { id: 2, name: "Calendar : app" },
            { id: 3, name: "Chrome : app" },
            { id: 4, name: "Webstorm : app" },
          ],
        },
        {
          id: 5,
          name: "設備状況 :",
          children: [
            {
              id: 6,
              name: "vuetify :",
              children: [
                {
                  id: 7,
                  name: "src :",
                  children: [
                    { id: 8, name: "index : ts" },
                    { id: 9, name: "bootstrap : ts" },
                  ],
                },
              ],
            },
            {
              id: 10,
              name: "material2 :",
              children: [
                {
                  id: 11,
                  name: "src :",
                  children: [
                    { id: 12, name: "v-btn : ts" },
                    { id: 13, name: "v-card : ts" },
                    { id: 14, name: "v-window : ts" },
                  ],
                },
              ],
            },
          ],
        },
      ],
    };
  },
  methods: {
    // onViewMode() {
    //   this.onView = !this.onView;
    // },
  },
};
</script>
