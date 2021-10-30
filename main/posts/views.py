from django.http import HttpResponseForbidden, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render

from .forms import EditPost, CreateNewPost, AddPostCredit, AddPostTag
from .models import Post
from .serializers import PostSerializer


def indexPost(response, id):
    if not response.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    p = Post.objects.get(id=id)
    # if redirecting from edit
    if response.method == "POST":
        success = p.edit_post(response)
        if success:
            return HttpResponseRedirect("/api/post/")
        return HttpResponseRedirect("/api/home/")

    form = EditPost(p)
    creditForm = AddPostCredit()

    return render(response, "main/posts/post.html",
                  {"post": p, "form": form,
                   "tagForm": tagForm, "creditForm": creditForm})


def deletePost(response, id):
    if not response.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    Post.objects.get(id=id).delete()
    return redirect('/api/post/')


def listPost(response):
    if response.user.is_authenticated:
        pList = Post.objects.all()

        return render(response, "main/posts/postList.html", {"list": pList})
    return HttpResponseRedirect('/login/')


def createPost(response):
    if not response.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    if response.method == "POST":
        success = Post().create_post(response)
        if success:
            return HttpResponseRedirect("/api/post/")
        return HttpResponseRedirect("/api/home/")
    form = CreateNewPost()
    return render(response, "main/posts/postCreate.html", {"form": form})


def addPostCredit(response, id):
    if not response.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    success = Post.objects.get(id=id).add_credit(response)
    if success:
        return HttpResponseRedirect("/api/post/" + str(id)+"/")
    return HttpResponseRedirect("/api/post/")


def post(request, id):
    if request.method == 'GET':
        post = Post.objects.get(id=id)
        if not post.public:
            return None
        serializer = PostSerializer(post)
        return JsonResponse(serializer.data)
    # return JsonResponse()


def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.filter(public=True)
        serializer = PostSerializer(posts, many=True)
        return JsonResponse(serializer.data, safe=False)
    # return JsonResponse()
