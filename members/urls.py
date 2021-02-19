from django.urls import path
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import views as auth_views
from .views import UserRegisterView, UserUpdateView

urlpatterns = [
    path(_('register/'), UserRegisterView.as_view(), name='register'),
    path(_('edit_profile/'), UserUpdateView.as_view(), name='edit_profile'),
    path(_('password/'), auth_views.PasswordChangeView.as_view())

]
