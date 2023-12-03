import os
from typing import Any
from django.conf import settings
from django.template.loader import render_to_string
from django.http import HttpResponse, BadHeaderError
from django.utils.translation import gettext_lazy as _
from django.core.mail import get_connection, send_mail, send_mass_mail

import os
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags


class EMailHelper:
    def __init__(
        self,
        *recipients,
    ):
        self._conn = get_connection(fail_silently=False)
        self.recipients = [*recipients]
        self.from_email = settings.EMAIL_HOST_USER
        self.measages = ()

    def __enter__(self):
        return self

    def __connect__(self):
        return self._conn

    def html_meassage(
        self,
        subject: str,
        template_name: str,
        context: dict[str, Any] = None,
    ):
        try:
            html_message = render_to_string(
                template_name=os.path.join(settings.TEMPLATE_DIR, "emails", template_name),
                context=context,
            )
            plain_message = strip_tags(html_message)
            message = EmailMultiAlternatives(
                subject=subject,
                body=plain_message,
                from_email=self.from_email,
                to=self.recipients,
                # connection=self.__connect__(),
            )
            message.attach_alternative(html_message, "text/html")
            message.send()
        except BadHeaderError:
            return HttpResponse("Invalid header found.")
        except Exception as e:
            return HttpResponse(f"Sen E-Mail Error > {e}")

    def send(
        self,
        subject: str,
        message: str,
        template_name: str = None,
        context: dict[str, Any] = None,
    ):
        if template_name:
            html_message = render_to_string(
                template_name=os.path.join(
                    settings.TEMPLATE_DIR, "emails", template_name
                ),
                context=context,
            )
        else:
            html_message = None
        try:
            send_mail(
                subject=subject,
                message=message,
                from_email=self.from_email,
                recipient_list=self.recipients,
                fail_silently=False,
                html_message=html_message,
                connection=self.__connect__(),
            )
        except BadHeaderError:
            return HttpResponse("Invalid header found.")
        except Exception as e:
            return HttpResponse(f"Sen E-Mail Error > {e}")

    def add_measage(
        self,
        subject: str,
        message: str,
        recipient_list: [str] = None,
    ):
        if not recipient_list:
            recipient_list = self.recipients
        measage = (
            subject,
            message,
            self.from_email,
            recipient_list,
        )
        self.measages = (*self.measages, measage)

    def send_many(self):
        send_mass_mail(
            datatuple=self.measages(),
            fail_silently=False,
            connection=self.__connect__(),
        )

    def __disconnect__(self):
        print("disconnect")
        self.__connect__().close()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__")
        self.__disconnect__()


"""
https://stackoverflow.com/questions/38076220/python-mysqldb-connection-in-a-class
"""
