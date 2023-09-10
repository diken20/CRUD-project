from django.shortcuts import render,HttpResponseRedirect
from . forms import studentReg
from . models import User
# Create your views here.


def addandshow(request):
    if request.method == 'POST':
        fm=studentReg(request.POST)
        if fm.is_valid():
            fm.save()
            fm=studentReg()
    else:
         fm=studentReg()
    stud=User.objects.all()
    return render(request, 'enroll/addandshow.html',{'form':fm,'stu':stud})

#This fn will edit
def update(request,id):
    if request.method=='POST':
       pi=User.objects.get(pk=id)
       fm=studentReg(request.POST,instance=pi)
       if fm.is_valid():
           fm.save()
    else:
       pi =User.objects.get(pk=id)
       fm=studentReg(instance=pi)
    return render(request,'enroll/updatestudent.html',{'form':fm})
   
        
   
def delete(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')