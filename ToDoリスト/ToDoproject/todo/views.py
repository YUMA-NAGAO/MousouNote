from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy
from .models import TodoModel


# Create your views here.
class ToDoList(ListView):
    template_name = 'list.html'
    model = TodoModel


class ToDoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel


class ToDoCreate(CreateView):
    template_name = 'create.html'
    model = TodoModel
    fields = ("title", "memo", "priority", "duedate")
    success_url = reverse_lazy('list')
    # クラスの中で、定義するなら、reverse_lazyにする


class ToDoDelete(DeleteView):
    template_name = 'delete.html'
    model = TodoModel
    # データベースの継承
    success_url = reverse_lazy('list')

class ToDoUpdate(UpdateView):
    template_name = 'update.html'
    model = TodoModel
    fields = ("title", "memo", "priority", "duedate")
    # 全てのデータを更新する権限を付与する
    success_url = reverse_lazy('list')

