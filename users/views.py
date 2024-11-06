from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404, redirect
from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm, UserForm, UserModeratorForm
from users.models import User
import secrets
from django.core.mail import send_mail
from django.core.exceptions import PermissionDenied


class UserCreateView(CreateView):
    login_url = "users:login"
    redirect_field_name = "redirect_to"

    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}'
        send_mail(
            subject="Подтверждение почты",
            message=f"Привет, перейди по ссылке для потвердления почты {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


class UserListView(ListView):
    model = User


class UserUpdateView(UpdateView):
    login_url = "users:login"
    redirect_field_name = "redirect_to"

    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:users_list')

    def get_success_url(self):
        return reverse('users:users_list')

    def get_form_class(self):
        user = self.request.user
        if user.is_superuser:
            return UserForm
        if user.has_perm('mailing.can_edit_status') and not user.is_superuser:
            return UserModeratorForm
        raise PermissionDenied


class UserDeleteView(DeleteView):
    login_url = "users:login"
    redirect_field_name = "redirect_to"

    model = User
    success_url = reverse_lazy('users:users_list')
