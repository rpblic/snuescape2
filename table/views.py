from django.shortcuts import render

def post_list(request):
    return render(request, 'table/post_list.html', {})