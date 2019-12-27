
from django.urls import path
from . import views


app_name = 'music'


urlpatterns = [
    # /music/
    path('', views.IndexView.as_view() , name='index'),

    #/music/71/
    path('<int:pk>/', views.DetailView.as_view() , name='detail' ),

    #/music/album/add/
    path('album/add/' , views.AlbumCreate.as_view() ,name='album-add'),

    #/music/71/favourite/
    #path('<int:album_id>/favourite/', views.favourite , name='favourite' ),
]

