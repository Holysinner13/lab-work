from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import UserRegisterView, UserLoginView, UserLogoutView


app_name = 'users'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('signup/', UserRegisterView.as_view(), name='signup'),
    path('login', UserLoginView.as_view(), name='login'),
    path('logout', UserLogoutView.as_view(), name='logout'),
    path('back', views.back, name='back')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
