from django.contrib import admin
from django.urls import path, include
from home import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.home, name='home'),
    path('aboutpage/',views.aboutpage, name='aboutpage'),
    path('afterjoincom/',views.afterjoincom, name='afterjoincom'),
    path('Allresourses/',views.Allresourses, name='Allresourses'),
    path('applenext/',views.applenext, name='applenext'),
    path('ask-doubt/', views.askdoubt, name='askdoubt'),
    path('askdoubt1/',views.askdoubt1, name='askdoubt1'),
    path('borrow/', views.borrow_item, name='borrowitem'),
    path('borrow/success/', views.borrow_success, name='borrow_success'),
    path('casiofx991es/',views.casiofx991es, name='casiofx991es'),
    path('casiofx991ms/',views.casiofx991ms, name='casiofx991ms'),
    path('casiofx9960g/',views.casiofx9960g, name='casiofx9960g'),
    path('community/',views.community, name='community'),
    path('contact/',views.contact, name='contact'),
    path('contact1/',views.contact1, name='contact1'),

    path('dellnext/',views.dellnext, name='dellnext'),
    path('hpnext/',views.hpnext, name='hpnext'),
    path('lenovonext/',views.lenovonext, name='lenovonext'),
    path('lenovonextcp/',views.lenovonextcp, name='lenovonextcp'),
    path('Login/', views.Login, name='Login'),
    path('nextbooks/',views.nextbooks, name='nextbooks'),
    path('nextcalculator/',views.nextcalculator, name='nextcalculator'),
    path('nextlaptop/',views.nextlaptop, name='nextlaptop'),
    path('nextnotes/',views.nextnotes, name='nextnotes'),

    path('Registration/', views.register, name='register'),

    path('search/',views.search, name='search'),
    path('services/',views.services, name='services'),
    path('share/', views.shareitem, name='shareitem'),
    path('COA/', views.COA, name='COA'),
    path('share-success/', views.share_success, name='share_success'),
    path('simplecalculater/',views.simplecalculater, name='simplecalculater'),
    path('COA/rent/', views.rent_now, name='rent_now'),
    path('COA/buy/', views.buy_now, name='buy_now'),
    path('logout/', views.user_logout, name='logout'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('profile/', views.profile, name='profile'),
    path('Chemistry/', views.Chemistry, name='Chemistry'),
    path('cybersecurity/', views.cybersecurity, name='cybersecurity'),
    path('DBMS/', views.DBMS, name='DBMS'),
    path('DigitalElectronic/', views.DigitalElectronic, name='DigitalElectronic'),
    path('DS/', views.DS, name='DS'),
    path('DSTL/', views.DSTL, name='DSTL'),
    path('ElectricalEngineering/', views.ElectricalEngineering, name='ElectricalEngineering'),
    path('ElectronicEngineering/', views.ElectronicEngineering, name='ElectronicEngineering'),
    path('Environment&Ecology/', views.Environment, name='Environment&Ecology'),
    path('HumanValue/', views.HumanValue, name='HumanValue'),
    path('MachinicalEngineering/', views.MachinicalEngineering, name='MachinicalEngineering'),
    path('Mathematics1/', views.Mathematics1, name='Mathematics1'),
    path('Mathematics2/', views.Mathematics2, name='Mathematics2'),
    path('Mathematics3/', views.Mathematics3, name='Mathematics3'),
    path('Mathematics4/', views.Mathematics4, name='Mathematics4'),
    path('Physics/', views.Physics, name='Physics'),
    
    path('PPS/', views.PPS, name='PPS'),
    path('Python/', views.Python, name='Python'),
    path('Softskills/', views.Softskills, name='Softskills'),
    path('Technical/', views.Technical, name='Technical'),
    path('Resetpassword/', views.Resetpassword, name='Resetpassword'),
    path('resetpassword2/', views.resetpassword2, name='resetpassword2'),
    path('createpassword/', views.createpassword, name='createpassword'),
      path(
        'change-password/',
        auth_views.PasswordChangeView.as_view(
            template_name='change_password.html'
        ),
        name='change_password'
    ),
    path(
        'change-password-done/',
        auth_views.PasswordChangeDoneView.as_view(
            template_name='change_password_done.html'
        ),
        name='password_change_done'
    ),

     
    path("P_rent_book/", views.P_rent_book, name="P_rent_book"),
    path("P_buy_book/", views.P_buy_book, name="P_buy_book"),
]