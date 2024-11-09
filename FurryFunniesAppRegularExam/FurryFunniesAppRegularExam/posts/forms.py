from django import forms

from FurryFunniesAppRegularExam.common.mixins import LabelMixin, ReadOnlyMixin
from FurryFunniesAppRegularExam.posts.models import Post


class PostBaseForm(LabelMixin, forms.ModelForm):
    @staticmethod
    def get_image_type():
        return "Post"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Post
        exclude = ["updated_at", "author"]


class CreatePostForm(PostBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            "title": "Put an attractive and unique title...",
            "content": "Share some interesting facts about your adorable pets..."
        }

        for field_name, placeholder in placeholders.items():
            if field_name in self.fields:
                self.fields[field_name].widget.attrs["placeholder"] = placeholder


class EditDeletePostForm(PostBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["image_url"].help_text = ""


class EditPostForm(EditDeletePostForm):
    pass


class DeletePostForm(ReadOnlyMixin, EditDeletePostForm):
    readonly_fields = ["title", "image_url", "content"]
