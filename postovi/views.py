from django.views import generic
from django.views.generic import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .models import Question

class IndexView(generic.ListView):
    template_name = 'postovi/index.html'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')

class DetailView(generic.DetailView):
    model = Question
    template_name = 'postovi/detail.html'

class QuestionCreate(CreateView):
    model = Question
    fields = ['quest_name','quest_text']

class QuestionUpdate(UpdateView):
    model = Question
    fields = ['quest_name','quest_text']

class QuestionDelete(DeleteView):
    model = Question
    success_url = reverse_lazy('postovi:index')
    