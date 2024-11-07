from django.shortcuts import render,redirect
from .models import Student
from django.db.models import Q
from django.contrib import messages
# Create your views here.

def home(request):
    a=request.GET.get('searchQuery','')
    if a:
        Student.objects.filter(Q(name__icontains=a) | Q(email__icontains=a) | Q(phno__icontains=a))
    else:
        std=Student.objects.all()
    data={
        'data':std
    }
    return render(request, 'home.html',context=data)

def save(request):
    if request.method=="POST":
       
        name=request.POST['name']
        email=request.POST['email']
        phno=request.POST['phno']
        Student.objects.create(name=name,email=email,phno=phno)
        messages.success(request, 'Student Added Successfully')
    return redirect('home')
        
def updated(request):
    if request.method=="POST":

        
        nm=request.POST['unn']
        id=request.POST['uhn']   
        em=request.POST['uen']
        ph=request.POST['ucn']
        Student.objects.filter(id=id).update(name=nm,email=em,phno=ph)
        messages.success(request, 'Student Updated Successfully')
    return redirect('home')

# def update(request):
        # id=request.POST['id']
        # name=request.POST['name']
        # email=request.POST['email']
        # phno=request.POST['phno']
        # std=Student.objects.get(id=id)
        # std.name=name
        # std.email=email
        # std.phno=phno
        # std.save()
        # messages.success(request, 'Student Updated Successfully')
    # return redirect('home')
        
def delete(request):
    if request.method=="POST":
        id=request.POST["hn"]
        a=Student.objects.get(id=id)
        a.delete()
        messages.success(request, 'Student Deleted data Successfully')
    return redirect('home')
    
