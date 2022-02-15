module.exports = {
  transpileDependencies: ["vuetify"],
  devServer: {
    proxy: {
      "/ledger/": {
        target: "http://localhost:5000",
        pathRewrite: { "^/ledger/": "" },
      },
    },
  },
};
