from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import doctor
from .forms import AddForm
from django.contrib.auth import authenticate,login as log,logout
# Create your views here.

def test(request):
    return HttpResponse("TRIAL")
    
def regi(request):
    if request.method=='POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        department = request.POST.get('department')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        doctor(name=name,age=age,department=department,email=email,username=username,password=password).save()
    return render(request,"registration.html")

def login(request):
    return render(request,"login.html")

def loginuser(request):
     if request.method=='POST':
         username=request.POST.get('username')
         password=request.POST.get('password')
         cr=doctor.objects.filter(username=username,password=password)
         if cr:
             user_details=doctor.objects.get(username=username,password=password)
             
             name=user_details.name
             department=user_details.department
             email=user_details.email
             age=user_details.age
             request.session['name']=name
             request.session['department']=department
             request.session['email']=email
             request.session['age']=age
             

             return redirect('welcome')
         else:
              return render(request,'login.html')
     else:
              return render(request,'patient.html')
          
def welcome(request):
    name=request.session['name']
    deparment=request.session['department']
    email=request.session['email']
    age=request.session['age']
    return render(request,'welcome.html',{'name':name,'deparment':deparment,'email':email,'age':age,})

def view(request):
    cr = doctor.objects.all()
    return render(request,'view.html',{'cr':cr})

def detailview(request,pk):
    cr = doctor.objects.get(id=pk)
    return render(request,"detailedview.html",{'cr':cr})

def update(request,pk):
    cr = doctor.objects.get(id = pk)
    form = AddForm(instance = cr)
    if request.method =="POST":
        form = AddForm(request.POST,instance = cr)
        if form.is_valid:
            form.save()
            return redirect("views")
    return render(request,"update.html",{'form':form})

def delete(request,pk):
    cr = doctor.objects.get(id = pk)
    cr.delete()
    return redirect("views")

def adminlogin(request):
    return render(request,"adminlogin.html")

def adminloguser(request):
    if request.method=='POST':
        
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            log(request,user)
            return redirect('views')
        else:
            return render(request,'adminlogin.html')
    else:
        return render(request,'insert.html')
    
    