from django.views.generic import TemplateView, ListView

from MyPlantApp.common.helpers import get_user_obj
from MyPlantApp.profiles.models import Profile


class HomeView(TemplateView):
    template_name = 'home-page.html'


class CatalogueView(ListView):
    model = Profile
    template_name = 'plants/catalogue.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_user_obj()
        context['plants'] = context['profile'].plants.all()

        return context
