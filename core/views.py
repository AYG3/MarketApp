from django.shortcuts import render, redirect
from item.models import Category, Item
from .forms import SignupForm, 

# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {'categories': categories, 'items': items})


def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST) # gets all the information from the form
        if form.is_valid():
            form.save()     #saves the user in the DB
            return redirect('/login')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {'form':form })

def login(request):
    form = Au