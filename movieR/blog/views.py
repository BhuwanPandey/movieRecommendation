from django.shortcuts import render
import os
import pickle
import random
# Create your views here.

def home(request):
    filename=os.path.dirname(os.path.abspath(__file__))+'/movies_pickle'
    with open(filename,"rb") as f:
        model=pickle.load(f)
    s=model.index.size

    movie=[]
    for i in range(21):
        r=random.randint(1,s)
        movie.append(model.index[r])
    return render(request,'home.html',{'movies':movie})