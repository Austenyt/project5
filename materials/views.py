from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from materials.models import Material


class MaterialCreateView(CreateView):
    model = Material
    fields = ('title', 'body',)
    success_url = reverse_lazy('mainapp:index')


class MaterialListView(ListView):
    model = Material
