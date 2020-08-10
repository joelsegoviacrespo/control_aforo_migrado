from django.urls import path, reverse_lazy, include
from .views import login_view, register_user
from authentication import views
from django.contrib.auth.views import (
    LoginView, LogoutView,
    PasswordChangeView, PasswordChangeDoneView,
    PasswordResetView,PasswordResetDoneView, PasswordResetConfirmView,PasswordResetCompleteView,
)

from django.utils.translation import activate

activate('es')
app_name = 'accounts'

urlpatterns = [    
    path('register/', register_user, name="register"),
    
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/accounts/login'), name='logout'),
    path('password_change/', PasswordChangeView.as_view( success_url='/accounts/password_change/'), name="password_change"),
    path('password_change/done/', PasswordChangeDoneView.as_view(), name="password_change_done"),    
    
    path('password_reset/', PasswordResetView.as_view(
        template_name='registration/password_reset_form.html',
        email_template_name='registration/password_reset_email.html',
        subject_template_name='registration/password_reset_subject.txt',
        success_url=reverse_lazy('accounts:password_reset_done')
    ), name='password_reset'),
  
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    
    
    path('reset_<uidb64>_<token>/', PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html',
        success_url=reverse_lazy('accounts:password_reset_complete')
    ), name='password_reset_confirm'),   
    
    
    path('reset/done/', PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'
    ), name='password_reset_complete'),

]