from django.contrib.staticfiles.storage import staticfiles_storage
from django.db.models import Count
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.generic import RedirectView, TemplateView
from django.views.generic.edit import FormMixin

from search.forms import SearchForm
from victims.models import Victim


class FaviconView(RedirectView):
    url = staticfiles_storage.url('img/favicon.ico')
    permanent = False


class HomeView(FormMixin, TemplateView):
    form_class = SearchForm
    template_name = 'home.html'

    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['victim_list_count'] = Victim.objects.all().count()
        context['customer_list_count'] = Victim.objects.exclude(name='').count()
        context['subscriber_list_count'] = Victim.objects.filter(newsletter=True).count()
        return context


class RobotsView(TemplateView):
    template_name = 'robots.txt'
    content_type = 'text/plain'
