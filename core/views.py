from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models
from . import forms


class RegisterView(View):
    form = forms.UserCreationForm
    template_name = "registration/register.html"

    def get(self, request):
        context = {
            "register_form": self.form(),
        }

        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form(request.POST)

        if form.is_valid():
            form.save()

            return redirect("login")

        context = {
            "register_form": form,
        }

        return render(request, self.template_name, context)


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "home.html"


class UpdateUserView(LoginRequiredMixin, UpdateView):
    model = models.User
    form_class = forms.UserUpdateForm
    template_name = "user_update.html"
    success_url = reverse_lazy("core:home")


class NoteListView(LoginRequiredMixin, ListView):
    template_name = 'notes_list.html'
    context_object_name = 'notes'

    def get_queryset(self):
        _user = self.request.user
        if _user.is_superuser:
            return models.Note.objects.all()

        queryset = self.request.user.assigned_notes.all()

        return queryset


class CreateNoteView(LoginRequiredMixin, CreateView):
    model = models.Note
    form_class = forms.NoteCreateForm
    template_name = "note_form.html"
    success_url = reverse_lazy("core:notes_list")


class EditNoteView(LoginRequiredMixin, UpdateView):
    model = models.Note
    form_class = forms.NoteEditForm
    template_name = "note_form.html"
    success_url = reverse_lazy("core:notes_list")

class DeleteNoteView(LoginRequiredMixin, DeleteView):
    model = models.Note
    template_name = "note_confirm_delete.html"
    success_url = reverse_lazy("core:notes_list")


class DetailNoteView(DetailView):
    model = models.Note
    template_name = 'note_detail.html'
    context_object_name = 'note'
