from django.urls import path
from .views import home,sinup,transaction,expence
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('sinup/',sinup),
    path('home/',home),
    path('login/',LoginView.as_view(template_name='monthlyexp/login.html')),
    path('logout/',LogoutView.as_view(template_name='monthlyexp/logout.html')),
    path('transaction/',transaction),
    path('expence',expence),
]