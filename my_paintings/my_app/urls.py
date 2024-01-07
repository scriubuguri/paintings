from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="my-home-page"),
    path("about-me/", views.about_me, name="about-me"),
    path('my-paintings/', views.my_paintings, name="my-paintings"),
    path("my-tools/", views.my_tools, name="my-tools"),
]
