from django.urls import path
from .views import CategoriesView, CategoryView, BooksView, BookView

app_name = 'library'



urlpatterns = [
    path('', CategoriesView.as_view(), name='categories'),
    path('category/<int:pk>/', CategoryView.as_view(), name='category'),
    path('books/<int:category_pk>/<int:author_pk>/', BooksView.as_view(), name='author_books'),
    path('book/<int:pk>/', BookView.as_view(), name='book'),
]