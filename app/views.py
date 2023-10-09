from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from .models import Post, PostImage, Comment
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView, ListView
from .forms import *
from django.urls import reverse_lazy

class SignUp(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'login.html'
    success_url = reverse_lazy('login')

class Login(LoginView):
    pass

class Logout(LogoutView):
    pass

class PostListView(ListView):
    model = Post
    template_name = "home_all.html"
    context_object_name = 'posts'

"""class PostCreateView(CreateView):
    model = Post
    template_name = ".html"

    def get():
        pass

    def post():
        pass


class PostDeleteView(DeleteView):
    model = Post
    template_name = ".html"

class PostDetailView(DetailView):
    model = Post
    template_name = ".html"

    def get():
        pass

    def post():
        pass

class PostUpdateView(UpdateView):
    model = Post
    template_name = ".html"

class CommentDeleteView(DeleteView):
    model = Comment
    template_name = ".html"""





