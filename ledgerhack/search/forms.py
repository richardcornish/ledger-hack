from django import forms

from victims.models import Victim


class SearchForm(forms.Form):
    q = forms.CharField(label='E-mail address', widget=forms.TextInput(attrs={
        'type': 'search',
        'autocapitalize': 'words',
        'autocomplete': 'email',
        'autocorrect': 'off',
        'autofocus': True,
        'class': 'form-control form-control-lg text-center',
        'placeholder': 'Search by e-mail',
    }))

    def get_result(self, query):
        try:
            obj = Victim.objects.get(email__iexact=query)
        except Victim.DoesNotExist:
            obj = None
        return obj
