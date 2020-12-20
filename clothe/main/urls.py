from main.views import signup_view
from django.urls import path, include
import main.views as main_views

urlpatterns = [
    path('', main_views.home, name="home"),
    path('signup/', main_views.signup_view, name="signup_view"),
    path('profile/', main_views.profile_view, name="profile_view"),
    path('preferences/', main_views.preferences, name="preferences"),
    path('recommendation/', main_views.userChoices, name="recommendation"),
    path('posts/', main_views.post_comment_create_and_list_view, name="posts"),
    path('liked/', main_views.like_unlike_post, name = "like_posts"),
    path('disliked/', main_views.dislike_undislike_post, name = "dislike_posts"),
]