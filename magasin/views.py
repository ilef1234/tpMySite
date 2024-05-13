from django.shortcuts import render, redirect
from .forms import ProduitForm,FournisseurForm,CommandeForm
from .models import Produit
from .models import Fournisseur
from .models import Commande
from .forms import ProduitForm, FournisseurForm,UserCreationForm,UserRegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from magasin.models import Categorie ,Produit
from magasin.serializers import CategorySerializer,ProduitSerializer
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets

@login_required
def index1(request):
    context={'val':"Menu Acceuil"}
    return render(request,'magasin/acceuil.html',context)

def indexprincipal(request):
    products = Produit.objects.all()
    context = {'products': products}
    return render(request, 'magasin/mesProduits.html', context)

def index2(request):
     if request.method == "POST":
         form = ProduitForm(request.POST, request.FILES)
         if form.is_valid():
             form.save()
             return redirect('/magasin')

     else:
         form = ProduitForm()  # Create an empty form
         return render(request, 'magasin/majProduits.html', {'form': form})
def index(request):
    # Get the list of products
    list = Produit.objects.all()

    return render(request, 'magasin/vitrine.html', {'list': list})

#def index1(request):
    #return render(request,'magasin/acceuil.html' )

def formFournisseur(request):
    form = FournisseurForm()
    if request.method == "POST":
        form = FournisseurForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    fournisseurs=Fournisseur.objects.all()
  
    context={'form': form,'fournisseurs': fournisseurs}
    return render(request, 'magasin/fournisseur.html', context)

def nCommande(request):
    form = CommandeForm()
    if request.method == "POST":
        form = CommandeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    commandes=Commande.objects.all()
  
    context={'form': form,'commandes': commandes}
    return render(request, 'magasin/commande.html', context)

def register(request):
    if request.method == 'POST' :
        form =UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
            return redirect('home')
    else :
        form = UserCreationForm()

    return render(request,'registration/register.html',{'form' : form})

def logout(request): 
    logout(request,'registration/logout.html') 


class CategoryAPIView(APIView):
 def get(self, *args, **kwargs):
    categories = Categorie.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)
 
class ProduitAPIView(APIView):
 def get(self, *args, **kwargs):
    produits = Produit.objects.all()
    serializer = ProduitSerializer(produits, many=True)
    return Response(serializer.data) 
 

class ProductViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProduitSerializer
    def get_queryset(self):
        queryset = Produit.objects.filter()
        category_id = self.request.GET.get('category_id')
        if category_id:
           queryset = queryset.filter(categorie_id=category_id)
        return queryset 