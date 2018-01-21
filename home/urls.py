from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('auth/', views.auth_page, name='auth_page'),
    path('the_thing/', views.do_the_thing, name='the_thing'),
    path('liked/', views.liked, name='liked'),
    path('disliked/', views.disliked, name='disliked'),
    path('artists/<slug:artist_id>', views.detail, name='detail')
]
