from django.urls import path

from .views import ListePost, DetailPost, CreerPost, ModifierPost, SupprimerPost,ModifierPost
urlpatterns = [
    path('', ListePost.as_view(), name='liste_postes'), 
    path('<int:pk>/', DetailPost.as_view(), name='detail_post'), 
    path('ajouter/', CreerPost.as_view(), name='creer_post'), 
    path('<int:pk>/modifier/', ModifierPost.as_view(), name='modifier_post'), 
    path('<int:pk>/supprimer/', SupprimerPost.as_view(), name='supprimer_post'), 
]
