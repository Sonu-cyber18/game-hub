from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('game/', views.snake_game_view, name='snake-game'),
    path('chess-game/', views.chess_game_view, name='chess-game'),
    path('puzzle-game/', views.puzzle_game, name='puzzle-game'),
    path('pacman-game/', views.pacman_game, name='pacman-game'),
    path('neon-car-racing/', views.neon_car_racing_view, name='neon-car-racing'),
    path('jumanji-game/', views.jumanji_game_view, name='jumanji-game'),
    path('memory-game/', views.memory_game_view, name='memory-game'),
    path('flappy-bird/', views.flappy_bird_game_view, name='flappy-bird'),
    path('level-devil/', views.level_devil_view, name='level-devil'),
    path('troll-peril/', views.troll_peril_view, name='troll-peril'),
    path('escape/', views.escape_view, name='escape'),
    path("python-learning-game/", views.python_learning_game_view, name="python-learning-game"),
]