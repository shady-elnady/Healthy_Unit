from django.forms import Widget
from django.contrib.auth.hashers import UNUSABLE_PASSWORD_PREFIX, identify_hasher
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _


class ReadOnlyPasswordHashWidget(Widget):
    template_name = "Widgets/read_only_password_hash.html"

    read_only = True

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        summary = []
        if not value or value.startswith(UNUSABLE_PASSWORD_PREFIX):
            summary.append({"label": gettext("No password set.")})
        else:
            try:
                hasher = identify_hasher(value)
            except ValueError:
                summary.append(
                    {
                        "label": gettext(
                            "Invalid password format or unknown hashing algorithm."
                        )
                    }
                )
            else:
                for key, value_ in hasher.safe_summary(value).items():
                    summary.append({"label": gettext(key), "value": value_})
        context["summary"] = summary
        return context

    def id_for_label(self, id_):
        return None
