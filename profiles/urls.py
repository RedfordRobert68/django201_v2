from django.urls import path
from . import views
from profiles import views as profile_views

app_name = "profiles"

urlpatterns = [
    path("<str:username>/", views.ProfileDetailView.as_view(), name="detail"),
    path("<str:username>/follow/", views.FollowView.as_view(), name="follow"),
    path("update/", profile_views.profile, name="profile_update"),
]