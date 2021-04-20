from django.contrib.auth import get_user_model

# check for unique email & username

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widged=forms.PasswodInput(
            attrs={
                "class": "form-control",
                "id": "user-password"
            }
        )
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)
        if not qs.exist():
            raise forms.ValidationError("This is an invalid user.")
        return username