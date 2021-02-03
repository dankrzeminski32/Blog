from django.contrib import admin
from .models import Post, Feedback

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject','date',)
    search_fields = ('name', 'email',)
    date_hierarchy = 'date'

admin.site.register(Post)
admin.site.register(Feedback, FeedbackAdmin)


