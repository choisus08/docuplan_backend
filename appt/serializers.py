from .models import Appointment;
from rest_framework import serializers;

# AppointmentSerializer
class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # the model it will serialize
        model = Appointment
        # the fields that should be included in the serialized output
        fields = ['id', 'appointment_title', 'doctor_name', 'doctor_specialist', 'address', 'date', 'time', 'notes']