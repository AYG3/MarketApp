from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from item.models import Item
from .forms import ConversationMessageForm
from .models import Conversation, ConversationMessage

# Communication app is for users to send messages to owners of products

@login_required
def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    if item.created_by == request.user:
        return redirect('dashboard:index')
    
    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])

    if conversations: 
        pass

    if request.method == 'POST': #https://youtu.be/ZxMB6Njs3ck?t=7461 - User 
        form = ConversationMessageForm(request.POST)
        
        if form.is_valid():
            conversation = Conversation.objects.create(item=item) #- To create the conversation - (imagine CONVERSATION like a group but only for two people)
            conversation.members.add(request.user) #ading user to the conversation
            conversation.members.add(item.created_by) #addding seller to the conversation
            conversation.save()

            conversation_message = form.save(commit=False) #commit false message to avoid error, bcuz we are stillsaving the created_by, e.t.c ...
            conversation_message.conversation = conversation #establishes relationship with the conversation instance from earlier
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('item:detail', pk=item_pk)
    else:
        form = ConversationMessageForm()

        return render(request, 'conversation/new.html', {'form': form})

@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id])

    return render(request, 'conversation/inbox.html', {'conversations': conversations})