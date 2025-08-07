from django.db import models
from django.utils.html import format_html



class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name()



class Book(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='books', on_delete=models.CASCADE)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return format_html(
            '<b>Название: </b> {} <br> <b>Автор: </b> {} <br> <b>Жанр: </b> {}',
            self.name,
            self.author,
            self.category
        )



class Comment(models.Model):
    nickname = models.CharField(max_length=50)
    comment = models.TextField()
    book = models.ForeignKey(Book, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return format_html(
            '<b>Автор: </b> {} <br> <b>Книга: </b> {} <br> <b>Комментарий: </b> <br> {}',
            self.nickname,
            self.book.name,
            self.comment
        )