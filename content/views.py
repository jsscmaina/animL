from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from content.models import Post
from django.db.models import Q
from django.utils.translation import gettext as _


# Create your views here.

def content_index(request):
    posts = Post.objects.all().order_by('-created_on')
    a = _("Welcome")
    context = {
        "posts": posts,
        "a": a,
    }
    return render(request, "content/index.html", context)


def content_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "content/category.html", context)


def content_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        "post": post,
    }
    return render(request, "content/detail.html", context)


def content_search(request):
    query = request.GET.get('q')
    posts = Post.objects.filter(Q(title__icontains=query) | Q(body__icontains=query)).order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "content/search.html", context)


def observe_form(request):
    context = {
        "a": "SANTA TELL ME",
    }
    return render(request, "observation/index.html", context)

# class SearchResultsView(ListView):
#     model = Post
#     template_name = 'content/search.html'

