from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('signup/', signup_view, name="signup_view"),
    path('profile/', profile_view, name="profile_view"),
    path('preferences/', preferences, name="preferences"),
    path('recommendation/', userChoices, name="recommendation"),
    path('posts/', post_comment_create_and_list_view, name="posts"),
    path('liked/', like_unlike_post, name = "like_posts"),
    path('disliked/', dislike_undislike_post, name = "dislike_posts"),
    path('editprofile/', editProfile, name = "editProfile"),
    path('createpost/', create_posts, name="create_posts"),
    path('my-invites/', invites_received_view, name='my-invites-view'),
]