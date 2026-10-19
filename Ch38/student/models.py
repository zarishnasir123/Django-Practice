# models.py
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, FileExtensionValidator


#pin code must be exactly 6 digits
def validate_pin_length(value):
    if len(str(value)) != 6:
        raise ValidationError('Pin code must be exactly 6 digits')


#provinces and territories of Pakistan
STATE_CHOICES = [
    ('Punjab', 'Punjab'),
    ('Sindh', 'Sindh'),
    ('Khyber Pakhtunkhwa', 'Khyber Pakhtunkhwa'),
    ('Balochistan', 'Balochistan'),
    ('Islamabad Capital Territory', 'Islamabad Capital Territory'),
    ('Gilgit-Baltistan', 'Gilgit-Baltistan'),
    ('Azad Jammu and Kashmir', 'Azad Jammu and Kashmir'),
]


class Profile(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.PositiveIntegerField(
        help_text='6 digits only',
        validators=[validate_pin_length])
    state = models.CharField(max_length=50, choices=STATE_CHOICES)
    mobile = models.CharField(
        max_length=13,
        help_text='Pakistani mobile number, e.g. 03001234567 or +923001234567',
        validators=[RegexValidator(r'^(\+92|0)3\d{9}$', 'Enter a valid mobile number, e.g. 03001234567')])
    email = models.EmailField()
    job_city = models.CharField(max_length=100)
    profile_image = models.ImageField(
        upload_to='profileimg',
        blank=True,
        help_text='Allowed: jpg, jpeg, png, gif, webp',
        validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'gif', 'webp'])])
    my_file = models.FileField(
        upload_to='doc',
        blank=True,
        help_text='Allowed: pdf, doc, docx',
        validators=[FileExtensionValidator(['pdf', 'doc', 'docx'])])