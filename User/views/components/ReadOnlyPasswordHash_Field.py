from django.forms import Field
from django.utils.translation import gettext_lazy as _

from ..widgets.ReadOnlyPasswordHash_Widget import ReadOnlyPasswordHashWidget


class ReadOnlyPasswordHashField(Field):
    widget = ReadOnlyPasswordHashWidget

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("required", False)
        kwargs.setdefault("disabled", True)
        super().__init__(*args, **kwargs)
