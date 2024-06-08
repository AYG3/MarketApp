from django.contrib.auth.decorators import login_required

from django.shortcuts import render, get_object_or_404 # type: ignore
from .models import Item

from .forms import NewItemForm

# https://youtu.be/ZxMB6Njs3ck?t=2762

# Create your views here.
def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=item.pk)

    return render(request, 'item/details.html', {'item':item, 'related_items':related_items})


@login_required #Ensures user is login, else redirects user to login page
def new(request):
    form = NewItemForm()

    return render(request, 'item/form.html', {'form': form, 'title': 'New Item' })