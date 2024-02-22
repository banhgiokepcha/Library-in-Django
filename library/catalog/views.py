
# Create your views here.
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from .models import *
from django.template.loader import get_template
from django.template import loader
from django.contrib.auth import login, logout 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView
from django.urls import reverse_lazy
from . import forms 
from django.http import HttpResponse, HttpResponseRedirect

def main_page(request): 
    return render(request, 'main-page.html')
 
def logout_page(request):
    logout(request) 
    return HttpResponseRedirect('/')
 
class BookList(ListView): 
    template_name = 'browse/book.html' 
    def get_queryset(self):
       return Book.objects.all().order_by('title')
      
class BookDetail(DetailView):   
    model = Book
    template_name = 'browse/book-detail.html'

    
class GenreList(ListView):
    template_name = 'browse/genre.html'
    def get_queryset(self):
        return Genre.objects.all().order_by('name')
    
class AuthorList(ListView):
    template_name = 'browse/author.html'
    def get_queryset(self):
        return Author.objects.all().order_by('name')
        
     
class SignUp(CreateView):
    form_class = forms.SignUpForm
    success_url = reverse_lazy("login")
    template_name = "signup.html" 
    

