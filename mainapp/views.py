from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.cache import cache
from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from config import settings
from mainapp.forms import StudentForm, SubjectForm
from mainapp.models import Student, Subject


@login_required
def index(request):
    student_list = Student.objects.all()
    context = {
        'object_list': student_list,
        'title': 'Главная'
    }
    return render(request, 'main/student_list.html', context)


@login_required
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


class StudentListView(ListView):
    model = Student


class StudentDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Student
    permission_required = 'mainapp.view_student'

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)
        if settings.CACHE_ENABLED:
            key = f'subject_list{self.object.pk}'
            subject_list = cache.get(key)
            if subject_list is None:
                self.object.subject_set.all()
                cache.set(key, subject_list)
        else:
            subject_list = self.object.subject_set.all()

        context_data['subjects'] = subject_list
        return context_data


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    form_class = StudentForm
    # fields = ('first_name', 'last_name', 'avatar')
    success_url = reverse_lazy('mainapp:index')


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    # fields = ('first_name', 'last_name', 'avatar')
    form_class = StudentForm
    success_url = reverse_lazy('mainapp:index')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        SubjectFormset = inlineformset_factory(Student, Subject, form=SubjectForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = SubjectFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = SubjectFormset(instance=self.object)

        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    success_url = reverse_lazy('mainapp:index')


def toggle_activity(request, pk):
    student_item = get_object_or_404(Student, pk=pk)
    if student_item.is_active:
        student_item.is_active = False
    else:
        student_item.is_active = True

    student_item.save()

    return redirect(reverse('mainapp:index'))
