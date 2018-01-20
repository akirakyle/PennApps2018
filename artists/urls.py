from django.urls import path

from . import views

urlpatterns = [
            path('<int:artist_id>', views.detail, name='detail'),
            ]
