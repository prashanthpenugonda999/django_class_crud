from django.shortcuts import render,redirect
from testapp1.forms import Std_Form
from django.http import HttpResponseRedirect
from testapp1.models import student

def Homepage(req):
    try:
        data=student.objects.all()
        for i in data:
            print(i)
        return render(req,"crud/index.html",{"data":data})
    except:
        return render(req,"crud/index.html")

    

def Page(req):
    form=Std_Form()
    if req.method=="POST":
        form=Std_Form(req.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect("/")
            
            

    return render(req,"crud/page.html",{"form":form})
def delete(req,id):
    form=student.objects.get(id=id)
    form.delete()
    return redirect("/")
def update(req,id):
    form=student.objects.get(id=id)
    form1=Std_Form(instance=form)
    if req.method=="POST":
        form1=Std_Form(req.POST,instance=form)
        if form1.is_valid:
            form1.save()
            return redirect("/")
            
            
    return render(req,"crud/update.html",{"form":form1})
    