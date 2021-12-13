from django.urls import path
from .import views
from django.contrib.auth import views as auth_view


urlpatterns = [
    # path('login/', views.login, name='login'),
    # class based views requires as_view method
    # 4 step process to reset password
    path('forget_password/', auth_view.PasswordResetView.as_view(template_name='resetpass.html'), name = 'resetpass'),
    # gives message to tell the user to check email after sending the link
    path('finishedreset/', auth_view.PasswordResetDoneView.as_view(template_name='PasswordResetDone.html'), name = 'password_reset_done'),
    # email will be sent with a link which will then redirect you to aform that you can input new password
    # 3rd step is confirming and it requires passing in uid b64 token, a secure way for django to send the password reset
    path('forget_password_confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='PasswordResetConfirmView.html'), name = 'password_reset_confirm'),
    # completes password reset
    path('forget_password_complete/', auth_view.PasswordResetCompleteView.as_view(template_name='PasswordResetCompleteView.html'), name = 'password_reset_complete'),
    

]