from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import Task
from .forms import TaskForm

# Create your views here.


def loginPage(request):
      page = 'login'
      if request.user.is_authenticated:
            return redirect('home')

      if request.method == 'POST':
            username = request.POST.get('username').lower()
            password = request.POST.get('password')

            try:
                  user = User.objects.get(username=username)
            except:
                  messages.error(request, 'Invalid username or password')
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                  login(request, user)
                  return redirect('home')
            else:
                  messages.error(request, 'User or Password Does Not Exist')

      context = {'page': page}
      return render(request, 'base/login_register.html', context)


def logoutUser(request):
      logout(request)
      return redirect('home')


def registerPage(request):
      form = UserCreationForm()

      if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                  user = form.save(commit=False)
                  user.username = user.username.lower()
                  user.save()
                  login(request, user)
                  return redirect('home')
            else:
                  messages.error(request, 'An Error Has Occurred During Registration')

      context = {'form': form}
      return render(request, 'base/login_register.html', context)


def home(request):
      task = request.GET.get('task') if request.GET.get('task') != None else ''      
      tasks = Task.objects.filter(name__icontains=task)

      context = {'tasks': tasks}
      return render(request, 'base/home.html', context)


@login_required(login_url='login')
def createTask(request):
      form = TaskForm()
      if request.method == 'POST':
            form = TaskForm(request.POST)
            if form.is_valid():
                  task =form.save(commit=False)
                  task.user = request.user
                  task.save()
                  return redirect('home')

      context = {'form': form}
      return render(request, 'base/task-form.html', context)


@login_required(login_url='login')
def updateTask(request, pk):
      task = Task.objects.get(id=pk)
      form = TaskForm(instance=task)

      if request.user != task.user:
            return HttpResponse('YOU Are Not Allowed HERE!')

      if request.method == 'POST':
            form = TaskForm(request.POST, instance=task)
            if form.is_valid():
                  form.save()
                  return redirect('home')

      context = {'form': form}
      return render(request, 'base/task-form.html', context)


@login_required(login_url='login')
def deleteTask(request, pk):
      task = Task.objects.get(id=pk)

      if request.user != task.user:
            return HttpResponse('YOU Are Not Allowed HERE!')

      if request.method == 'POST':
            task.delete()
            return redirect('home')

      context = {'task': task}
      return render(request, 'base/delete.html', context)
