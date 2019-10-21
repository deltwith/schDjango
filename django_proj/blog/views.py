from django.shortcuts import render
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    # intercept the check for a valid form
    def form_valid(self, form):
        # add author to the attributes
        form.instance.author = self.request.user
        # send the updated form to the parent's method
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    # intercept the check for a valid form
    def form_valid(self, form):
        # add author to the attributes
        form.instance.author = self.request.user
        # send the updated form to the parent's method
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

# Create your views here.
