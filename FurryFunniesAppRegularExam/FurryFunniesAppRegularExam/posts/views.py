from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView

from FurryFunniesAppRegularExam.common.helpers import get_author_obj
from FurryFunniesAppRegularExam.posts.forms import CreatePostForm, EditPostForm, DeletePostForm
from FurryFunniesAppRegularExam.posts.models import Post


class CreatePostView(CreateView):
    model = Post
    template_name = "posts/create-post.html"
    form_class = CreatePostForm
    success_url = reverse_lazy("dashboard")

    def form_valid(self, form):
        form.instance.author = get_author_obj()
        return super().form_valid(form)


class PostDetailsView(DetailView):
    model = Post
    template_name = "posts/details-post.html"
    pk_url_kwarg = "post_id"


class EditPostView(UpdateView):
    model = Post
    template_name = "posts/edit-post.html"
    form_class = EditPostForm
    pk_url_kwarg = "post_id"
    success_url = reverse_lazy("dashboard")


class DeletePostView(DeleteView):
    model = Post
    template_name = "posts/delete-post.html"
    form_class = DeletePostForm
    pk_url_kwarg = "post_id"
    success_url = reverse_lazy("dashboard")

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)
