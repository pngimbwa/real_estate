from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns,include, url
from django.contrib import admin
admin.autodiscover()
from . import views

urlpatterns = [
    url(r'^search_home/(?P<housetype>[-\w]+)/(?P<bed_number>[-\w]+)/(?P<min_price>[-\w]+)/(?P<max_price>[-\w]+)/(?P<choices>[-\w]+)/search_home/$','housing_estate.dropdown.get_home',name='search_home'),
]
if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)












