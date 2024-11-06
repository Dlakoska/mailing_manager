from users.apps import UsersConfig
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.views import UserCreateView, email_verification, UserListView, UserUpdateView, UserDeleteView

app_name = UsersConfig.name


urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='login.html'), name='logout'),
    path('register/', UserCreateView.as_view(template_name='login.html'), name='register'),
    path('email-confirm/<str:token>/', email_verification, name='email-confirm'),
    path('', UserListView.as_view(), name='users_list'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='users_update'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='users_delete')
]
