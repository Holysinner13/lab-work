from django.http import HttpResponse
from django.template import loader
from .forms import UserRegisterForm, UserLoginForm
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView


class UserRegisterView(SuccessMessageMixin, CreateView):
    """
    Представление регистрации на сайте с формой регистрации
    """
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:homepage')
    template_name = 'signup.html'
    success_message = 'Вы успешно зарегистрировались. Можете войти на сайт!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация на сайте'
        return context


class UserLoginView(SuccessMessageMixin, LoginView):
    """
    Авторизация на сайте
    """
    form_class = UserLoginForm
    template_name = 'signup.html'
    next_page = 'users:homepage'
    success_message = 'Добро пожаловать на сайт!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация на сайте'
        return context


class UserLogoutView(LogoutView):
    """
    Выход с сайта
    """
    next_page = 'users:homepage'


def homepage(request):
    template = loader.get_template('../templates/homepage/index.html')
    return HttpResponse(template.render())


def error_404(request, exception):
    return render(request, '../templates/404/404.html', status=404)


def back(request):
    template = loader.get_template('../templates/back.html')
    return HttpResponse(template.render())