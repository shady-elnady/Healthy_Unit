from django.shortcuts import render
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import default_storage
from django.contrib import messages
import os

from firebase_admin import db, firestore

from .strings import UsersRealTimeRef
from .models import TModel

# Create your views here.


ref = db.reference("/Shady_System")
users_ref = ref.child(UsersRealTimeRef)


def save_users(request):
    try:
        users_ref.set(
            {
                "Ashady": {
                    "full_name": "AShady El Nady",
                    "date_of_birth": "June 23, 1912",
                },
                "Aalanisawesome": {
                    "full_name": "AAlan Turing",
                    "date_of_birth": "June 23, 1912",
                },
                "Aahmed": {
                    "full_name": "AAhmed Shady",
                    "date_of_birth": "December 9, 1906",
                },
                "Agracehop": {
                    "full_name": "AGrace Hopper",
                    "date_of_birth": "December 9, 1906",
                },
            }
        )
        context = {
            "saved": True,
        }
    except:
        context = {
            "saved": False,
        }

    return render(request, "save_users.html", context)


def get_users(request):
    context = {
        "users": users_ref.get(),
    }
    return render(request, "users.html", context)


def save_to_firestroe(request):
    try:
        db = firestore.client()
        doc_ref = db.collection("users").document("alovelace")
        doc_ref.set({"first": "Ada", "last": "Lovelace", "born": 1815})
        doc_ref = db.collection("users").document("aturing")
        doc_ref.set(
            {"first": "Alan", "middle": "Mathison", "last": "Turing", "born": 1912}
        )
        context = {
            "saved": True,
        }
    except:
        context = {
            "saved": False,
        }
    return render(request, "firestroe.html", context)


def read_from_firestroe(request):
    db = firestore.client()
    users_ref = db.collection("users").stream()
    # for doc in docs:
    #     print(f"{doc.id} => {doc.to_dict()}")
    #     print("====================shady=====================================")
    # users_ref = db.collection('users').get()
    context = {
        "users": [user.to_dict() for user in users_ref],
    }
    return render(request, "read_from_firestroe.html", context)


# storage.child(PATH/DIRECTORY_ON_CLOUD).put(PATH_TO_LOCAL_IMAGE  )
## Example (same directory, same file name)
# storage.child("images/example.jpg").put("example.jpg")

