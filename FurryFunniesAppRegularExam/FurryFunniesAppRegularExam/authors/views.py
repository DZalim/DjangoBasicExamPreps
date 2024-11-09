from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from FurryFunniesAppRegularExam.authors.forms import CreateAuthorForm, EditAuthorForm
from FurryFunniesAppRegularExam.authors.models import Author
from FurryFunniesAppRegularExam.common.helpers import get_author_obj


class CreateAuthorView(CreateView):
    model = Author
    template_name = "authors/create-author.html"
    form_class = CreateAuthorForm
    success_url = reverse_lazy("dashboard")


class AuthorDetailsView(DetailView):
    template_name = "authors/details-author.html"

    def get_object(self, queryset=None):
        return get_author_obj()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["last_post"] = context["author"].posts.order_by("-updated_at").first()

        return context


class EditAuthorView(UpdateView):
    template_name = "authors/edit-author.html"
    form_class = EditAuthorForm
    success_url = reverse_lazy("author-details")

    def get_object(self, queryset=None):
        return get_author_obj()


class DeleteAuthorView(DeleteView):
    template_name = "authors/delete-author.html"
    success_url = reverse_lazy("index")

    def get_object(self, queryset=None):
        return get_author_obj()
