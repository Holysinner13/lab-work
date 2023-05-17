from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = 'users'
urlpatterns = [
    # path('users/', views.users_view, name='list'),
    path('', views.homepage, name='homepage'),
    # path('users/create/', views.UserCreateView.as_view(), name='create'),
    # path('users/<str:user_name>/', views.user_detail, name='detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
