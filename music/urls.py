
from django.urls import path
from . import views


app_name = 'music'


urlpatterns = [
    # /music/
    path('', views.IndexView.as_view() , name='index'),

    path('register/', views.UserFormView.as_view() , name='register'),

    #/music/71/
    path('<int:pk>/', views.DetailView.as_view() , name='detail' ),

    #/music/album/add/
    path('album/add/' , views.AlbumCreate.as_view() ,name='album-add'),

    #/music/album/2/
    path('album/<int:pk>/' , views.AlbumUpdate.as_view() ,name='album-update'),

    #/music/album/2/delete/
    path('album/<int:pk>/delete/' , views.AlbumDelete.as_view() ,name='album-delete'),

    #/music/71/favourite/
    #path('<int:album_id>/favourite/', views.favourite , name='favourite' ),
]

