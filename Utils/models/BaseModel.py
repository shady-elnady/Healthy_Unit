# from django.db import models
import uuid
from django.db.models import (
    Model,
    UUIDField,
    AutoField,
    CharField,
    DateTimeField,
    ImageField,
    FileField,
    PositiveSmallIntegerField,
)
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.conf import settings

from Utils.Custom_Fields import BarCodeField
from .Methods import (
    upload_image_to,
    upload_logo_to,
    upload_file_to,
    upload_svg_to,
)

# Create your models here.


class BaseTimeStampModel(Model):
    created_at = DateTimeField(
        auto_now_add=True,
        editable=False,
        db_index=True,
        verbose_name=_("Created at"),
    )
    last_updated = DateTimeField(
        auto_now=True,
        editable=False,
        verbose_name=_("Last Update"),
    )

    class Meta:
        ordering = "-last_updated"
        abstract = True


class BaseAutoIncrementModel(Model):
    id = AutoField(
        primary_key=True,
        verbose_name=_("ID"),
    )

    @property
    def slug(self) -> str:
        return slugify(f"{self.id}")

    class Meta:
        abstract = True


class BaseUUIDModel(Model):
    uid = UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name=_("UID"),
    )

    def __str__(self) -> str:
        return str(self.uid)

    def __decode__(self) -> str:
        return str(self.uid)

    @property
    def slug(self) -> str:
        return slugify(f"{self.uid}")

    class Meta:
        abstract = True


class BaseModel(BaseAutoIncrementModel, BaseTimeStampModel):
    class Meta:
        abstract = True


class BaseUUIDTimeModel(BaseUUIDModel, BaseTimeStampModel):
    photo_url = ImageField(
        upload_to=upload_image_to,
        null=True,
        blank=True,
        verbose_name=_("Photo URL"),
    )
    class Meta:
        abstract = True


class BaseBarCodeModel(BaseTimeStampModel):
    bar_code = BarCodeField(
        verbose_name=_("BarCode"),
    )

    @property
    def slug(self) -> str:
        return slugify(f"{self.bar_code}")

    class Meta:
        abstract = True


class BaseNameModel(BaseTimeStampModel):
    name = CharField(
        max_length=50,
        unique=True,
        error_messages={"unique": _("Name is Used ,it must be Unique")},
        verbose_name=_("Name"),
    )

    def __str__(self) -> str:
        return f"{self.name}"

    def __decode__(self) -> str:
        return f"{self.name}"

    class Meta:
        abstract = True


class BaseAutoIncrementNameModel(
    BaseAutoIncrementModel,
    BaseNameModel,
):
    class Meta:
        abstract = True


class BaseNativeModel(BaseAutoIncrementNameModel):
    native = CharField(
        max_length=20,
        unique=True,
        error_messages={"unique": _("Native Name is Used ,it must be Unique")},
        null=True,
        blank=True,
        verbose_name=_("Native"),
    )

    @property
    def slug(self) -> str:
        return slugify(f"{self.id}")

    def __str__(self) -> str:
        return f"{self.native}"

    def __decode__(self) -> str:
        return f"{self.native}"

    class Meta:
        abstract = True
        # indexes = [
        #     TextIndex(fields=['name', 'native'])
        # ]


class BaseEmojiModel(BaseAutoIncrementNameModel):
    emoji = CharField(
        max_length=5,
        unique=True,
        error_messages={"unique": _("Emoji is Used ,it must be Unique")},
        null=True,
        blank=True,
        verbose_name=_("Emoji"),
    )

    class Meta:
        abstract = True


############################


class BaseLogoModel(BaseAutoIncrementNameModel):
    logo = ImageField(
        upload_to=upload_logo_to,
        null=True,
        blank=True,
        verbose_name=_("Logo"),
    )

    class Meta:
        abstract = True


class BaseImageModel(Model):
    image = ImageField(
        upload_to=upload_image_to,
        null=True,
        blank=True,
        verbose_name=_("Image"),
    )

    class Meta:
        abstract = True


class BaseFileModel(Model):
    file = FileField(
        upload_to=upload_file_to,
        null=True,
        blank=True,
        verbose_name=_("File"),
    )

    class Meta:
        abstract = True


class BaseSVGModel(Model):
    svg_img = ImageField(
        upload_to=upload_svg_to,
        null=True,
        blank=True,
        verbose_name=_("SVG Image"),
    )

    class Meta:
        abstract = True


class AgeModel(Model):
    day = PositiveSmallIntegerField(
        default=0,
        verbose_name=_("Day"),
    )
    month = PositiveSmallIntegerField(
        default=0,
        verbose_name=_("Month"),
    )
    year = PositiveSmallIntegerField(
        default=0,
        verbose_name=_("Year"),
    )

    class Meta:
        abstract = True
