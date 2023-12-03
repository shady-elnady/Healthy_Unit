from rest_framework.serializers import HyperlinkedModelSerializer

from ...models.User import User


class UserSerializer(HyperlinkedModelSerializer):
    # User_Restaurants = UserRestaurantSerializer(many= True)

    class Meta:
        model = User
        fields = [
            "url",
            "id",
            "name",
            "national_id",
            "email",
            "mobile",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        instance.email = instance.email.lower()
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
