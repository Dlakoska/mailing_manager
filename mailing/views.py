from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from mailing.forms import MailingForm, ClientForm, MessageForm, MailingModeratorForm
from mailing.models import Mailing, Client, Message, MailingAttempt
from django.core.exceptions import PermissionDenied
from django.views import View
from django.shortcuts import render, get_object_or_404

from mailing.services import get_cached_articles


class MainPage(View):
    """Выводит статистику"""
    def get(self, request, *args, **kwargs):
        total_mailings = Mailing.objects.count()
        active_mailings = Mailing.objects.filter(status="started").count()
        unique_clients_count = Client.objects.distinct().count()

        random_articles = get_cached_articles()

        context = {
            "total_mailings": total_mailings,
            "active_mailings": active_mailings,
            "unique_clients_count": unique_clients_count,
            "random_articles": random_articles,
        }

        return render(request, "mailing/home.html", context)


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
        if user == self.object.owner or user.is_superuser:
            return MailingForm
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


class MailingAttemptListView(LoginRequiredMixin, ListView):
    model = MailingAttempt
    template_name = "mailing/mailing_attempt_list.html"
    context_object_name = "attempts"

    def get_queryset(self):
        mailing_id = self.kwargs["mailing_id"]
        return MailingAttempt.objects.filter(mailing_id=mailing_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mailing_id = self.kwargs["mailing_id"]
        context["mailing"] = get_object_or_404(Mailing, pk=mailing_id)
        context["mailing_id"] = mailing_id
        return context