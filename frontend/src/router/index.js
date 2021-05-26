import { createWebHistory, createRouter } from "vue-router"
import Home from "@/components/Home"
import Musician from "@/components/Musician";
import Traveler from "@/components/Traveler";
import PageNotFound from "@/components/PageNotFound";
import Writer from "@/components/Writer";
import MusicPage from "@/components/MusicPage";
import PicAlbumPage from "@/components/PicAlbumPage";

const routes = [
    {
        path: "/",
        name: "Home",
        component: Home,
    },
    {
        path: "/music",
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
        path: "/music_details",
        name: "Music_details",
        component: MusicPage,
    },
    {
        path: "/album_details",
        name: "Album_details",
        component: PicAlbumPage
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