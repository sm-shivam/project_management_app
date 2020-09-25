from rest_frameworks import serializers
from .models import User , Invite,UserProfile , Company


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class InviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invite
        fields = '__all__'


class UserProfile(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'