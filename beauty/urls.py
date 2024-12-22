# quiz/urls.py
from django.urls import path
from .views import LandingPageView, QuestionView, LoginView, PurchaseView

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing_page'),
    path('question/<int:pk>/', QuestionView.as_view(), name='question'),
    path('login/', LoginView.as_view(), name='login'),
    path('purchase/', PurchaseView.as_view(), name='purchase'),
]
