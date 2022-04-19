from django.http import HttpResponse
from django.shortcuts import render
from theGame.models import scoreRegester

def main (request):
    
    return render (request , 'main.html')


def team (request):
    
    return render (request , 'team.html')

def tutorial (request):
    
    return render (request , 'toturial.html')

def blue (request):
    
    return render (request , 'blue.html')

def task1 (request):
    
    return render (request , 'task1.html')


def task2 (request):
     context = {}
     theScore=request.POST.get('score', None)
     deduction =  request.POST.get('helpdeduct', 0)
     counter =  request.POST.get('trueCount', 0)
     counteradd = request.POST.get('counterAdd', 0)
     score= int(theScore) - int(deduction)
     truecounter = int(counter)+ int(counteradd)
     

     return render (request , 'task2.html', {'score': score, 'truecounter':truecounter})


def task3 (request):
     
    context = {}
    theScore=request.POST.get('score', 0)
    theScorAdd = request.POST.get('scoreAdd', 0)
    deduction =  request.POST.get('helpdeduct', 0)
    counter =  request.POST.get('trueCount', 0)
    counteradd = request.POST.get('counterAdd', 0)
    
    score= int(theScore) + int(theScorAdd) - int(deduction)
    truecounter = int(counter)+ int(counteradd)
    
    return render (request , 'task3.html',  {'score': score, 'truecounter':truecounter})


def task4 (request):
     
    context = {}
    theScore=request.POST.get('score', 0)
    theScorAdd = request.POST.get('scoreAdd', 0)
    deduction =  request.POST.get('helpdeduct', 0)
    counter =  request.POST.get('trueCount', 0)
    counteradd = request.POST.get('counterAdd', 0)
    
    score= int(theScore) + int(theScorAdd) - int(deduction)
    truecounter = int(counter)+ int(counteradd)
    
    
    return render (request , 'task4.html', {'score': score, 'truecounter':truecounter})

def task5 (request):
    theScore=request.POST.get('score', 0)
    theScorAdd = request.POST.get('scoreAdd', 0)
    deduction =  request.POST.get('helpdeduct', 0)
    counter =  request.POST.get('trueCount', 0)
    counteradd = request.POST.get('counterAdd', 0)
    
    score= int(theScore) + int(theScorAdd) - int(deduction)
    truecounter = int(counter)+ int(counteradd)
    
    
    
    return render (request , 'task5.html', {'score': score, 'truecounter':truecounter})

def task6 (request):

    theScore=request.POST.get('score', 0)
    theScorAdd = request.POST.get('scoreAdd', 0)
    deduction =  request.POST.get('helpdeduct', 0)
    counter =  request.POST.get('trueCount', 0)
    counteradd = request.POST.get('counterAdd', 0)
    
    score= int(theScore) + int(theScorAdd) - int(deduction)
    truecounter = int(counter)+ int(counteradd)
    
    
    
    return render (request , 'task6.html', {'score': score, 'truecounter':truecounter})

def task7 (request):
    
    theScore=request.POST.get('score', 0)
    theScorAdd = request.POST.get('scoreAdd', 0)
    deduction =  request.POST.get('helpdeduct', 0)
    counter =  request.POST.get('trueCount', 0)
    counteradd = request.POST.get('counterAdd', 0)
    
    score= int(theScore) + int(theScorAdd) - int(deduction)
    truecounter = int(counter)+ int(counteradd)
    
    
    
    return render (request , 'task7.html', {'score': score, 'truecounter':truecounter})

def result (request):
         
    theScore=request.POST.get('score', 0)
    theScorAdd = request.POST.get('scoreAdd', 0)
    deduction =  request.POST.get('helpdeduct', 0)
    counter =  request.POST.get('trueCount', 0)
    counteradd = request.POST.get('counterAdd', 0)
    
    score= int(theScore) + int(theScorAdd) - int(deduction)
    truecounter = int(counter)+ int(counteradd)
    return render (request , 'result.html', {'score': score, 'truecounter':truecounter})

def about(request):

     return render (request , 'about.html')

def scoring(request):
    
     return render (request , 'scoring.html')






