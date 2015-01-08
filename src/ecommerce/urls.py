from django.conf import settings #Lecture 51
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static #Lecture 51
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ecommerce.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'products.views.home', name='home'),
    url(r'^products/$', 'products.views.all', name='products'),
) 

if settings.DEBUG: #Lecture 51: If DEBUG is True, then serve these static files
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
