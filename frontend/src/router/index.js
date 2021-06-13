import { createWebHistory, createRouter } from "vue-router"
import Home from "@/components/Home"
import Musician from "@/components/Musician/Musician";
import Traveler from "@/components/Traveler/Traveler";
import PageNotFound from "@/components/PageNotFound";
import Writer from "@/components/Writer/Writer";
import MusicPage from "@/components/Musician/MusicPage";
import PicAlbumPage from "@/components/Traveler/PicAlbumPage";
import PostPage from "@/components/Writer/PostPage";

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
        path: "/post_details",
        name: "Post_details",
        component: PostPage,
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