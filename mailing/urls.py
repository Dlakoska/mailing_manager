from django.urls import path
from django.views.decorators.cache import cache_page
from mailing.apps import MailingConfig
from mailing.views import MailingListView, MailingDetailView, MailingUpdateView, MailingDeleteView, MailingCreateView, \
    ClientListView, ClientCreateView, ClientDeleteView, ClientUpdateView, MessageListView, MessageCreateView, \
    MessageDetailView, MessageDeleteView, MessageUpdateView, MainPage, MailingAttemptListView

app_name = MailingConfig.name

urlpatterns = [
    path('home/', cache_page(5)(MainPage.as_view()), name="home"),
    path('', MailingListView.as_view(), name='mailing_list'),
    path('<int:pk>/', MailingDetailView.as_view(), name='mailing_detail'),
    path('<int:pk>/update', MailingUpdateView.as_view(), name='mailing_update'),
    path('<int:pk>/delete', MailingDeleteView.as_view(), name='mailing_delete'),
    path('create/', MailingCreateView.as_view(), name='mailing_create'),
    path('client/', ClientListView.as_view(), name='client_list'),
    path('client/create/', ClientCreateView.as_view(), name='client_create'),
    path('client/delete/<int:pk>', ClientDeleteView.as_view(), name='client_delete'),
    path('client/update/<int:pk>', ClientUpdateView.as_view(), name='client_update'),
    path('message/', MessageListView.as_view(), name='message_list'),
    path('message/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('message/create/', MessageCreateView.as_view(), name='message_create'),
    path('message/delete/<int:pk>', MessageDeleteView.as_view(), name='message_delete'),
    path('message/update/<int:pk>', MessageUpdateView.as_view(), name='message_update'),
    path('mailings/<int:mailing_id>/attempts/', MailingAttemptListView.as_view(), name="mailing_attempt_list"),

]