from django_countries.serializer_fields import CountryField
from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers
from .models import Property, PropertyViews

class PropertySerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    country = CountryField(name_only =True)
    class  Meta:
        model = Property
        fields =["user", "title","slug","ref_code","description","country","city","postal_code","street_address","property_number","price","tax","final_property_price","plot_area","total_floors","bedrooms","bathrooms","advert_type"]
    def get_user(self,obj):
        return obj.user.username
        
class  PropertyCreateSerializer(serializers.ModelSerializer):
    country = CountryField(name_only=True)

    class Meta:
        model =Property
        exclude=["updated_at","pkid"]
class  PropertyViewSerializer(serializers.ModelSerializer):
    country = CountryField(name_only=True)

    class Meta:
        model =PropertyViews
        exclude=["updated_at","pkid"]        