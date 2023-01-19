from django.contrib import admin
from django.urls import path

from poll import views as poll_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', poll_views.home, name='home'),
    path('create/', poll_views.create, name='create'),
    path('results/', poll_views.results, name='results'),
    path('vote/', poll_views.vote, name='vote'),
    path('welcome/',poll_views.welcome),
    path('signup/',poll_views.signup),
    path('login/', poll_views.login),
    path('logout/', poll_views.logout),
    path('',poll_views.welcome),
]