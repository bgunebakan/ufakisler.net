from django.shortcuts import render
from django.http import HttpResponse
from ufakisler.models import Post,Project

def index(request):
    latest_project_list = Project.objects.all().order_by('-date')[:5]

    latest_post_list = Post.objects.all().order_by('-date')[:5]

    context = {'latest_post_list': latest_post_list,
               'latest_project_list': latest_project_list}
    return render(request, 'ufakisler/index.html', context)

def post_detail(request,post_id):

    
    return HttpResponse(post_id)
