from django.contrib import admin
from home.models import Contact
from .models import UserAccount
from .models import Profile
from .models import BorrowItem
from .models import ShareItem
from .models import COABook
from .models import Doubt
from .models import Book, BookOrder
# Register your models here.
admin.site.register(Contact)

@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('email','password',)

@admin.register(Profile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'roll', 'mobile', 'branch', 'year', 'get_email')
    search_fields = ('user__username', 'roll', 'mobile')
    def get_password(self, obj):
        return obj.user.password

    get_password.short_description = 'Password (hashed)'
    
    def get_email(self, obj):
        return obj.user.email

    get_email.short_description = "Email"
    
@admin.register(BorrowItem)
class BorrowItemAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'category', 'quantity', 'contact_info', 'created_at')
    search_fields = ('item_name', 'contact_info')
    list_filter = ('category',)


@admin.register(ShareItem)
class ShareItemAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'category', 'quantity', 'contact_info', 'created_at')
    search_fields = ('item_name', 'contact_info')
    list_filter = ('category',)

@admin.register(COABook)
class COABookAdmin(admin.ModelAdmin):
    list_display = ('title', 'condition', 'available', 'rent_price', 'buy_price')
    list_filter = ('condition', 'available')
    search_fields = ('title',)


@admin.register(Doubt)
class DoubtAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('subject', 'created_at')


admin.site.register(Book)
admin.site.register(BookOrder)   