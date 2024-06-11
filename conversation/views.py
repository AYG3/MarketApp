from django.shortcuts import render, get_object_or_404

from item.models import Item

# Communication app is for users to send messages to owners of products

# Create your views here.
def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)