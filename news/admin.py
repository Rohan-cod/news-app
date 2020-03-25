from django.contrib import admin

# Register your models here.

from .models import News

class NewsAdmin(admin.ModelAdmin):
    class Meta:
	    model = News

admin.site.register(News,NewsAdmin)