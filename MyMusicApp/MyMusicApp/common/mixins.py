class PlaceholderMixin:
    def add_placeholders(self):
        for field_name, field in self.fields.items():  # ('first_name': field_obj)
            placeholder = field.label or field_name.replace('_', ' ').capitalize()
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
