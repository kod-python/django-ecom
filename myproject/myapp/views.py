from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature

# Create your views here


def index(request):
    features = Feature.objects.all()
    
    return render(request, 'index.html', {'features':features})




def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        # email = request.POST.get['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        
        if password == password2:
            # if User.objects.filter(email=email).exists():
            #     messages.info(request, 'email already exists')
            #     return redirect('register')
            
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username already exists')
                return redirect('register')
            
            else:
                User.objects.create_user(username=username, password=password)
                messages.success(request, 'Registration successful. Please login.')
                # User.save()
                return redirect('login')
        else:
            messages.error(request, 'passowrd not matched')
     
            return redirect('register')
        
    else:    
      return render(request, 'register.html')





def login(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            
            return redirect('/')
        else:
            messages.info(request, 'credentials are incorrect')
            return redirect('login')
    else:       
      return render(request, 'login.html')








# def index(request):
    
#     feature1 = Feature()
#     feature1.id = 0
#     feature1.name = 'apple'
#     feature1.desc = 'is very sweet papa'
#     feature1.price = '$4352'
#     feature1.is_true = 'False'
    
#     feature2 = Feature()
#     feature2.id = 1
#     feature2.name = 'pineaple'
#     feature2.desc = 'taste great'
#     feature2.price = '$5687'
#     feature1.is_true = 'True'
    
#     feature3 = Feature()
#     feature3.id = 2
#     feature3.name = 'watermelon'
#     feature3.desc = 'good for blood circulation'
#     feature3.price = '$9352'
#     feature1.is_true = 'True'
    
    
#     feature4 = Feature()
#     feature4.id = 3
#     feature4.name = 'banana'
#     feature4.desc = 'digest food quick'
#     feature4.price = '$2008'
    
    
  

#     return render(request, 'index.html', {'feature': feature1, 'features': feature2, 'featuress': feature3, 'featuresss':feature4 })
