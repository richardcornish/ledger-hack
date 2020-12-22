from django import forms


class SearchForm(forms.Form):
    q = forms.CharField(label='Query', widget=forms.TextInput(attrs={
        'type': 'search',
        'autocapitalize': 'words',
        'autocomplete': 'email',
        'autocorrect': 'off',
        'autofocus': True,
        'class': 'form-control form-control-lg text-center',
        'placeholder': 'Search for name, e-mail, phone, etc.',
    }))

    def get_results(self, query):
        return None
