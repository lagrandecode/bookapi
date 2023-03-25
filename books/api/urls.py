
from django.urls import path
from . import views

urlpatterns = [
    path('',views.BookList.as_view()),
    path('<int:pk>',views.BookView.as_view())
]
