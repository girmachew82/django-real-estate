from django.contrib.auth import get_user_model
from django_countries.serializer_fields import CountryField
from djoser.serializers import UserCreateSerializer
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    sex = serializers.CharField(source="profile.sex")
    phone_number = PhoneNumberField(source="profile.phone_number")
    profile_photo = serializers.ImageField(source="profile.photo")
    country = CountryField(source="profile.country")
    city = serializers.CharField(source="profile.city")
    top_seller = serializers.BooleanField(source="profile.top_seller")
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()        
    full_name = serializers.SerializerMethodField()    

    class Meta:
        model=User
        fields =['id','username','email','first_name','last_name','full_name','sex','phone_number','country','city','top_seller','profile_photo']

    def get_first_name(self, obj):
        return obj.first_name.title()
    def get_last_name(self, obj):
        return obj.last_name.title() 
    def get_full_name(self, obj):
        return obj.get_full_name
    def to_representation(self, instance):
        representation = super(UserSerializer, self).to_representation(instance)
    
        if instance.is_superuser:
            representation['admin'] = True
        return representation
    

class CreateUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields =['id','username','email','first_name','last_name','password']
        