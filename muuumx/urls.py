from django.conf.urls import include, url, patterns
from django.contrib import admin

from home import views as home_views
from users import views as user_views

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^business/$', include('business.urls', namespace='business')),
    url(r'^client/$', include('business.urls', namespace='client')),

    url(
        r'^$',
        home_views.home_page,
        name='home'
    ),
    url(
        r'^signup/cliente/$',
        user_views.SignupClientView.as_view(),
        name='signup_client'
    ),
    url(
        r'^signup/negocio/$',
        user_views.SignupBusinessView.as_view(),
        name='signup_business'
    ),
    url(
        r'^login/$',
        user_views.LoginView.as_view(),
        name='login'
    ),
    url(
        r'^logout/$',
        user_views.logout_user,
        name='login'
    ),
)
