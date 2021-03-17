from django.urls import path, include #new

from drf_app.views import (
    drf_testing_view
)


urlpatterns = [
    path('', drf_testing_view.as_view(), name="drf_testing"),
]
