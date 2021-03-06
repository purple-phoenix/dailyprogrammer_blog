from django.views import generic
from .models import Post
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from blog.forms import PostForm
import pdb


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


def blog_index(request):

    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    return render(request, 'index.html', context)


def post_detail(request, pk):

    post = Post.objects.get(pk=pk)

    context = {
        "post": post
    }

    return render(request, "post_detail.html", context)


def make_post(request):

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():

            form.save()
            return HttpResponseRedirect("/")

    else:
        form = PostForm()
        context = {
            "form": form
        }
        return render(request, "make_post.html", context)
