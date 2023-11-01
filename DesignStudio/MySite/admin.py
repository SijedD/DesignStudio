from django.contrib import admin
from .models import Applications
from .models import Category

# Register your models here.


admin.site.register(Category)

@admin.register(Applications)
class ApplicationsAdmin(admin.ModelAdmin):
    list_display = ('title', 'deck', 'category')
    model = Applications
