from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# for contact 
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.EmailField(max_length=122)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
     
class UserAccount(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email
    
# for Regiatation 

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15)
    roll = models.CharField(max_length=50)
    year = models.CharField(max_length=10)
    branch = models.CharField(max_length=20)
    hostel = models.CharField(max_length=10)

    gender = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    gender = models.CharField(max_length=1, choices=gender, null=True, blank=True)

    choice = models.CharField(max_length=100, null=True, blank=True)

    photo = models.ImageField(
        upload_to='profile_photos/',
        default='profile_photos/default.png',
        blank=True,
        null=True
    )
    address = models.TextField()
    
    
    email = models.EmailField(max_length=122, null=True, blank=True)

    def __str__(self):
        return self.user.username

    
# for borrowitem 
class BorrowItem(models.Model):
    CATEGORY_CHOICES = [
        ('book', 'Book / Notebook'),
        ('laptop', 'Laptop'),
        ('calculator', 'Calculator'),
        ('other', 'Other'),
    ]

    item_name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    quantity = models.PositiveIntegerField()
    description = models.TextField()
    contact_info = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item_name
    
# For Shareitem
class ShareItem(models.Model):
    CATEGORY_CHOICES = [
        ('book', 'Book / Notebook'),
        ('laptop', 'Laptop'),
        ('calculator', 'Calculator'),
        ('other', 'Other'),
    ]

    item_name = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    quantity = models.PositiveIntegerField()
    description = models.TextField()
    contact_info = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item_name

# book rent COA 
class COABook(models.Model):
    CONDITION_CHOICES = [
        ('New', 'New'),
        ('Good', 'Good'),
        ('Fair', 'Fair'),
        ('Poor', 'Poor'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='books/')
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, default='Good')
    available = models.BooleanField(default=True)
    rent_price = models.DecimalField(max_digits=6, decimal_places=2)  # ₹70.00 etc
    buy_price = models.DecimalField(max_digits=6, decimal_places=2)   # ₹420.00 etc

    def __str__(self):
        return self.title

from django.db import models

class Doubt(models.Model):
    SUBJECT_CHOICES = [
        ('math', 'Mathematics'),
        ('physics', 'Physics'),
        ('chemistry', 'Chemistry'),
        ('computer', 'Computer Science'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES)
    doubt = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
    
class PasswordResetOTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email
 

class Book(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="books/")
    rent_price = models.IntegerField()
    buy_price = models.IntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class BookOrder(models.Model):
    ORDER_TYPE = (
        ('RENT', 'Rent'),
        ('BUY', 'Buy'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    order_type = models.CharField(max_length=10, choices=ORDER_TYPE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.book.title} ({self.order_type})"
