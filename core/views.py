from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

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

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("account_login")

        return super().dispatch(request, *args, **kwargs)
