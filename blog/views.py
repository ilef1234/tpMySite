from django.shortcuts import render

from django.views.generic.edit import UpdateView

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from blog.forms import PostForm
from .models import Post

class ListePost(ListView):
    model = Post
    template_name = 'blog/liste_postes.html'
    context_object_name = 'postes'
class DetailPost(DetailView):
    model = Post
    template_name = 'blog/detail_post.html'
    context_object_name = 'post'
class CreerPost(CreateView):
    model = Post
    template_name = 'blog/creer_post.html'
    form_class = PostForm 
    success_url = reverse_lazy('liste_postes') 
class ModifierPost(UpdateView):
     model = Post
     template_name = 'blog/modifier_post.html'
     form_class = PostForm
     success_url = reverse_lazy('liste_postes')
class SupprimerPost(DeleteView):
    model = Post
    template_name = 'blog/supprimer_post.html'
    success_url = reverse_lazy('liste_postes') 

