from django.shortcuts import render
from .models import Post
from django.utils import timezone

def post_list(request):
    posts= Post.objects.filter(published_date__lte= timezone.now())
    posts= posts.order_by('published_date')
    return render(request, 'table/post_list.html', {'posts': posts})
