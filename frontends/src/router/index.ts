import { createRouter, createWebHistory } from "vue-router";
import PageNotFound from "../views/PageNotFound.vue";
import HomeView from "../views/HomeView.vue";
import HomePlaceholder from '../views/HomePlaceholder.vue';
import ArtistView from "../views/ArtistView.vue";
// import PortfolioView from "../views/PortfolioView.vue";

const router = createRouter({
  history: createWebHistory('/'),
  routes: [
    {
      path: "/",
      name: "placeholder",
      component: HomePlaceholder,
    },
    {
      path: "/home",
      name: "home",
      component: HomeView,
    },
    {
      path: "/a/:artist",
      name: "artist",
      component: ArtistView,
      // component: () => import("../views/ArtistView.vue"),
      // children: [
      //   {
      //     path: 'p/:portfolio_type/:portfolio_id',
      //     name: 'artist_portfolio',
      //     component: PortfolioView,
      //   }
      // ],
    },
    { path: "/:pathMatch(.*)*", component: PageNotFound }
  ],
});

export default router;
