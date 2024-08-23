from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import *
from django.contrib.messages import *
from django.contrib.auth import login as auth_login
from datetime import timedelta, date
from .services import *

def index(request):
    process = listado_procedimientos()
    days = get_week_days()
    
    
    process_by_day = {day: [] for day in days}
    
    for proc in process:
        proc_date = proc.fecha

        data = {
            'medico': proc.usuario,
            'horario': f'{proc.hora_inicio} - {proc.hora_fin}',
            'sala': proc.sala,
        }
        for day in days:
            if proc_date == day:
                process_by_day[day].append(data)

    print(process_by_day.items())
    
    context = {
        'days': days,
        'process_by_day': process_by_day,
    }

    return render(request, 'index.html', context)

def get_week_days():
    today = date.today()
    days = []
    weekday = today.weekday()  # Obtener el índice del día de la semana
    first_day = today - timedelta(days=weekday)  # Calcular el primer día de la semana (lunes)
    for i in range(7):
        days.append(first_day + timedelta(days=i))  # Añadir cada día de la semana
    return days

def registro(request):
  if request.method == 'POST':
        form = RegistroUserForm(request.POST)
        context = { 'form': form }
        if form.is_valid():
            form.save()
            add_message(request, INFO, 'Usuario creado correctamente')
            return redirect('login')
        else:
            add_message(request, ERROR, 'Error al crear el usuario')
            return render(request, 'autenticacion/registro.html', context)
  else:
    form = RegistroUserForm()
    context = { 'form': form }
    return render(request, 'autenticacion/registro.html', context)

def login(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, request.POST)
        context = {'form': form}
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('index')
        else:
            add_message(request, ERROR, 'Usuario o contraseña incorrectos')
            return render(request, 'autenticacion/login.html', context)
    else:
        form = CustomLoginForm()
        context = {'form': form}
    return render(request, 'autenticacion/login.html', context)
  
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
        
