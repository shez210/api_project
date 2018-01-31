from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from api_app.models import Information
# from api_app.models import SocialUser

UserModel = get_user_model()


class InformationSerializer(ModelSerializer):
    class Meta:
        model = Information
        fields = '__all__'


class UserSerializer(ModelSerializer):
    def create(self, validated_data):
        user = super().create(validated_data)
        # user = UserModel.objects.create(first_name=validated_data['first_name'], last_name=validated_data['last_name'], email=validated_data['email'], username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'email', 'username', 'password')
