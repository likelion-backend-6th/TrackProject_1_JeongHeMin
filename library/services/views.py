import django.utils.datastructures
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import BookInfo, Loan
# Create your views here.

class MainPageView(ListView):

    def get(self, request, *args, **kwargs):
        try:
            booktitle = request.GET['bookName']

        except django.utils.datastructures.MultiValueDictKeyError:
            booktitle = None
        finally:
            if booktitle:
                books = BookInfo.objects.filter(title__contains=booktitle)
            else:
                books = BookInfo.objects.all()[:10]
            return render(request, template_name='main.html', context={'books':books})


    def post(self, request, *args, **kwargs):
        return render(request, template_name='main.html')

class LoanSuccessView(TemplateView):
    def post(self, request, book_id, *args, **kwargs):
        loanBook = Loan()
        loanBook.userId = request.user
        loanBook.bookId = BookInfo.objects.filter(id=book_id)[0]
        loanBook.save()
        BookInfo.objects.filter(id=book_id).update(available=False)
        return render(request, template_name='loan_success.html')

class BookLoanView(TemplateView):
    pass

class BookDetailView(DetailView):
    pass