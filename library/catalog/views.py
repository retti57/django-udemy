from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Book, BookInstance, Author, Language, Genre
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def index(request: HttpRequest):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_avail = BookInstance.objects.filter(status__exact='a').count()
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_avail': num_instances_avail
    }
    return render(request, 'catalog/index.html', context=context)


class BookCreate(LoginRequiredMixin, CreateView):  # model_form.html
    model = Book
    fields = '__all__'


class BookDetail(DetailView):
    model = Book


@login_required
def my_view(request):
    return render(request, 'catalog/my_view.html')


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'catalog/signup.html'


class CheckedOutBooksByUserView(LoginRequiredMixin,ListView):
    """ list all BookInstances but ill filter based of currently logged in user session"""
    model = BookInstance
    template_name = 'catalog/profile.html'
    paginate_by = 5  # 5 instances per page

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user)
