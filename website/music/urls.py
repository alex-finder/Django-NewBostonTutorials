from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    # / music /
    path('', views.index, name='index'),

    # music/{AlbumId}/
    # path(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    path('<int:album_id>', views.detail, name='Music Album Details')
]
