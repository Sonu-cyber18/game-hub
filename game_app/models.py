# myapp/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Profile settings
    profile_picture = models.ImageField(upload_to='profile_pics/', default='profile_pics/default.svg')
    bio = models.TextField(max_length=500, blank=True)
    region = models.CharField(max_length=10, default='eu')

    # Gameplay settings
    game_difficulty = models.CharField(max_length=10, default='medium')
    control_scheme = models.CharField(max_length=10, default='default')
    invert_y_axis = models.BooleanField(default=True)
    show_tutorials = models.BooleanField(default=False)
    enable_subtitles = models.BooleanField(default=True)
    motion_blur = models.BooleanField(default=False)
    master_volume = models.PositiveIntegerField(default=75)

    # Privacy settings
    profile_visibility = models.CharField(max_length=10, default='public')
    show_online_status = models.BooleanField(default=True)
    show_game_activity = models.BooleanField(default=True)
    allow_friend_requests = models.BooleanField(default=True)
    allow_messages = models.BooleanField(default=True)
    share_analytics = models.BooleanField(default=True)
    share_gameplay_data = models.BooleanField(default=False)

    def __str__(self):
        return self.username