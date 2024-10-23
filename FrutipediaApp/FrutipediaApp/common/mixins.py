from django import forms


class LabelMixin:
    def add_labels(self):
        for field_name, field in self.fields.items():
            field.label = field_name.replace('_', ' ').title()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_labels()


class NoLabelMixin:
    def remove_labels(self):
        for field in self.fields.values():
            field.label = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.remove_labels()


class PlaceholderMixin:
    def add_placeholders(self):
        for field_name, field in self.fields.items():
            placeholder = field_name.replace('_', ' ').title()
            field.widget.attrs['placeholder'] = placeholder

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_placeholders()


class DisabledMixin:
    disabled_fields = []

    def make_fields_disabled(self):
        for field_name in self.disabled_fields:
            if field_name in self.fields:
                self.fields[field_name].widget.attrs['disabled'] = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.make_fields_disabled()


class FieldVisibilityMixin:
    visible_fields = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name in list(self.fields):
            if field_name not in self.visible_fields:
                self.fields[field_name].widget = forms.HiddenInput()
                self.fields[field_name].label = ''
