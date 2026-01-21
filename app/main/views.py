from django.shortcuts import render
from django.http import HttpRedirect
from .models import Book
from .forms import BookForm
from django_filters.views import FilterView
from .filters import BookFilter


# Create your views here.

def get_input(request) :
    if request.method == 'POST' :
        form = BookForm(request.POST)
        if form.is_valid() :
            form.save()
            return HttpRedirect('result')
    else:
        form = BookForm
        return render(request,'input.html',{'form':form})
    
class BookListView(FilterView) :
    model = Book
    queryset = Book.objects.all()
    filterset_class = BookFilter
    template_name = 'result.html'
    context_object_name = 'books'







