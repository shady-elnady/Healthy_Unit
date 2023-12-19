# serializers.py
from rest_polymorphic.serializers import PolymorphicSerializer

from User.api.Serializers.User_Serializer import UserSerializer
from Employee.api.Serializer import EmployeeSerializer
from Doctor.api.Serializer import DoctorSerializer
from Client.api.Serializer import ClientSerializer


class UserPolymorphicSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        "User": UserSerializer,
        "Employee": EmployeeSerializer,
        "Doctor": DoctorSerializer,
        "Client": ClientSerializer,
    }
    # resource_type_field_name = 'projecttype'
