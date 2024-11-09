from django.views.generic import TemplateView, ListView

from FurryFunniesAppRegularExam.posts.models import Post


class IndexView(TemplateView):
    template_name = "index.html"


class DashboardView(ListView):
    model = Post
    template_name = "dashboard.html"
    context_object_name = "posts"
