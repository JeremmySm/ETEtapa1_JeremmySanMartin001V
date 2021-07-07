from django.shortcuts import render, redirect
from .forms import proveedorForm
from .models import Proveedor,Pais



def index(request):

    return render (request, 'index.html')

def index2(request):
    if request.method=='POST': 
        proveedor=proveedorForm(request.POST, files=request.FILES)
        if proveedor.is_valid():
            proveedor.save()         #metodo que crea un nuevo objeto, reemplaza al insert
            return redirect('index3')
    else: 
        proveedor=proveedorForm()
    return render(request, 'index2.html', {'proveedor': proveedor})

def index3(request):
    proveedores = Proveedor.objects.all()   

    return render(request, 'index3.html', context={'proveedores':proveedores})    

def index4(request,id):
    proveedor = Proveedor.objects.get(idproveedor=id)
    
    datos = {
        'form': proveedorForm(instance=proveedor)
    }
    if request.method == 'POST': 
        formulario = proveedorForm(data=request.POST, instance = proveedor)
        if formulario.is_valid: 
            formulario.save()           #permite actualizar la info del objeto encontrado
            return redirect('index3')
        else:
            proveedor=proveedorForm()
            return render(request,'index')
    return render(request, 'index4.html',datos)
    
def index5(request,id):
    proveedor = Proveedor.objects.get(idproveedor=id)
    proveedor.delete()
    return redirect('index3')