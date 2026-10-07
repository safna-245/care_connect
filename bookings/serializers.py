from rest_framework import serializers
from datetime import datetime
from staff.models import Doctor

class AppointmentSerializer(serializers.Serializer):

    patient_name = serializers.CharField()
    
    phone = serializers.CharField()

    doctor = serializers.PrimaryKeyRelatedField(
    queryset=Doctor.objects.all()
)
    
    appointment_date = serializers.DateField()
    
    token_number = serializers.IntegerField(read_only = True)
    
    appointment_time = serializers.TimeField(read_only = True)
    
    problem = serializers.CharField()
    
    created_at = serializers.DateTimeField(read_only =True)

    def validate(self, validated_data):
        
        appointment_date = validated_data.get("appointment_date")


        if appointment_date < datetime.today().date():

            raise serializers.ValidationError("invalid date")

        return validated_data




    