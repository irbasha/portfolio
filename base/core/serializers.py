from rest_framework import serializers
from core.models import Person, Profile, Skills, Experience, Education, Projects


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['bio', 'designation', 'email']


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['name', 'role']