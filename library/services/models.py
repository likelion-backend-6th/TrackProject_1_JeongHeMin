from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class BookInfo(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    pubDate = models.DateTimeField()
    subscription = models.TextField()
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ['title']

class Loan(models.Model):
    userId = models.ForeignKey(User, related_name='userid', on_delete=models.CASCADE)
    bookId = models.ForeignKey(BookInfo, related_name='bookid', on_delete=models.CASCADE)
    loan_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(default=timezone.now() + timezone.timedelta(days=14))

    class Meta:
        ordering = ['loan_date']