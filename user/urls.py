from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register , name="register"),
    path('verify-account/', views.verify_account, name="verify_account"),
    path('forget-password/', views.send_password_reset_email, name="reset_password_email"),
    path('verify_pass_reset_link/', views.verify_pass_reset_link, name="verify_pass_reset_link"),
    path('set-password/', views.reset_password_using_link, name="reset-password"),
]