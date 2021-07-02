from django.shortcuts import render, redirect
from .models import Users
# Create your views here.

def index(request):
    context = {
        'user': Users.objects.all()
    }
    return render(request, 'index.html', context)

def create_user(request):
    user1 = Users.objects.create(
        name = request.POST['name'], 
        age = request.POST['age'],
        email = request.POST['email']
    )

    return redirect('/')