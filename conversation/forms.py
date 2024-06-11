from django import forms

from item.models  import Item
from .models import ConversationMessage

class form(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            })
        }
