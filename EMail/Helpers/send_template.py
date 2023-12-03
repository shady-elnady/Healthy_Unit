from typing import Any
from django.conf import settings
from django.http import HttpResponse, BadHeaderError
from django.utils.translation import gettext_lazy as _
from templated_email import send_templated_mail


def send_template(
    *recipients,
    template_name: str = "welcome",
    from_email: str = settings.EMAIL_HOST_USER,
    context: dict[str, Any] = None,
    create_link: bool = True,
    **kargs: Any,
):
    try:
        send_templated_mail(
            template_name=template_name,
            from_email=from_email,
            recipient_list=[*recipients],
            context=context,
            create_link=create_link,
            **kargs,
        )
    except BadHeaderError:
        return HttpResponse("Invalid header found.")
    except Exception as e:
        return HttpResponse(f"Send E-Mail Error: \n \t Error is > {e}")
