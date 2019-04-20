from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from blog.models import Post


def home(request):
    postList = Post.objects.filter(visible='1')
    paginator = Paginator(postList, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {
        "posts": posts,
        "title": "Главная страница блога",
        "desc": "Описание для главной страницы",
        "key": "ключевые, слова",
    }
    return render(request, "partial/home.html", context)


def single(request, id=None):
    post = get_object_or_404(Post, id=id)

    context = {
        "post": post,
    }
    return render(request, "partial/single.html", context)


def add_like(request, slug):
    try:
        article = get_object_or_404(Post, slug=slug)
        article.likes += 1
        article.save()
    except ObjectDoesNotExist:
        return Http404
    return redirect(request.GET.get('next', '/'))
