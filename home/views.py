from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Activity, ContactMessage, ContactInfo

def index(request):
    # This version fetches the data for the template
    activities = Activity.objects.all()
    return render(request, 'home/index.html', {'activities': activities})

def what_we_do(request):
    return render(request, 'home/what_we_do.html')

def contact(request):
    info = ContactInfo.objects.first()
    if request.method == "POST":
        # Later we can add code here to save the message to a database
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('program') #for select name= program
        message = request.POST.get('message')

        #save it to the Database
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        #Success Feedback
        messages.success(request, f"Hi {name}, your message has been sent successfully!")
        return redirect('contact')
    
        #print(request.POST.get('name')) 
    return render(request, 'home/contact.html', {'info': info})

def pitch_in(request):
    return render(request, 'home/pitch_in.html')

def apply(request):
    if request.method == "POST":
        messages.success(request, "Your application has been submitted successfully! We will contact you soon.")
        return redirect('apply')
    
    return render(request, 'home/apply.html')