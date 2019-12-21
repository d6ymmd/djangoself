from django.db import models


class Author(models.Model):
    name = models.CharField('저자', max_length=30)

    def __str__(self):
        return self.name


class Book(models.Model):
    Author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    name = models.CharField('도서명', max_length=100)

    def __str__(self):
        return self.name
