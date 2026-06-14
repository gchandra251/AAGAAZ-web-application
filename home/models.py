from django.db import models

# Create your models here.
class Activity(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()


    def __str__(self):
        return self.title
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
    
class ContactInfo(models.Model):
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    facebook_url = models.URLField(blank=True, null=True, help_text="https://www.facebook.com/people/Aagaaz-Trust/100094013675364/")
    instagram_url = models.URLField(blank=True, null=True, help_text="https://www.instagram.com/aagaaz_charitable_9528/")
    youtube_url = models.URLField(blank=True, null=True, help_text="https://www.youtube.com/@aagaazcharitabletrust9528")

    class Meta:
        verbose_name_plural = "contact Information"

    def __str__(self):
        return "Aagaaz Trust Contact Details"
    
class Application(models.Model):

    APP_TYPES = [
        ('volunteer', 'Volunteer'),
        ('internship', 'Internship')
    ]
    app_type = models.CharField(max_length=20, choices=APP_TYPES)
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    cv = models.FileField(upload_to='cv/', blank=True, null=True) #upload field

    def __str__(self):
        return f"{self.app_type.capitalize()}: {self.First_name} {self.Last_name}"
    
class BankDetail(models.Model):
    account_holder_name = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=30)
    ifsc_code = models.CharField(max_length=20)
    branch_name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Bank Details"

    def __str__(self):
        return f"Bank Details for {self.account_holder_name}"
    

class Program(models.Model):
    #defining the categories
    CATEGORY_CHOICES = [
        ('COMMUNITY', 'Community Program'),
        ('VOCATIONAL', 'Vocational training'),
        ('EDUCATION', 'Educational and Skills'),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    icon_class = models.CharField(max_length=50, default='fas fa-graduation-cap', help_text="FontAwesome icon class (e.g., 'fas fa-users')")
    image = models.ImageField(upload_to='program/', blank=True, null=True)
    is_active = models.BooleanField(default=True, help_text="Uncheck this to hide the program without deleting it")

    def __str__(self):
        return f"{self.title} ({self.get_category_display()})"
    
class TeamMember(models.Model):
    ROLE_CHOICES = [
        ('FOUNDER', 'Founding Member'),
        ('TEACHER', 'Teacher/Staff')
    ]

    name = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='TEACHER')
    email = models.EmailField(blank=True, null=True)
    image = models.ImageField(upload_to='team/', blank=True, null=True)
    bio = models.TextField(blank=True, help_text='Ashort intro about them')
    order = models.IntegerField(default=0, help_text="Order to display (lower numbers first)")

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name}({self.get_role_display()})"
    
class AboutUs(models.Model):
    title = models.CharField(max_length=200, default="Our Story")
    story_text = models.TextField(help_text="The emotional narrative of how it began")
    vision = models.TextField(blank=True)
    mission = models.TextField(blank=True)
    image = models.ImageField(upload_to='about/', null=True, blank=True)

    class Meta:
        verbose_name_plural = "About Us Content"

    def __str__(self):
        return "About Us Content"
    
class AboutGallery(models.Model):
    about_content = models.ForeignKey(AboutUs, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ImageField(upload_to='about_gallery/')
    caption = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return f"Gallery Image {self.id}"

class HomeSlider(models.Model):
    image = models.ImageField(upload_to='home_slider/')

    class Meta:
        verbose_name_plural = "Homepage Slider Images"

    def __str__(self):
        return f"Homepage slide {self.id}"
    
class Testimonial(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=100)
    role = models.CharField(max_length=100, blank=True, null=True, help_text="e.g., Former Student, Community Volunteer")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.author}-{self.role}"