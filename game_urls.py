from django.urls import path
from . import views

app_name = "game"

urlpatterns = [
    path("leaderboard/", views.leaderboard_view, name="leaderboard"),
]

