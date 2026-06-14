from django.contrib import admin
from .models import Activity, ContactMessage, ContactInfo, Application, BankDetail, Program, TeamMember, AboutUs, AboutGallery, HomeSlider, Testimonial

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

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('First_name', 'Last_name', 'app_type', 'cv', 'created_at')
    list_filter = ('app_type', 'created_at') #adds a nice sidebar to filter by vulunteer vs intern

    search_fields = ('First_name', 'Last_name', 'email')

admin.site.register(BankDetail)

@admin.register(Program)
class PogramAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('title', 'description')

#admin.site.register(AboutUs)

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):

    list_display = ('name', 'role', 'order') #shows column in the admin list view

    list_filter = ('role',) #adds a filter sidebar 

    search_fields = ('name', 'bio') #adds a search at the top

    list_editable = ('order',)  #change the order number directly

class AboutGalleryInline(admin.TabularInline):
    model = AboutGallery
    extra = 3

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    inlines = [AboutGalleryInline]

# Optional: Also register it separately if you want to see a list of all photos
admin.site.register(AboutGallery)

admin.site.register(HomeSlider)

admin.site.register(Testimonial)