from django.contrib import admin
from .models import post

class postmodeladmin(admin.ModelAdmin):
    list_display = ["title","last_seen"]
    list_display_links = ["last_seen","title"]
    list_filter=["title","last_seen"]
    search_fields=["title","content"]
    class Meta:
        model=post
admin.site.register(post,postmodeladmin)

# Register your models here.
