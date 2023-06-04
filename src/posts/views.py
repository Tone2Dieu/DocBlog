from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views import generic
from . import models
# Create your views here.


class HomeList(generic.ListView):
    model = models.BlogPost
    template_name = 'posts/home.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_authenticated:
            return queryset.filter(published=True)
        return queryset



class DetailArticle(generic.DetailView):
    model = models.BlogPost
    template_name = 'posts/detail.html'
    context_object_name = 'post'


class CreateArticle(generic.CreateView):
    model = models.BlogPost
    template_name = 'posts/create.html'
    success_url = reverse_lazy('posts:home')

    fields = [
        'title',
        'content'
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['valider'] = 'Créer'
        return context


class UpdateArticle(generic.UpdateView):
    model = models.BlogPost
    template_name = 'posts/create.html'
    success_url = reverse_lazy('posts:home')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['valider'] = 'Modifier'
        return context


class DeleteArticle(generic.DeleteView):
    model = models.BlogPost
    template_name = 'posts/delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('posts:home')



