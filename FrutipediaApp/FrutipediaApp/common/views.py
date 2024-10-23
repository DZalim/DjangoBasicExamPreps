from django.views.generic import TemplateView, ListView

from FrutipediaApp.fruits.models import Fruit


class IndexView(TemplateView):
    template_name = 'index.html'


class DashboardView(ListView):
    model = Fruit
    template_name = 'dashboard.html'
