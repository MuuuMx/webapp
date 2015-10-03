from django.conf.urls import include, url
from django.contrib import admin

from home import views as home_views

urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', home_views.home_page, name='home'),
    url(r'^admin/', include(admin.site.urls)),
]
