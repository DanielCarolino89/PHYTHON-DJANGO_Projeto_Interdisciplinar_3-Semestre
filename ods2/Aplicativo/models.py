from django.db import models

class Member(models.Model):
  nome = models.CharField(max_length=255)
  sobrenome = models.CharField(max_length=255)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_year = models.IntegerField()
    isbn = models.CharField(max_length=13)

    def to_json(self):
        return {
            'title': self.title,
            'author': self.author,
            'published_year': self.published_year,
            'isbn': self.isbn,
        }