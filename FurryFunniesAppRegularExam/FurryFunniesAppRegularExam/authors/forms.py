from django import forms

from FurryFunniesAppRegularExam.authors.models import Author
from FurryFunniesAppRegularExam.common.mixins import LabelMixin, FieldVisibilityMixin


class AuthorBaseForm(LabelMixin, forms.ModelForm):

    @staticmethod
    def get_image_type():
        return "Profile"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Author
        fields = "__all__"


class CreateAuthorForm(FieldVisibilityMixin, AuthorBaseForm):
    visible_fields = ["first_name", "last_name", "passcode", "pets_number"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["passcode"].widget = forms.PasswordInput(
            attrs={
                "placeholder": "Enter 6 digits...",
            }
        )

        placeholders = {
            "first_name": "Enter your first name...",
            "last_name": "Enter your last name...",
            "pets_number": "Enter the number of your pets..."
        }

        for field_name, placeholder in placeholders.items():
            if field_name in self.fields:
                self.fields[field_name].widget.attrs["placeholder"] = placeholder


class EditAuthorForm(FieldVisibilityMixin, AuthorBaseForm):
    visible_fields = ["first_name", "last_name", "pets_number", "info", "image_url"]
