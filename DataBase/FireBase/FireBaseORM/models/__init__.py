import os
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from FireBase.FireBaseORM.models.fields import *
from FireBase.FireBaseORM.models.base import Model
from FireBase.FireBaseORM.models.manager import Manager

import firebase_admin
from firebase_admin import credentials, auth, storage, firestore

CERTIFICATE = getattr(settings, "FIREBASE_ORM_CERTIFICATE", None)
BUCKET_NAME = getattr(settings, "FIREBASE_ORM_BUCKET_NAME", None)

if CERTIFICATE is None:
    raise ImproperlyConfigured(
        "You havent set the FIREBASE_ORM_CERTIFICATE in your settings.py"
    )
if BUCKET_NAME is None:
    raise ImproperlyConfigured(
        "You havent set the FIREBASE_ORM_BUCKET_NAME in your settings.py"
    )

firebase_admin.initialize_app(
    credentials.Certificate(CERTIFICATE),
    {
        "storageBucket": BUCKET_NAME,
        "databaseURL": "https://shady-system-a5170-default-rtdb.firebaseio.com",
        "databaseAuthVariableOverride": {
            "uid": "my-service-worker",  # or None
        },
    },
)


if not Manager.db:
    Manager.db = firebase_admin.firestore.client()
    Manager.bucket = firebase_admin.storage.bucket()
