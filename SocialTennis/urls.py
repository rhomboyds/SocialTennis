from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup', views.signup),
    path('home', views.home),
    path('login', auth_views.LoginView.as_view(template_name='login.html', redirect_field_name='home')),
    path('friend', views.friend),
    path('event/<slug:server>/<int:friend_id>', views.event),
]
