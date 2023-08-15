from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class ServiceRequest(models.Model):
    REQUEST_TYPES = [
        ('Gas Leak', 'Gas Leak'),
        ('Meter Installation', 'Meter Installation'),
        ('Billing Inquiry', 'Billing Inquiry'),
    ]
    status_choice=[
        ('Pending' , 'pending'),
        ('In Process','In Process'),
        ('Resolved' , 'Resolved'),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=50, choices=REQUEST_TYPES)
    details = models.TextField()
    attachments = models.FileField(upload_to='attachments/', blank=True, null=True)
    status = models.CharField(max_length=20, default='Pending',choices=status_choice)
    submission_timestamp = models.DateTimeField(auto_now_add=True)
    resolution_timestamp = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.request_type} - {self.customer.username}"