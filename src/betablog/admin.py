from django.contrib import admin
from .models import PostModels, commentsModels
# Register your models here.

#inherits from admin, displays a list of things you want to see
#in the blog post list
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created')

admin.site.register(PostModels, PostModelAdmin)
admin.site.register(commentsModels)
