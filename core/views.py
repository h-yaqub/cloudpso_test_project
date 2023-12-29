from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView

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


class HomeView(TemplateView):
    template_name = "home.html"
