from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import os
import pickle
import random

def models(request):
    filename=os.path.dirname(os.path.abspath(__file__))+'/movies_pickle'
    with open(filename,'rb') as f:
        model=pickle.load(f)
    return model

def home(request):
    model=models(request)
    movie=[]
    s=model.index.size
    for i in range(21):
        r=random.randint(1,s)
        movie.append(model.index[r])
    return render(request,'home.html',{'movies':movie})

def detail(request):
    model=models(request)
    movie=request.GET['movie']
    if movie in model.index:
        return render(request,'detail.html',{'movie':movie})
    else:
        return render(request,'detail.html',{'movie':movie,'message':'Movie Not found'})