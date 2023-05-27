from django.shortcuts import render, redirect
from items.models import Category, Items
from .forms import SignupForm


def index(request):
    items = Items.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request, 'index.html', {'items': items, 'categories': categories})


def contact(request):
    return render(request, 'contact.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})


def error_404(request, exception):
    return render(request, '404/404.html', status=404)
