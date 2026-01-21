from django.urls import path
from . import views
urlpatterns = [
    path('',views.get_input,name='input'),
    path('result',views.BookListView.as_view,name='filter'),

]