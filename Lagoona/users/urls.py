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
    path('logout', UserLogoutView.as_view(), name='logout')
    # path('login/', auth_views.LoginView.as_view(template_name = 'core/login.html',
    #                                             authentication_form = LoginForm), name='login'),
    # path('users/create/', views.UserCreateView.as_view(), name='create'),
    # path('users/<str:user_name>/', views.user_detail, name='detail'),
    # path('users/', views.users_view, name='list'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
