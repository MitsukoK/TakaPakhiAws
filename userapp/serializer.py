from rest_framework.serializers import (IntegerField, ModelSerializer,
                                        Serializer, ValidationError)

from userapp.models import NewUser


class NewUserSerializer(ModelSerializer):
    class Meta:
        model = NewUser
        fields = "__all__"


# make a serializer for change pin which will take old pin and new pin (required)
class ChangePinSerializer(Serializer):
    old_pin = IntegerField(required=True)
    new_pin = IntegerField(required=True)
