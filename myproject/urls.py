from django.conf.urls import include, url
from django.contrib import admin
urlpatterns = [
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','article.views.home'),
   #url(r'(?P<my_args>\d+)/$','article.views.detail',name = 'detail'),
    #url(r'^search/$',search.search),
    #url(r'^search-form/$',search.search_form)
]
