from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(BookInfo)
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'pubDate', 'subscription', 'available']


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ['userId', 'bookId', 'loan_date', 'end_date']