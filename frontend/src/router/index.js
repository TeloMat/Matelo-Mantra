import { createWebHistory, createRouter } from "vue-router"
import Home from "@/components/Home"
import Musician from "@/components/Musician";
import Traveler from "@/components/Traveler";
import PageNotFound from "@/components/PageNotFound";
import Writer from "@/components/Writer";

const routes = [
    {
        path: "/",
        name: "Home",
        component: Home,
    },
    {
        path: "/musician",
        name: "Musician",
        component: Musician,
    },
    {
        path: "/travels",
        name: "Travels",
        component: Traveler,
    },
    {
        path: '/writer',
        name: 'Writer',
        component: Writer,
    },
    {
        path: '/:catchAll(.*)*',
        name: "PageNotFound",
        component: PageNotFound,
    },
]



const router = createRouter({
  history: createWebHistory(),
    routes
})


export default router