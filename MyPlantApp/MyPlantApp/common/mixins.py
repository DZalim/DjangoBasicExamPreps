class LabelMixin:
    def add_labels(self):
        for field_name, field in self.fields.items():
            field.label = field_name.replace('_', ' ').title()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_labels()


class DisabledMixin:
    disabled_fields = []

    def make_fields_disabled(self):
        for field_name in self.disabled_fields:
            if field_name in self.fields:
                self.fields[field_name].widget.attrs['disabled'] = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.make_fields_disabled()
