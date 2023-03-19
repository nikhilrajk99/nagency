from django.shortcuts import render, redirect

from .form import AgencyForm
from . models import Agency


# Create your views here.
def index(request):
    age=Agency.objects.all()
    return render(request,"index.html",{'age':age})

def add(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        img=request.FILES['img']
        date=request.POST.get('date')
        ages=Agency(name=name,desc=desc,img=img,date=date)
        ages.save()
        return redirect('/')
    return render(request,"add.html")

def update(request,id):
    agent=Agency.objects.get(id=id)
    form=AgencyForm(request.POST or None,request.FILES,instance=agent)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"update.html",{'agent':agent,'form':form})

def delete(request,id):
    if request.method=='POST':
        agen=Agency.objects.get(id=id)
        agen.delete()
        return redirect('/')
    return render(request,"delete.html")