from django.urls import path

from api.views import HealthcheckView


urlpatterns = [
  path('healthcheck', HealthcheckView.as_view())
]
