from django.shortcuts import render,redirect,get_object_or_404
from datetime import datetime
from home.models import Contact
from .models import UserAccount
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from .models import ShareItem
from django.contrib.auth import authenticate, login
from .models import COABook
from django.contrib.auth import logout
from .models import Doubt
from .models import Book, BookOrder



def home(request):
    return render(request, 'home.html')

def aboutpage(request):
    return render(request, 'aboutpage.html')

def afterjoincom(request):
    return render(request, 'afterjoincom.html')

def Allresourses(request):
    return render(request, 'Allresourses.html')

def applenext(request):
    return render(request, 'applenext.html')
def askdoubt(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        doubt_text = request.POST.get('doubt')

        Doubt.objects.create(
            name=name,
            email=email,
            subject=subject,
            doubt=doubt_text
        )

        return redirect('askdoubt')  # reload page after submit

    return render(request, 'askdoubt.html')

def askdoubt1(request):
    return render(request, 'askdoubt1.html')

from django.shortcuts import render, redirect
from .models import BorrowItem

def borrow_item(request):
    if request.method == "POST":
        BorrowItem.objects.create(
            item_name=request.POST.get('item_name'),
            category=request.POST.get('category'),
            quantity=request.POST.get('quantity'),
            description=request.POST.get('description'),
            contact_info=request.POST.get('contact_info'),
        )
        return redirect('borrow_success')

    return render(request, 'borrowitem.html')


def borrow_success(request):
    return render(request, 'borrow_success.html')


def casiofx991es(request):
    return render(request, 'casiofx991es.html')


def casiofx991ms(request):
    return render(request, 'casiofx991ms.html')

def casiofx9960g(request):
    return render(request, 'casiofx9960g.html')

def community(request):
    return render(request, 'community.html')


from django.shortcuts import render
from .models import Contact

def contact(request):
    if request.method == "POST":
        print("🔥 POST REQUEST AAYI")  # DEBUG

        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        print(name, email, subject, message)  # DEBUG

        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        print("✅ DATA SAVED")

    return render(request, "contact.html")



def contact1(request):
    return render(request, 'contact1.html')



def dellnext(request):
    return render(request, 'dellnext.html')

def hpnext(request):
    return render(request, 'hpnext.html')

def lenovonext(request):
    return render(request, 'lenovonext.html')

def lenovonextcp(request):
    return render(request, 'lenovonextcp.html')

def Login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        # username = email (अगर registration में username = email रखा है)
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')   # login success
        else:
            messages.error(request, "Invalid email or password")

    return render(request, "Login.html")

def user_logout(request):
    logout(request)
    return redirect('home')


def nextbooks(request):
    return render(request, 'nextbooks.html')

def nextcalculator(request):
    return render(request, 'nextcalculator.html')

def nextlaptop(request):
    return render(request, 'nextlaptop.html')

def nextnotes(request):
    return render(request, 'nextnotes.html')




def register(request):
      if request.method == "POST":
        print("POST DATA:", request.POST)

        # CAPTCHA CHECK
        if not request.POST.get('captcha'):
            messages.error(request, "Please confirm captcha")
            return redirect('register')

        year = request.POST.get('year')
        roll = request.POST.get('roll')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        username = request.POST.get('username')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')
        hostel = request.POST.get('hostel')
        branch = request.POST.get('branch')
        choice = request.POST.get('choice')
        address = request.POST.get('address')

        if not gender or not hostel:
          messages.error(request, "Please select gender and hostel")
          return redirect('register')
        # PASSWORD MATCH CHECK
        if password != confirm:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        # USER EXISTS CHECK
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('register')

        # CREATE USER
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
           
        )
        photo = request.FILES.get('photo')
        # CREATE PROFILE
        Profile.objects.create(
        user=user,
        email=email,       
        mobile=mobile,
        roll=roll,
        year=year,
        branch=branch,
        hostel=hostel,
        gender=gender,
        choice=choice,
        address=address,
        photo=photo,
        )

        messages.success(request, "Registration successful! Please login.")
        return redirect('Login')

      return render(request, 'Registration.html')



def search(request):
    return render(request, 'search.html')

def services(request):
    return render(request, 'services.html')


def shareitem(request):
    if request.method == "POST":
        ShareItem.objects.create(
            item_name=request.POST.get('item_name'),
            category=request.POST.get('category'),
            quantity=request.POST.get('quantity'),
            description=request.POST.get('description'),
            contact_info=request.POST.get('contact_info'),
        )
        return redirect('share_success')

    return render(request, 'shareitem.html')


def share_success(request):
    return render(request, 'share_success.html')


def simplecalculater(request):
    return render(request, 'simplecalculater.html')

def COA(request):
    return render(request, "COA.html")


def rent_now(request, book_id):
    book = get_object_or_404(COABook, id=book_id)
    return render(request, 'rent_page.html')

def buy_now(request, book_id):
    book = get_object_or_404(COABook, id=book_id)
    return render(request, 'buy_page.html')

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Profile

@login_required
def edit_profile(request):
  profile, created = Profile.objects.get_or_create(user=request.user)


  if request.method == "POST":
        profile.mobile = request.POST.get("mobile")
        profile.roll = request.POST.get("roll")
        profile.year = request.POST.get("year")
        profile.branch = request.POST.get("branch")
        profile.hostel = request.POST.get("hostel")
        profile.address = request.POST.get("address")

        if 'photo' in request.FILES:
            profile.photo = request.FILES['photo']

        profile.save()
        return redirect('profile')

  return render(request, 'edit_profile.html', {'profile': profile})

@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'profile.html', {'profile': profile ,'email': request.user.email})

def Chemistry(request):
    return render(request, "Chemistry.html")
def cybersecurity(request):
    return render(request, "cybersecurity.html")
def DBMS(request):
    return render(request, "DBMS.html")
def DigitalElectronic(request):
    return render(request, "DigitalElectronic.html")
def DS(request):
    return render(request, "DS.html")
def DSTL(request):
    return render(request, "DSTL.html")
def ElectricalEngineering(request):
    return render(request, "ElectricalEngineering.html")
def ElectronicEngineering(request):
    return render(request, "ElectronicEngineering.html")
def Environment(request):
    return render(request, "Environment.html")
def HumanValue(request):
    return render(request, "HumanValue.html")
def MachinicalEngineering(request):
    return render(request, "MachinicalEngineering.html")
def Mathematics1(request):
    return render(request, "Mathematics1.html")
def Mathematics2(request):
    return render(request, "Mathematics2.html")
def Mathematics3(request):
    return render(request, "Mathematics3.html")
def Mathematics4(request):
    return render(request, "Mathematics4.html")

def PPS(request):
    return render(request, "PPS.html")
def Python(request):
    return render(request, "Python.html")
def Softskills(request):
    return render(request, "Softskills.html")
def Technical(request):
    return render(request, "Technical.html")

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
import random

def Resetpassword(request):
    if request.method == "POST":
        email = request.POST.get("email")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "Email not registered")
            return redirect("resetpassword2")  # 🔥 MUST EXIST

        otp = random.randint(100000, 999999)

        request.session['reset_email'] = email
        request.session['reset_otp'] = str(otp)

        print("OTP:", otp)

        return redirect("resetpassword2")

    return render(request, "Resetpassword.html")



# STEP 2: OTP VERIFY
def resetpassword2(request):
    if request.method == "POST":
        user_otp = request.POST.get("otp")
        session_otp = request.session.get("reset_otp")

        if user_otp == session_otp:
            return redirect("createpassword")
        else:
            messages.error(request, "Invalid OTP")
            return redirect("resetpassword2")

    return render(request, "resetpassword2.html")



# STEP 3: CHANGE PASSWORD (DB UPDATE 🔥)
from django.contrib.auth.hashers import make_password

def createpassword(request):
    if request.method == "POST":
        password = request.POST.get("password")
        email = request.session.get("reset_email")

        user = User.objects.get(email=email)
        user.password = make_password(password)
        user.save()

        # cleanup
        request.session.flush()

        messages.success(request, "Password changed successfully")
        return redirect("login")

    return render(request, "createpassword.html")

from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash

@login_required
def change_password(request):
    if request.method == "POST":
        old = request.POST['old_password']
        new = request.POST['new_password']

        if not request.user.check_password(old):
            return render(request, 'change_password.html', {
                'error': 'Old password is wrong'
            })

        request.user.set_password(new)
        request.user.save()

        update_session_auth_hash(request, request.user)
        return redirect('home')

    return render(request, 'change_password.html')


def Physics(request):
    
    return render(request, "Physics.html")



@login_required
def P_buy_book(request):
    if request.method == "POST":
        book_id = request.POST.get('book_id')

        if not book_id:
            return redirect('Physics')  # safety

        book = Book.objects.get(id=book_id)

        BookOrder.objects.create(
            user=request.user,
            book=book,
            order_type="BUY"
        )

    return redirect('Physics')


@login_required
def P_rent_book(request):
    if request.method == "POST":
        book_id = request.POST.get('book_id')

        if not book_id:
            return redirect('Physics')

        book = Book.objects.get(id=book_id)

        BookOrder.objects.create(
            user=request.user,
            book=book,
            order_type="RENT"
        )

    return redirect('Physics')

  
