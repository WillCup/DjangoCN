from django.contrib import admin
from .models import Comment
# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ('obj_type', 'user_pk', 'reply_user', 'reply_content', 'published', 'is_active')

admin.site.register(Comment, CommentAdmin)