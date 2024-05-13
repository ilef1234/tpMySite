from django.urls import path,include
from . import views
from .views import CategoryAPIView ,ProduitAPIView
urlpatterns = [
path('/i', views.index, name='index'),
path('/ii', views.index1, name='index1'),
path('', views.indexprincipal, name='indexprincipal'),
path('nouvFournisseur/', views.formFournisseur, name='fournisseur'),
path('nvcommande/', views.nCommande, name='nvcommande'),
path('register/',views.register, name = 'register'), 
 path('api/category/', CategoryAPIView.as_view()),
 path('api/produits/', ProduitAPIView.as_view()),
 
]