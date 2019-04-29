import json

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone

from blog.models import Post


def index(request):
    num_posts = Post.objects.all().count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'partial/index.html',
        context={'num_posts': num_posts,
                 'num_visits': num_visits},  # num_visits appended
    )


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


def add_like(request):
    if request.POST:
        post = Post.objects.get(pk=request.POST.get('post_id'))
        post.like += 1
        post.save()
    # return render(request, "partial/home.html")
    return redirect(request.GET.get('next', '/home/'))

# return HttpResponseRedirect('/')

"""

@login_required
def add_like(request):

    post_id = None
    if request.method == 'GET':
        post_id = request.GET['post_id']

    likes = 0
    if post_id:
        ans = Post.objects.get(id=(int(post_id)))
        if ans:
            likes = ans.likes + 1
            ans.likes = likes
            ans.save()

    return HttpResponse(likes)
    """


def logout(request):
    auth.logout(request)
    # Перенаправление на страницу.
    return HttpResponseRedirect("/account/logged_out/")


def post(request):
    if request.method == "POST":  # os request.GET()
        get_value = request.body
        # Do your logic here coz you got data in `get_value`
        data = {}
        data['result'] = 'you made a request'
        return HttpResponse(json.dumps(data), content_type="application/json")
