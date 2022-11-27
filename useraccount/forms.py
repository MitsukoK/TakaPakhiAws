from django import forms

from userapp.models import NewUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# class RequestForm(forms.Form):
#     template_name = "form_snippet.html"
#     # user = forms.ModelChoiceField(queryset=NewUser.objects.all())
#     money = forms.IntegerField()
#     method = forms.CharField(
#         max_length=100,
#         widget=forms.TextInput(
#             attrs={
#                 "class": "block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer",
#             }
#         ),
#     )
#     phone_number = forms.CharField(max_length=100)
#     bankid = forms.CharField(max_length=100)


# Create your forms here.


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = NewUser
        # fields = ("username", "email", "password1", "password2")
        # use all fields from the NewUser model
        # fields = "__all__"
        exclude = [
            "last_login",
            "is_superuser",
            "date_joined",
            "groups",
            "user_permissions",
            # "id_password",
            "password",
        ]

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
