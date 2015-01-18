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

    #L54: The parentheses indicate that an argument will be passed into the view.
    #Replaced in L54: url(r'^products/(?P<slug>.*)/$', 'products.views.single', name='single_product'), 
    url(r'^products/(?P<slug>[\w-]+)/$', 'products.views.single', name='single_product'),
    #(?P<all_items>.*)
    #(?P<id>\d+)
    #You can chain the regex components above together (ex. manufacturer, model) if you also change the number of arguments that the view passes as well

    #L57: Add /s/ url for searches
    url(r'^s/$', 'products.views.search', name='search'),
    url(r'^cart/$', 'carts.views.view', name='cart'),
    url(r'^cart/(?P<slug>[\w-]+)/$', 'carts.views.update_cart', name='update_cart'),
) 

if settings.DEBUG: #Lecture 51: If DEBUG is True, then serve these static files
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)