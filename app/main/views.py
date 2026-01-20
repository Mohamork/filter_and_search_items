from django.shortcuts import render
from django.http import HttpRedirect
from .models import Book
from .forms import BookForm

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
    
def result(request) :
    books = Book.objects.all()
    return render(request,'result.html',{'books': books})





