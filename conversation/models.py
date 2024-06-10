from django.contrib.auth.models import User
from django.db import models
from item.models import Item

# Create your models here.
class Conversations(models.Model):
    item = models.ForeignKey(Item, related_name='conversations',on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)  # Set at object creation and not modified thereafter.
    modified_at = models.DateTimeField(auto_now=True)  # Updated to current timestamp on every save of the object.

    class Meta:
        ordering = ('-modified_at', )


class ConversationMessage(models.Model):
    conversation = models.ForeignKey(Conversations, related_name='messages', on_delete=models.CASCADE)