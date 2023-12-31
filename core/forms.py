from django import forms

from core import models


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = models.User
        fields = ("full_name", "username", "email")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")

        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()

        return user


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ("full_name",)


class NoteCreateForm(forms.ModelForm):
    class Meta:
        model = models.Note
        fields = "__all__"
        widgets = {
            "created_by": forms.HiddenInput(),
        }


class NoteEditForm(forms.ModelForm):
    class Meta:
        model = models.Note
        fields = ("description", "assigned_to")
