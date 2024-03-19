from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from testapp2.models import Book
from django.urls import reverse_lazy


# Create your views here.
class Book_view(ListView):
    model=Book
    template_name="classbased/Book_List.html"
    context_object_name="book"
class Book_Detailview(DetailView):
    model=Book
    template_name="classbased/Bookdetail.html"
    context_object_name="book"
class Book_createview(CreateView):
    model=Book
    template_name="classbased/create.html"
    fields=("__all__")
    
class Book_deleteview(DeleteView):
    model=Book
    template_name="classbased/book_confirm_delete.html"
    success_url=reverse_lazy("list")
class Book_updateview(UpdateView):
    model=Book
    fields="__all__"
    template_name="classbased/book_update.html"
    success_url="/"




