from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .models import BoardModel
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy

# サインアップ機能
def signupfunc(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    try:
      user = User.objects.create_user(username, '', password)
      return render(request, 'signup.html', {})
    except IntegrityError:
      return render(request, 'signup.html', {'error': 'このユーザーはすでに登録されています。'})
  return render(request, 'signup.html', {})

# ログイン機能
def loginfunc(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('list')
    else:
        return render(request, 'login.html', {})
  return render(request, 'login.html', {})

# 一覧表示
def listfunc(request):
  object_list = BoardModel.objects.all()
  return render(request, 'list.html', {'object_list' : object_list})

# ログアウト機能
def logoutfunc(request):
  logout(request)
  return redirect('login')

# 詳細ぺーじ作成
def detailfunc(request, pk):
  object = get_object_or_404(BoardModel, pk=pk)
  return render(request, 'detail.html', {'object': object})

# いいね機能作成
def goodfunc(request, pk):
  object = BoardModel.objects.get(pk=pk)
  object.good = object.good + 1
  object.save()
  return redirect('list')

# 既読機能作成
def readfunc(request, pk):
  object = BoardModel.objects.get(pk=pk)
  username = request.user.get_username()
  if username in object.readtext:
    return redirect('list')
  else:
    object.read = object.read + 1
    object.readtext = object.readtext + ' ' + username
    object.save()
    return redirect('list')

# 新規作成機能
class BoardCreate(CreateView):
  template_name = 'create.html'
  model = BoardModel
  fields = ('title', 'content', 'author', 'snsimage')
  success_url = reverse_lazy('list')


