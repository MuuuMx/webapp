from django.conf.urls import include, url
from django.contrib import admin

from home import views as home_views
from users import views as user_views

urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(
        r'^$',
        home_views.home_page,
        name='home'
    ),
    # url(r'^blog/', include('blog.urls')),
    url(
        r'^signup/cliente/$',
        user_views.SignupClientView.as_view(),
        name='signup'
    ),
    url(
        r'^login/$',
        user_views.LoginView.as_view(),
        name='login'
    ),
]
