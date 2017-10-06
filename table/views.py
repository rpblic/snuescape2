from django.shortcuts import render, get_object_or_404
from .models import Rserv
from django.utils import timezone
from .forms import PostForm
from django.shortcuts import redirect

def timetable(request):
    return None

def rserv_info(request, pk):
    return None

def rserv_edit(request, pk):
    return None

# def post_list(request):
#     posts= Post.objects.all()
#     # posts= Post.objects.filter(published_date__lte= timezone.now())
#     # filter를 할 때 한 개밖에 안 나타나게 바뀌는 듯? 왜 그러지
#     posts= posts.order_by('published_date')
#     return render(request, 'table/post_list.html', {'posts': posts})
#
# def post_detail(request, pk):
#     post= get_object_or_404(Post, pk=pk)
#     return render(request, 'table/post_detail.html', {'post': post})
#
# def post_new(request):
#     if request.method== "POST":
#         form= PostForm(request.POST)
#         if form.is_valid():
#             post= form.save(commit= False)
#             post.author= request.user
#             post.published_date= timezone.now()
#             post.save()
#             return redirect('post_detail', pk= post.pk)
#     else:
#         form= PostForm()
#     return render(request, 'table/post_edit.html', {'form': form})
#
# def post_edit(request, pk):
#     post= get_object_or_404(Post, pk= pk)
#     if request.method== "POST":
#         form= PostForm(request.POST, instance= post)
#         if form.is_valid():
#             post= form.save(commit= False)
#             post.author= request.user
#             post.published_date= timezone.now()
#             post.save()
#             return redirect('post_detail', pk= post.pk)
#     else:
#         form= PostForm(instance= post)
#     return render(request, 'table/post_edit.html', {'form': form})
