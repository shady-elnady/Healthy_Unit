from typing import Any
from django.conf import settings
from django.http import HttpResponse, BadHeaderError
from django.utils.translation import gettext_lazy as _
from templated_email import InlineImage, send_templated_mail


class EMailSender:
    def __init__(
        self,
        *recipients,
        create_link: bool = True,
        from_email: str = settings.EMAIL_HOST_USER,
        fail_silently: bool = False,
        # cc: Any | None = None,
        # bcc: Any | None = None,
        # connection: Any | None = None,
        # headers: Any | None = None,
        # template_prefix: Any | None = None,
        # template_suffix: Any | None = None,
    ):
        self.recipients = [*recipients]
        self.from_email = from_email
        self.context = {}
        self.create_link = create_link
        self.fail_silently = fail_silently
        # self.cc = cc
        # self.bcc = bcc
        # self.connection = connectio
        # self.headers = headers
        # self.template_prefix = template_prefix
        # self.template_suffix = template_suffix

    def add_image(
        self,
        image_file_name: str,
        imageField: object = None,
    ):
        if imageField:
            # From a file
            image = imageField.read()
        else:
            with open(image_file_name, "rb") as img:
                image = img.read()
        inline_image = InlineImage(filename=image_file_name, content=image)
        if image_file_name in self.context.keys():
            raise ValueError(_("Image name is Exist."))
        else:
            self.context[image_file_name] = inline_image

    def send_template(
        self,
        template_name: str = "welcome",
        context: dict[str, Any] = None,
        **kargs: Any,
    ):
        try:
            send_templated_mail(
                template_name=template_name,
                from_email=self.from_email,
                recipient_list=self.recipients,
                context={
                    **context,
                    **self.context,
                },
                create_link=self.create_link,
                # cc=self.cc,
                # bcc=self.bcc,
                # fail_silently=self.fail_silently,
                # connection=self.connection,
                # headers=self.headers,
                # template_prefix=self.template_prefix,
                # template_suffix=self.template_suffix,
                **kargs,
            )
        except BadHeaderError:
            return HttpResponse("Invalid header found.")
        except Exception as e:
            return HttpResponse(f"Send E-Mail Error: \n \t Error is > {e}")
        # finally:
        #     self.__exit__()

    def __exit__(self):
        print("from exit fun")


"""
https://stackoverflow.com/questions/38076220/python-mysqldb-connection-in-a-class
"""
