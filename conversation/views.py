from django.shortcuts import render, get_object_or_404, redirect

from item.models import Item
from .forms import ConversationMessageForm
from .models import Conversation, ConversationMessage

# Communication app is for users to send messages to owners of products

# Create your views here.
def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    if item.created_by == request.user:
        return redirect('dashboard:index')
    
    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])

    if conversations: #to check if there has been previous conversation between the customer and the seller
        pass #redirect to conversation

    if request.method == 'POST': #https://youtu.be/ZxMB6Njs3ck?t=7461 - User 
        form = ConversationMessageForm(request.POST)