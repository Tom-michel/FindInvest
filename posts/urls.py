from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('accueil', accueil, name="accueil"),

    #  crud post
    path('delete_post/<str:pk>', delete_post, name='delete_post'),
    path('update_post/<str:pk>', update_post, name='update_post'),
    path('create_post', create_post, name='create_post'),
    path('list_projects', list_projects, name='list_projects'),
    path('mes_projets/<str:id_e>', mes_projets, name='mes_projets'),


    # chat 
    path('<str:room>/', room, name="room"),
    path('send', send, name='send'),
    path('getMessages/<str:room>/', getMessages, name='getMessages'),
    path('createRoom/<str:u1>/<str:u2>/<str:title>', createRoom, name='createRoom'),

    # comment post
    path('CommentPost', CommentPost, name='CommentPost'),
    path('getComments', getComments, name='getComments'),

    # favoris
    path('favoris/<str:id_u>', favoris, name="favoris"),
    path('createFavoris', createFavoris, name="createFavoris"),
    path('getFavoris', getFavoris, name='getFavoris'),

    # marquer investi
    path('markPost', markPost, name='markPost'),

]
