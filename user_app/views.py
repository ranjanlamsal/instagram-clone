from django.shortcuts import render, redirect
from .models import UserModel

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        if username and password:
            user= UserModel.objects.filter(username=username, password=password).first()

            if user:
                request.session['user_id'] = user.id
                return redirect('index')
    else:
        return render(request, 'user_app/login.html')



def logout(request):
    request.session.flush()
    return redirect('login')
