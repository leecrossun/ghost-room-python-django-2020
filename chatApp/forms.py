from django import forms
from .models import Room, Message

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = {'user', 'user_read', 'admin_read', 'last_message',}

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = {'body',}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['body'].label = ""
        self.fields['body'].widget.attrs.update({
            'class': 'enter-message',
            'placeholder': '문의사항을 간단히 입력해주세요'
        })