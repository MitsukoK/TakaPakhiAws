from rest_framework.serializers import ModelSerializer
from userapp.models import NewUser


class NewUserSerializer(ModelSerializer):
    class Meta:
        model = NewUser
        fields = "__all__"
