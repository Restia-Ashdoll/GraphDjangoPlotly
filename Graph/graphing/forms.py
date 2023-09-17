from django import forms

class ColumnSelectionForm(forms.Form):
    selected_column = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        required=False
    )