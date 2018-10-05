from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from apps.mascota.models import Mascota
from django.views.generic.list import ListView
from django.core import serializers

from django.core.urlresolvers import reverse_lazy
from apps.mascota.forms import MascotaForm
from django.views.generic.edit import CreateView,UpdateView, DeleteView
# Create your views here.



def listadousuarios(request):
    lista = serializers.serialize('json', User.objects.all(),fields= ['username','first_name'])
    return HttpResponse(lista, content_type='application/json')

def index(request):
    return render(request,"mascota/index.html")

def mascota_view(request):
    if request.method=='POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('mascota:index')
    else:
        form = MascotaForm()
    return render(request,'mascota/mascota_form.html',{'form':form})


def mascota_list(request):
    mascota=Mascota.objects.all().order_by('folio')
    contexto={'mascotas':mascota}
    return render(request,'mascota/mascota_list.html',contexto)

def mascota_edit(request,id_mascota):
    mascota=Mascota.objects.get(folio=id_mascota)
    if request.method=='GET':
        form=MascotaForm(instance=mascota)
    else:
        form = MascotaForm(request.POST,instance=mascota)
        if form.is_valid():
            form.save()
            return redirect('mascota:mascota_listar')
    return render(request,'mascota/mascota_form.html',{'form':form})

def mascota_delete(request,id_mascota):
    mascota = Mascota.objects.get(folio=id_mascota)
    if request.method=='POST':
        mascota.delete()
        return redirect('mascota:mascota_listar')
    return render(request,'mascota/mascota_delete.html',{'mascota':mascota})

class MascotaList(ListView):
    model=Mascota
    template_name= 'mascota/mascota_list'

class MascotaCreate(CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/mascota_form.html'
    success_url= reverse_lazy('mascota:mascota_listar')


class MascotaUpdate(UpdateView):
    model=Mascota
    form_class=MascotaForm
    template_name = 'mascota/mascota_form.html'
    success_url = reverse_lazy('mascota:mascota_listar')

class MascotaDelete(DeleteView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/mascota_delete.html'
    success_url= reverse_lazy('mascota:mascota_listar')

