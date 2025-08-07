from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic.base import ContextMixin
from .models import Category, Author, Book, Comment



class CategoriesView(View, ContextMixin):
    template_name = 'categories.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def get(self, request):
        return render(request=request, template_name=self.template_name, context=self.get_context_data())



class CategoryView(View):
    template_name = 'category.html'

    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        all_authors = Author.objects.all()
        authors = []

        for author in all_authors:
            books = Book.objects.filter(category=category, author=author)
            if books:
                authors.append(author)

        context = {
            'category': category,
            'authors': authors
        }

        return render(request=request, template_name=self.template_name, context=context)



class BooksView(View):
    template_name = 'books.html'

    def get(self, request, category_pk, author_pk):
        category = get_object_or_404(Category, pk=category_pk)
        author = get_object_or_404(Author, pk=author_pk)
        books = Book.objects.filter(author=author, category=category)

        context = {
            'author': author,
            'books': books
        }

        return render(request=request, template_name=self.template_name, context=context)



class BookView(View):
    template_name = 'book.html'

    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        comments = Comment.objects.filter(book=book)

        context = {
            'book': book,
            'comments': comments
        }

        return render(request=request, template_name=self.template_name, context=context)

    def post(self, request, pk):
        nickname = request.POST.get('nickname')
        book = get_object_or_404(Book, pk=pk)
        comment = request.POST.get('comment')

        if nickname and comment:
            Comment.objects.create(nickname=nickname, book=book, comment=comment)

        return redirect('book', pk=pk)