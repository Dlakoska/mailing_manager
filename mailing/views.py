from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from mailing.forms import MailingForm, ClientForm, MessageForm, MailingModeratorForm
from mailing.models import Mailing, Client, Message
from django.core.exceptions import PermissionDenied


class MailingListView(ListView):
    model = Mailing


class MailingDetailView(DetailView):
    model = Mailing


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "users:login"
    redirect_field_name = "redirect_to"

    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list')

    def get_success_url(self):
        return reverse('mailing:mailing_detail', args=[self.kwargs.get('pk')])

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ClientForm
        if user.has_perm('mailing.can_edit_status'):
            return MailingModeratorForm
        raise PermissionDenied


class MailingDeleteView(DeleteView):
    login_url = "users:login"
    redirect_field_name = "redirect_to"

    model = Mailing
    success_url = reverse_lazy('mailing:mailing_list')


class MailingCreateView(CreateView, LoginRequiredMixin):
    login_url = "users:login"
    redirect_field_name = "redirect_to"

    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list')

    def form_valid(self, form):
        mailing = form.save(form)
        user = self.request.user
        mailing.owner = user
        mailing.save()
        return super().form_valid(form)


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

    def form_valid(self, form):
        client = form.save(form)
        user = self.request.user
        client.owner = user
        client.save()
        return super().form_valid(form)


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

    def form_valid(self, form):
        message = form.save(form)
        user = self.request.user
        message.owner = user
        message.save()
        return super().form_valid(form)


class MessageUpdateView(UpdateView):
    login_url = "users:login"
    redirect_field_name = "redirect_to"

    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')

    def get_success_url(self):
        return reverse('mailing:message_list')