from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def what_we_do(request):
    return render(request, 'home/what_we_do.html')

def contact(request):
    if request.method == "POST":
        # Later we can add code here to save the message to a database
        print(request.POST.get('name')) # This prints the name to your terminal
    return render(request, 'home/contact.html')

def pitch_in(request):
    return render(request, 'home/pitch_in.html')

def apply(request):
    if request .method == "POST":
        messages.success(request, "Your application had been submitted successfully! We will contact you soon.")
        return redirect('apply')
    
    return render(request, 'home/apply.html')
    

