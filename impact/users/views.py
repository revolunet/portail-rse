import django.utils.http
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import (
    PasswordResetConfirmView as BasePasswordResetConfirmView,
)
from django.contrib.auth.views import PasswordResetView as BasePasswordResetView
from django.core import mail
from django.shortcuts import redirect
from django.shortcuts import render
from django.template.loader import render_to_string

import impact.settings
from .forms import UserCreationForm
from .forms import UserEditionForm
from .forms import UserPasswordForm
from .models import User
from api.exceptions import APIError
from entreprises.models import Entreprise
from entreprises.views import search_and_create_entreprise
from habilitations.models import attach_user_to_entreprise
from utils.tokens import check_token
from utils.tokens import make_token
from utils.tokens import uidb64


def creation(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            try:
                siren = form.cleaned_data["siren"]
                if entreprises := Entreprise.objects.filter(siren=siren):
                    entreprise = entreprises[0]
                else:
                    entreprise = search_and_create_entreprise(siren)
                user = form.save()
                attach_user_to_entreprise(
                    user,
                    entreprise,
                    form.cleaned_data["fonctions"],
                )
                _send_confirm_email(user)
                success_message = f"Votre compte a bien été créé. Un e-mail de confirmation a été envoyé à {user.email}. Confirmez votre e-mail avant de vous connecter."
                messages.success(request, success_message)
                return redirect("reglementations:reglementation", siren)
            except APIError as exception:
                messages.error(request, exception)
        else:
            messages.error(
                request, "La création a échoué car le formulaire contient des erreurs."
            )
    else:
        siren = request.session.get("siren")
        form = UserCreationForm(initial={"siren": siren})
    return render(request, "users/creation.html", {"form": form})


def _send_confirm_email(user):
    html_message = render_to_string(
        "users/email/confirm_email.html",
        {
            "uidb64": uidb64(user),
            "token": make_token(user, "confirm_email"),
        },
    )
    message = html_message
    mail.send_mail(
        "Confirmation de votre e-mail sur le projet Impact",
        message=message,
        from_email=impact.settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
        html_message=html_message,
    )


def confirm_email(request, uidb64, token):
    # basé sur PasswordResetConfirmView.get_user()
    try:
        uid = django.utils.http.urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (
        TypeError,
        ValueError,
        OverflowError,
        User.DoesNotExist,
        ValidationError,
    ):
        pass
    if check_token(user, "confirm_email", token):
        user.is_email_confirmed = True
        user.save()
    return redirect("/")


@login_required()
def account(request):
    if request.POST:
        if request.POST["action"] == "update-password":
            form = UserEditionForm(None, instance=request.user)
            password_form = UserPasswordForm(
                request.POST or None, instance=request.user
            )
            if password_form.is_valid():
                password_form.save()
                success_message = (
                    "Votre mot de passe a bien été modifié. Veuillez vous reconnecter."
                )
                messages.success(request, success_message)
            return redirect("account")
        else:
            form = UserEditionForm(request.POST or None, instance=request.user)
            password_form = UserPasswordForm(None, instance=request.user)
            if form.is_valid():
                form.save()

                if "email" in form.changed_data:
                    success_message = f"Votre e-mail a bien été modifié. Un e-mail de confirmation a été envoyé à {form.cleaned_data['email']}. Confirmez votre e-mail avant de vous connecter."
                    request.user.is_email_confirmed = False
                    request.user.save()
                    _send_confirm_email(request.user)
                    logout(request)
                else:
                    success_message = "Votre compte a bien été modifié."
                messages.success(request, success_message)
                return redirect("account")
        error_message = (
            "La modification a échoué car le formulaire contient des erreurs."
        )
        messages.error(request, error_message)
    form = UserEditionForm(None, instance=request.user)
    password_form = UserPasswordForm(None, instance=request.user)
    return render(
        request, "users/account.html", {"form": form, "password_form": password_form}
    )


class PasswordResetView(BasePasswordResetView):
    def form_valid(self, form):
        response = super(PasswordResetView, self).form_valid(form)
        success_message = "Un lien de ré-initialisation de votre mot de passe vous a été envoyé par mail. Vous devriez le recevoir d'ici quelques minutes."
        messages.success(self.request, success_message)
        return response


class PasswordResetConfirmView(BasePasswordResetConfirmView):
    def form_valid(self, form):
        response = super(PasswordResetConfirmView, self).form_valid(form)
        success_message = "Votre mot de passe a été réinitialisé avec succès. Vous pouvez à présent vous connecter."
        messages.success(self.request, success_message)
        return response
