from django.urls import path, include
import main.views as main_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', main_views.home, name="home"),
    path('', include("django.contrib.auth.urls")),
    path('signup', main_views.signup_view, name="signup_view"),
    path('profile', main_views.profile_view, name="profile_view"),
    path('preferences', main_views.preferences, name="preferences"),
    path('recommendation', main_views.userChoices, name="recommendation"),
    path('posts', main_views.post_comment_create_and_list_view, name="posts"),
    path('liked', main_views.like_unlike_post, name = "like_posts"),
    path('signup/', main_views.signup_view, name="signup_view"),
    path('profile/', main_views.profile_view, name="profile_view"),
    path('preferences/', main_views.preferences, name="preferences"),
    path('recommendation/', main_views.userChoices, name="recommendation"),
    path('posts/', main_views.post_comment_create_and_list_view, name="posts"),
    path('liked/', main_views.like_unlike_post, name = "like_posts"),
    path('disliked/', main_views.dislike_undislike_post, name = "dislike_posts"),
    path('editprofile/', main_views.editProfile, name = "editProfile"),
    path('createpost/', main_views.create_posts, name="create_posts"),
]