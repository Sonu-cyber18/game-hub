from django import forms
from .models import CustomUser

class ProfileSettingsForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'bio', 'region', 'profile_picture']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'region': forms.Select(attrs={'class': 'form-control'}),
            'profile_picture': forms.FileInput(attrs={'style': 'display: none;', 'id': 'avatarUpload'}),
        }

class GameplaySettingsForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'game_difficulty', 'control_scheme', 'invert_y_axis',
            'show_tutorials', 'enable_subtitles', 'motion_blur', 'master_volume'
        ]
        widgets = {
            'game_difficulty': forms.Select(attrs={'class': 'form-control'}),
            'control_scheme': forms.Select(attrs={'class': 'form-control'}),
            'invert_y_axis': forms.CheckboxInput(attrs={'class': 'checkbox'}),
            'show_tutorials': forms.CheckboxInput(attrs={'class': 'checkbox'}),
            'enable_subtitles': forms.CheckboxInput(attrs={'class': 'checkbox'}),
            'motion_blur': forms.CheckboxInput(attrs={'class': 'checkbox'}),
            'master_volume': forms.NumberInput(attrs={'class': 'form-control', 'type': 'range', 'min': '0', 'max': '100'}),
        }

class PrivacySettingsForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'profile_visibility', 'show_online_status', 'show_game_activity',
            'allow_friend_requests', 'allow_messages', 'share_analytics', 'share_gameplay_data'
        ]
        widgets = {
            'profile_visibility': forms.Select(attrs={'class': 'form-control'}),
            'show_online_status': forms.CheckboxInput(attrs={'class': 'checkbox'}),
            'show_game_activity': forms.CheckboxInput(attrs={'class': 'checkbox'}),
            'allow_friend_requests': forms.CheckboxInput(attrs={'class': 'checkbox'}),
            'allow_messages': forms.CheckboxInput(attrs={'class': 'checkbox'}),
            'share_analytics': forms.CheckboxInput(attrs={'class': 'checkbox'}),
            'share_gameplay_data': forms.CheckboxInput(attrs={'class': 'checkbox'}),
        }