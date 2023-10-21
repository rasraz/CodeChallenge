from django.urls import path,include
from .views import RiskCalculationView

app_name='insurance_api_urls'
urlpatterns = [
    path('',RiskCalculationView.as_view()),
]