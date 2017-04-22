"""real_estate URL Configuration
"""

from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import  housing_estate.views
import housing_estate.dropdown
urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$',housing_estate.views.index, name='index'),
    #********HOUSING ESTATES URLS ********
    url(r'^housing_estate/', include('housing_estate.urls', namespace='housing_estate', app_name='housing_estate')),

    url(r'^address_display/$',housing_estate.dropdown.list_addresses,name='address_display'),

    url(r'^search_home/(?P<housetype>[-\w]+)/(?P<bed_number>[-\w]+)/(?P<min_price>[-\w]+)/(?P<max_price>[-\w]+)/search_home/$','housing_estate.dropdown.get_home',name='search_home'),
]

if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
