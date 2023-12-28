from django.http import HttpResponse
from django.shortcuts import render
from .models import Food


# Create your views here.
def index(request):
    food=Food.objects.all()
    context={
        'food_list':food
    }
    return render(request,"index.html",context)
def detail(request,food_id):
    food=Food.objects.get(id=food_id)
    return render(request,"detail.html",{'food':food})