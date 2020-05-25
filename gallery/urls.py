from django.conf.urls import url
from . import views
from .views import SearchResultsListView,SearchLocationListView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('',views.home,name='home'),
    url('search/', SearchResultsListView.as_view(), name='search_results'),
    url('search/', SearchLocationListView.as_view(), name='search_results'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
