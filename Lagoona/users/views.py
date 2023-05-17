from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Users
from django.views.generic import CreateView
from django.urls import reverse_lazy


# def users_view(request):
#     users = Users.objects.all()
#     template = loader.get_template('../templates/user/list.html')
#     context = {
#         'users': users
#     }
#     return HttpResponse(template.render(context, request))


def homepage(request):
    template = loader.get_template('../templates/homepage/index.html')
    return HttpResponse(template.render())


# def user_detail(request, user_name):
#     user = Users.objects.get(username=user_name)
#     template = loader.get_template('../templates/user/user_detail.html')
#     context = {
#         'customer': user
#     }
#     return HttpResponse(template.render(context, request))
#
#
# class UserCreateView(CreateView):
#     model = Users
#     fields = ['username', 'age']
#     template_name = 'user/create.html'
#     success_url = reverse_lazy('users:list')

def error_404(request, exception):
    # context = {}
    # context['page_title'] = '404'
    # response = render(request, '../templates/404/404.html', context=context)
    # response.status_code = 404
    # return response
    return render(request, '../templates/404/bg404.html')
