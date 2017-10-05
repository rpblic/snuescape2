from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone

def post_list(request):
    posts= Post.objects.all()
    # posts= Post.objects.filter(published_date__lte= timezone.now())
    # filter를 할 때 한 개밖에 안 나타나게 바뀌는 듯? 왜 그러지
    posts= posts.order_by('published_date')
    return render(request, 'table/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post= get_object_or_404(Post, pk=pk)
    return render(request, 'table/post_detail.html', {'post': post})
