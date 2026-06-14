from .models import ContactInfo

def global_contact_info(request):
    #to make 'info' availabe in every single HTML file automatically
    return{
        'info': ContactInfo.objects.first()
    }