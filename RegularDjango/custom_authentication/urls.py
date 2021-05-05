from django.urls import path
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from custom_authentication.views import (
    SignUpView,
    LoginView,
    LogoutView,
    password_reset_request
)

app_name = "custom_authentication"

urlpatterns = [
    path('Sign-Up/', SignUpView, name='usersignup'),
    path('Log-In/', LoginView, name='userlogin'),
    path('Log-Out/', LogoutView, name='userslogout'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    path("password_reset/", password_reset_request, name="password_reset"),      
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
