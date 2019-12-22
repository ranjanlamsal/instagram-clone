from django.shortcuts import render
from .models import PostModel

# Create your views here.
def index(request):

    allpost = PostModel.objects.all()

    d = {
        'posts': allpost
    }

    return render(request, 'photo_app/index.html', d)