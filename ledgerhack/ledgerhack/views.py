from django.contrib.staticfiles.storage import staticfiles_storage
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.generic import RedirectView, TemplateView
from django.views.generic.edit import FormMixin

from search.forms import SearchForm


class FaviconView(RedirectView):
    url = staticfiles_storage.url('img/favicon.ico')
    permanent = False


class HomeView(FormMixin, TemplateView):
    form_class = SearchForm
    template_name = 'home.html'

    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class RobotsView(TemplateView):
    template_name = 'robots.txt'
    content_type = 'text/plain'
