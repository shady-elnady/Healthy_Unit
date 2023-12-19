import factory
from uuid import uuid4

from User.models.User import User as UserModel


class FireBaseUserFactory(factory.django.DjangoModelFactory):
    uid = factory.LazyAttribute(lambda s: uuid4())
    first_name = factory.Faker("pystr")
    last_name = factory.Faker("pystr")
    email = factory.Faker("email")
    phone = "+9551370038"

    class Meta:
        model = UserModel
