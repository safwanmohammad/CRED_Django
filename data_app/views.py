from django.shortcuts import get_object_or_404, redirect, render
from . models import datas
from django.contrib import messages
from .forms import dataForm

# class TasklistView(ListView):
#     model = datas
#     template_name = 'home.html'
#     context_object_name = 'context'

# Create your views here.

def add_data(request):
    context =  datas.objects.all()
    if request.method == "POST":
        SL_NO = request.POST.get('SL_NO', '')
        ITEM_NAME = request.POST.get('ITEM_NAME', '')
        DESCRIPTION = request.POST.get('DESCRIPTION', '')
        task = datas( SL_NO= SL_NO, ITEM_NAME=ITEM_NAME, DESCRIPTION= DESCRIPTION)
        task.save()
        return redirect('/',messages.success(request,'Your Data has been stored'))
    return render(request,'home.html',{'context':context})


def delete_data(request,data_id):
    context =  datas.objects.get(id=data_id)
    if request.method == 'POST':
        context.delete()
        return redirect('/',messages.warning(request,'Your Data has been deleted'))
    return render(request,'delete.html',{'context':context})


def update_data(request,data_id):
     data=get_object_or_404(datas,id=data_id)
     if request.method == 'POST':
        data.SL_NO = request.POST.get('SL_NO')
        data.ITEM_NAME = request.POST.get('ITEM_NAME')
        data.DESCRIPTION = request.POST.get('DESCRIPTION')
        data.save()
        return redirect('/',messages.info(request,'Your Data has been updated'))
     return render(request,'update.html',{'data':data})

# def update(request,id):
#     task=get_object_or_404(Form,id=id)
#     if request.method == 'POST':
#         task.num = request.POST.get('num')
#         task.name = request.POST.get('name')
#         task.desc = request.POST.get('desc')
#         task.save()
#         return redirect('/')
#     return render(request,'update.html',{'task':task}