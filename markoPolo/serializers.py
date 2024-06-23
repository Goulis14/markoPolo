from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Valuable


class ValuableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Valuable
        fields = ['id', 'title', 'category', 'description', 'cover_image', 'location', 'owner']


class UserSerializer(serializers.ModelSerializer):
    valuables = serializers.PrimaryKeyRelatedField(many=True, queryset=Valuable.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'valuables']
