# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 14:35:44 2019

@author: england.kwok
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), #views.index = index() in the views.py file
    path("books/", views.BookListView.as_view(), name="books"), #as_view() is class based
    path("book/<int:pk>", views.BookDetailView.as_view(), name="book-detail"), #parameter passed is called 'pk'
    path("authors/", views.AuthorListView.as_view(), name="authors"),
    path("author/<int:pk>", views.AuthorDetailView.as_view(), name="author-detail"),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path(r'borrowed/', views.LoanedBooksAllListView.as_view(), name='all-borrowed'),  # Added for challenge
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
] 
# catalog/author/create/, catalog/author/id>/update/, catalog/author/<id>/delete/
urlpatterns += [  
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
]

# catalog/book/create/, catalog/book/id>/update/, catalog/book/<id>/delete/
urlpatterns += [  
    path('book/create/', views.BookCreate.as_view(), name='book_create'),
    path('book/<int:pk>/update/', views.BookUpdate.as_view(), name='book_update'),
    path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='book_delete'),
]


#urlpatterns += [   
#    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
#]