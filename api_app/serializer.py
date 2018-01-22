from rest_framework.serializers import ModelSerializer

from api_app.models import Information
from api_app.models import SocialUser



class InformationSerializer(ModelSerializer):
    class Meta:
        model = Information
        fields = '__all__'


class SocialUserSerializer(ModelSerializer):
    class Meta:
        model = SocialUser
        fields = '__all__'

        def create(self, validated_data):
            return SocialUser.objects.create(**validated_data)

