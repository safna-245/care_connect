from rest_framework import serializers

from staff.models import Doctor

class DoctorSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)

    name = serializers.CharField()

    specialization = serializers.ChoiceField(choices=Doctor.SPECIALIZATION_OPTIONS)

    fee = serializers.IntegerField()

    qualification = serializers.CharField()

    email = serializers.EmailField()


