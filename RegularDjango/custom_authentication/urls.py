from django.urls import path
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from custom_authentication.views import (
    SignUpView,
    LoginView,
    LogoutView
)

app_name = "custom_authentication"

urlpatterns = [
    path('Sign-Up/', SignUpView, name='usersignup'),
    path('Log-In/', LoginView, name='userlogin'),
    path('Log-Out/', LogoutView, name='userslogout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
