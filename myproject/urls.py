from django.conf.urls import include, url
from django.contrib import admin
from myproject import search
urlpatterns = [
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/$',search.search),
    url(r'^search-form/$',search.search_form)
]
