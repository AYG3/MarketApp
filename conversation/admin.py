from django.contrib import admin
from .models import ConversationMessage, Conversations

# Register your models here.
admin.site.register(Conversations)
admin.site.register(ConversationMessage)