from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, 'index.html')

#Template varialbe 
def dinner(request):
    menu = ["족발", "햄버거", "치킨", "초밥"]
    pick = random.choice(menu)
    return render(request, 'dinner.html', {'dinner':pick})
    
# Variable routing
def hello(request, name):
    return render(request, 'hello.html', {'name': name})
    
def coffee(request):
    drink = ["카페모카", "헤이즐럿라떼", "그린티라떼", "아메리카노"]
    me = random.choice(drink)
    return render(request, 'coffee.html', {'coffee': me})
    
#Form tag
def throw(request):
    return render(request, 'throw.html')
    
def catch(request):
    message = request.GET.get('message')
    return render(request,'catch.html', {'message':message})

#Form 외부로 요청
def naver(request):
    return render(request,'naver.html')
    
#Bootstrap
def bootstrap(request):
    return render(request, 'botstrap.html')