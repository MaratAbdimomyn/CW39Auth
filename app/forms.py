from django import forms
from .models import Post, PostImage, Comment
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    pass

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'user']

class PostImageForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ['image', 'post']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body', 'post', 'user']
