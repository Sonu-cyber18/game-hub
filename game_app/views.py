from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from .models import CustomUser
from .forms import ProfileSettingsForm, GameplaySettingsForm, PrivacySettingsForm
from django import forms
from django.contrib.auth.forms import UserCreationForm

# Custom User Creation Form
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')  # Include any additional fields you need

def home_view(request):
    print("Reached")
    """View for root URL (/)"""
    return render(request, 'home.html')

@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')

def login_view(request):
    print("Login view called")  # Debug print
    if request.user.is_authenticated:
        print("User is already authenticated")  # Debug print
        return redirect('dashboard')
        
    if request.method == 'POST':
        print("POST request received")  # Debug print
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            print("Form is valid")  # Debug print
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                print("User authenticated successfully")  # Debug print
                auth_login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                next_url = request.POST.get('next', 'dashboard')
                print(f"Redirecting to: {next_url}")  # Debug print
                return redirect(next_url)
            else:
                print("Authentication failed")  # Debug print
        else:
            print("Form is invalid")  # Debug print
            print(form.errors)  # Debug print
            messages.error(request, "Invalid username or password.")
    else:
        print("GET request received")  # Debug print
        form = AuthenticationForm()
    
    return render(request, 'registration/login.html', {'form': form})

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)  # Use your custom form
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('dashboard')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomUserCreationForm()  # Use your custom form
    
    return render(request, 'registration/signup.html', {'form': form})

def snake_game_view(request):
    return render(request, 'game.html')

def chess_game_view(request):
    return render(request, 'chess_game.html')

def puzzle_game(request):
    return render(request, 'puzzel_game.html')

def pacman_game(request):
    return render(request, 'pacman-game.html')

def _get_neon_rush_high_scores():
    """
    Placeholder data for the Neon Rush leaderboard.
    Replace with real persistence once a score model exists.
    """
    return [
        {"player_name": "NeonNova", "score": 12480},
        {"player_name": "CyberDrift", "score": 11890},
        {"player_name": "PhotonRacer", "score": 11240},
        {"player_name": "LumaDash", "score": 10980},
        {"player_name": "VoidRunner", "score": 10150},
    ]

def neon_car_racing_view(request):
    """Render the neon car racing experience."""
    context = {
        "high_scores": _get_neon_rush_high_scores(),
    }
    return render(request, 'neon_car_racing.html', context)

def leaderboard_view(request):
    """Display the Neon Rush leaderboard page."""
    return render(request, 'leaderboard.html', {
        "high_scores": _get_neon_rush_high_scores()
    })

def jumanji_game_view(request):
    return render(request, 'jumanji_game.html')

def memory_game_view(request):
    return render(request, 'memory_game.html')
def flappy_bird_game_view(request):
    return render(request, 'flappy_bird.html')

def python_learning_game_view(request):
    return render(request, 'python_learning_game.html')
def level_devil_view(request):
    return render(request, 'level_devil.html')
def troll_peril_view(request):
    return render(request, 'troll_peril.html')

def escape_view(request):
    return render(request, 'escape.html')

def logout_view(request):
    auth_logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')

@login_required
def profile_view(request):
    if request.method == 'POST':
        # Determine which form is being submitted
        if 'save_profile' in request.POST:
            form = ProfileSettingsForm(request.POST, request.FILES, instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your profile settings have been updated.')
                return redirect('profile')
        elif 'save_gameplay' in request.POST:
            form = GameplaySettingsForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your gameplay settings have been updated.')
                return redirect('profile')
        elif 'save_privacy' in request.POST:
            form = PrivacySettingsForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your privacy settings have been updated.')
                return redirect('profile')

    profile_form = ProfileSettingsForm(instance=request.user)
    gameplay_form = GameplaySettingsForm(instance=request.user)
    privacy_form = PrivacySettingsForm(instance=request.user)

    return render(request, 'profile.html', {
        'profile_form': profile_form,
        'gameplay_form': gameplay_form,
        'privacy_form': privacy_form,
        'user': request.user
    })