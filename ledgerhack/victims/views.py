from django.views.generic import DetailView
from django.views.generic.edit import FormMixin

from .models import Victim
from search.forms import SearchForm


class VictimDetailView(FormMixin, DetailView):
    model = Victim
    slug_field = 'reference_id'
    form_class = SearchForm

    def get_initial(self):
        initial = super().get_initial()
        initial['q'] = self.get_object().email
        return initial