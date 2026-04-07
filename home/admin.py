from django.contrib import admin
from .models import Activity, ContactMessage, ContactInfo

# 1. Customizing how Activity looks in the admin
@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('title',)

# 2. Customizing how Contact Messages look
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    # This shows the Name, Subject, and Date in a nice table
    list_display = ('name', 'subject', 'created_at')
    # This adds a sidebar to filter by date
    list_filter = ('created_at',)
    # This adds a search bar
    search_fields = ('name', 'email', 'message')

admin.site.register(ContactInfo)