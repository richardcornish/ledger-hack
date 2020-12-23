from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from .views import FaviconView, HomeView, RobotsView


urlpatterns = [
    path('about/', include('about.urls')),
    path('search/', include('search.urls')),
    path('admin/', admin.site.urls),
    path('favicon.ico', FaviconView.as_view(), name='favicon'),
    path('robots.txt', RobotsView.as_view(), name='robots'),
    path('', include('victims.urls')),  # top-level hash IDs
    path('', HomeView.as_view(), name='home'),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
