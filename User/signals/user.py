from django.conf import settings
from django.db import transaction
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.utils.translation import get_language
from django.utils.translation import gettext_lazy as _

from EMail.Helpers.email_sender import EMailSender
from ..models.User import User
from ..models.Profile import Profile


@receiver(post_save, sender=User)
def user(sender, instance, created, **kwargs):
    if created:
        with transaction.atomic():
            Profile.objects.create(user=instance)
            Token.objects.create(user=instance)
            instance.Profile.save()
            if not instance.email_verified and not instance.is_active:
                EMailSender(
                    instance.email,
                ).send_template(
                    template_name="verify_email",
                    context={
                        "verify_link": f"{settings.BASE_URL}{get_language()}/verify_account_email/{instance.national_id}/",
                    },
                )
    else:
        if not instance.is_active and instance.email_verified:
            EMailSender(
                instance.email,
            ).send_template(
                template_name="welcome",
                context={
                    "name": instance.name,
                    "logIn_url": f"{settings.BASE_URL}{get_language()}/log_in/",
                    "message": _(
                        "Thank you for joining us.\n Log In To Active Your Account.",
                    ),
                },
            )
