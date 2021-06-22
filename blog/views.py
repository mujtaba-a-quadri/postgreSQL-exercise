from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.urls import reverse_lazy
from .models import Post
from django.contrib.auth.models import User
from django.http import HttpResponse

class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
      """Return all the posts."""
      return Post.objects.all()

class MyView(generic.ListView):
    template_name = 'blog/mine.html'
    context_object_name = 'post_list'

    def get_queryset(self):
      """Return all the user's posts."""
      return Post.objects.filter(author=self.request.user)
      
class AlphaView(generic.ListView):
    template_name = 'blog/alpha.html'
    context_object_name = 'post_list'
    
    def get_queryset(self):
      """Return all the posts, in alphabetical order"""
      return Post.objects.order_by('title')

class MyAlphaView(generic.ListView):
    template_name = 'blog/myalpha.html'
    context_object_name = 'post_list'
    
    def get_queryset(self):
      """Return all the user's posts, in alphabetical order"""
      return Post.objects.filter(author=self.request.user).order_by('title')

class CreateView(generic.edit.CreateView):
    template_name = 'blog/create.html'
    model = Post
    fields = ['author', 'title', 'text']
    success_url = reverse_lazy('blog:mine') # more robust than hardcoding to /greetings/; directs user to index view after creating a greeting

class UpdateView(generic.edit.UpdateView):
    template_name = 'blog/update.html'
    model = Post
    fields = ['author', 'title', 'text']
    success_url = reverse_lazy('blog:index')

class DeleteView(generic.edit.DeleteView):
    template_name = 'blog/delete.html' # override default of greetings/greeting_confirm_delete.html
    model = Post
    success_url = reverse_lazy('blog:index')
