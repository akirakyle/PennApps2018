from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('auth/', views.auth_page, name='auth_page'),
    path('my_info/', views.my_info, name='my_info'),
    path('my_songs/', views.my_songs, name='my_songs'),
    path('my_artists/', views.my_top_artists, name='my_artists'),
    path('my_related/', views.my_related_artist, name='my_artists')
]
