from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

from mailing.forms import MailingForm, ClientForm, MessageForm
from mailing.models import Mailing, Client, Message


class MailingListView(ListView):
    model = Mailing


class MailingDetailView(DetailView):
    model = Mailing


class MailingUpdateView(UpdateView):
    login_url = "users:login"
    redirect_field_name = "redirect_to"

    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list')

    def get_success_url(self):
        return reverse('mailing:mailing_detail', args=[self.kwargs.get('pk')])


class MailingDeleteView(DeleteView):
    login_url = "users:login"
    redirect_field_name = "redirect_to"

    model = Mailing
    success_url = reverse_lazy('mailing:mailing_list')


class MailingCreateView(CreateView):
    login_url = "users:login"
    redirect_field_name = "redirect_to"

    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list')


class ClientListView(ListView):
    model = Client


class ClientUpdateView(UpdateView):
    login_url = "users:login"
    redirect_field_name = "redirect_to"

    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')

    def get_success_url(self):
        return reverse('mailing:client_list')


class ClientDeleteView(DeleteView):
    login_url = "users:login"
    redirect_field_name = "redirect_to"

    model = Client
    success_url = reverse_lazy('mailing:client_list')


class ClientCreateView(CreateView):
    login_url = "users:login"
    redirect_field_name = "redirect_to"

    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')


class MessageListView(ListView):
    model = Message


class MessageDetailView(DetailView):
    model = Message


class MessageDeleteView(DeleteView):
    login_url = "users:login"
    redirect_field_name = "redirect_to"

    model = Message
    success_url = reverse_lazy('mailing:message_list')


class MessageCreateView(CreateView):
    login_url = "users:login"
    redirect_field_name = "redirect_to"

    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')


class MessageUpdateView(UpdateView):
    login_url = "users:login"
    redirect_field_name = "redirect_to"

    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')

    def get_success_url(self):
        return reverse('mailing:message_list')