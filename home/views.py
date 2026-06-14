from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Activity, ContactMessage, ContactInfo, Application, BankDetail, Program, TeamMember, AboutUs, AboutGallery, HomeSlider, Testimonial

def index(request):
    # This version fetches the data for the template
    activities = Program.objects.filter(is_active=True)[:3]
    slides = HomeSlider.objects.all()
    testimonials = Testimonial.objects.filter(is_active=True)
    return render(request, 'home/index.html', 
                  {'activities': activities,
                  'slides': slides,
                  'testimonials':testimonials}
                  )

def what_we_do(request):
    programs = Program.objects.filter(is_active=True)
    slides = HomeSlider.objects.all()

    context = {
        'community_programs': programs.filter(category='COMMUNITY'),
        'vocational_programs': programs.filter(category='VOCATIONAL'),
        'education_programs': programs.filter(category='EDUCATION'),
        'slides': slides,
    }
    return render(request, 'home/what_we_do.html', context)

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
    bank_info = BankDetail.objects.first()# Simplified: This view now just displays the page. 
    slides = HomeSlider.objects.all()

    return render(request, 'home/pitch_in.html', {'bank_info': bank_info, 'slides': slides,})

def apply(request):
    # 1. Get the type from the URL (?type=volunteer) to show on the page
    app_type = request.GET.get('type', 'volunteer') 

    if request.method == "POST":
        # 2. Capture all the data from the form
        # Make sure the 'name' attributes in apply.html match these strings!
        form_type = request.POST.get('form_type')
        f_name = request.POST.get('First_name')
        l_name = request.POST.get('Last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        msg = request.POST.get('message')
        cv_file = request.FILES.get('cv') # Files come from request.FILES

        # 3. Save to the database using the EXACT field names from models.py
        Application.objects.create(
            app_type=form_type,
            First_name=f_name,
            Last_name=l_name,
            email=email,
            phone=phone,
            message=msg,
            cv=cv_file
        )

        messages.success(request, f"Your {form_type} application has been submitted successfully!")
        return redirect('pitch_in')
    
    # Send the app_type to the template so it can say "Apply for Volunteer"
    return render(request, 'home/apply.html', {'app_type': app_type})

def about_us(request):
    # 1. Fetch the story text (AboutUs model)
    story = AboutUs.objects.first()
    
    # 2. Fetch the gallery images (AboutGallery model)
    # We use .all() because we want multiple photos for the shuffle
    gallery = story.gallery_images.all() if story else []
    
    # 3. Fetch the team members (TeamMember model)
    founders = TeamMember.objects.filter(role='FOUNDER')
    teachers = TeamMember.objects.filter(role='TEACHER')

    # 4. Pack it all into one context dictionary
    context = {
        'story': story,
        'gallery': gallery,
        'founders': founders,
        'teachers': teachers,
    }
    
    # 5. Send it to the template
    return render(request, 'home/about_us.html', context)


