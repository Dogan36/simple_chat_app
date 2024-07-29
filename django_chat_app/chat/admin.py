from django.contrib import admin
from .models import Message, Chat

class MessageAdmin(admin.ModelAdmin):
    fields = ('chat', 'text', 'created_at')
    list_display = ('chat', 'text', 'created_at')
    search_fields = ('text', )
# Register your models here.
admin.site.register(Message, MessageAdmin)
admin.site.register(Chat)
