from django import forms
from .models import Category


class NoteForm(forms.Form):

    title = forms.CharField(
        label='Naslov',
        min_length=3,
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Unesi naslov beleške'
        })
    )

    content = forms.CharField(
        label='Sadržaj',
        required=True,
        widget=forms.Textarea(attrs={
            'placeholder': 'Unesi sadržaj beleške',
            'rows': 5
        })
    )

    category = forms.ModelChoiceField(
        label='Kategorija',
        queryset=Category.objects.all(),
        required=True,
        empty_label='Izaberi kategoriju'
    )
