from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegisterUserForm
from .models import Author
from .models import Applications


# Create your views here.

def index(request):
    Applications_title = Applications.objects.all()
    Applications_deck = Applications.deck
    Applications_category = Applications.category
    return render(request, 'index.html', context={'Applications_title': Applications_title,
                                                 'Applications_deck': Applications_deck,
                                                 'Applications_category': Applications_category})


class AuthorCreate(CreateView):
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']
    initial = {'date_of_death': '11/06/2020'}


class AuthorUpdate(UpdateView):
    model = Author
    fields = '__all__'  # Not recommended (potential security issue if more fields added)


class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('authors')


class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')
