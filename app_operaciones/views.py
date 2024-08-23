from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import *
from django.contrib.messages import *

def index(request):
    return render(request, 'index.html')

# Create your views here.
def registro(req):
  if req.method == 'POST':
    # 1. Recogemos los datos del formulario
    email = req.POST['email']
    first_name = req.POST['first_name']
    password = req.POST['password']
    pass_confirm = req.POST['pass_confirm']
    print(email, first_name, password, pass_confirm)
    # 2. Validamos que contraseñas coincidan

    # 3. Creamos al usuario
    User.objects.create_user(username=email, email=email, password=password, first_name=first_name, is_active=False)

    # 4. Redirigimos al 'index'
    return redirect('/accounts/login/') 

  else:
    return render(req, 'registro.html')
  
def crear_procedimiento(request):
    if request.method == 'POST':
      form = ProcedimientoForm(request.POST)
      context = {"form": form}
      if form.is_valid():
        form.save()
        return redirect('index')
      else:
        return render(request, 'procedimiento/crear.html', context)
    else:
      form = ProcedimientoForm()
      context = {"form": form}
    return render(request, 'procedimiento/crear.html', context)
        
