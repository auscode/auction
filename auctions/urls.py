from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.loginfxn, name="login"),
    path("logout", views.logoutfxn, name="logout"),
    path("register", views.register, name="register"),
    path("newListing", views.newListing, name="newListing"),
    path("listing/<str:listing_id>", views.listing, name="listing"),
    path(
        "remove_watchlist/<str:listing_id>",
        views.remove_watchlist,
        name="remove_watchlist",
    ),
    path("add_watchlist/<str:listing_id>", views.add_watchlist, name="add_watchlist"),
    path("bidding/<str:listing_id>", views.bidding, name="bidding"),
    path("closeBid/<str:listing_id>", views.closeBid, name="closeBid"),
    path("watch_list/<str:user_id>", views.watchlist, name="watchlist"),
    path("categories", views.category, name="categories"),
]
