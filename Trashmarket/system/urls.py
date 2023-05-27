from django.contrib.auth import views as auth_views
from django.urls import path
from .views import UserLogoutView
from . import views
from .forms import LoginForm

app_name = 'system'

urlpatterns = [
    path('', views.index, name='index'),
    path('404', views.error_404, name='page_not_found'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html',
                                                authentication_form=LoginForm), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]
