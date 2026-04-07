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

    class Meta:
        verbose_name_plural = "contact Information"

    def __str__(self):
        return "Aagaaz Trust Contact Details"
