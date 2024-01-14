from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from mainapp.models import Student


class StudentListView(ListView):
    model = Student
    template_name = 'mainapp/index.html'


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email}): {message}')

    context = {
        'title': 'Контакты'
    }
    return render(request, 'mainapp/contact.html', context)


class StudentDetailView(DetailView):
    model = Student
    template_name = 'mainapp/student_detail.html'


class StudentCreateView(CreateView):
    model = Student
    fields = ('first_name', 'last_name', 'avatar')
    success_url = reverse_lazy('mainapp:index')
