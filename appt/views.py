from .models import Appointment;
from rest_framework import viewsets, permissions;
from .serializers import AppointmentSerializer;

# Create your views here.
class AppointmentViewSet(viewsets.ModelViewSet):
    # queryset is a list of all Appointment objects
    queryset = Appointment.objects.all()
    # The serializer_class attribute is used to control which serializer class should be used for serializing and deserializing queryset and model instances.
    serializer_class = AppointmentSerializer
    # Set permission_classes to allow unrestricted access to the API.
    permission_classes = [permissions.AllowAny]