from django.shortcuts import render, get_object_or_404
from .models import Item


# https://youtu.be/ZxMB6Njs3ck?t=2762

# Create your views here.
def detail(request, pk):
    item = get_object_or_404(Item, pk=pk )

    return render(request, 'item/details.html', {'item':item})