from django.shortcuts import render,redirect,get_object_or_404
from .models import Letter
import random
# Create your views here.

def home(request):
    letters = Letter.objects.all()
    max=len(letters)
    letters.id = random.randrange(1,max+1)
    return render(request,'home.html',{'letters':letters})

def write(request):
    return render(request,'write.html')

def create(request):
    new_letter = Letter()
    new_letter.title = request.POST.get('title', False)
    new_letter.body = request.POST.get('body', False)
    new_letter.save()
    return redirect('home')

def read(request,id):
    letters = get_object_or_404(Letter, pk = id)
    return render(request,'read.html',{'letters':letters})

def update(request):
    letters = Letter.objects.all()
    max=len(letters)
    letters.id = random.randrange(1,max+1)
    return redirect('read',letters.id)