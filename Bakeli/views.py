from rest_framework import viewsets
from rest_framework.views import APIView
from Gestcom.models import *
from Bakeli.serializers import *

class ClientsViewSet(viewsets.ModelViewSet):

    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer

class LunetteViewSet(viewsets.ModelViewSet):
	
	queryset = Lunette.objects.all()
	serializer_class = LunetteSerializer


class CommandeViewSet(viewsets.ModelViewSet):

    queryset = Commandes.objects.all()
    serializer_class = CommandeSerializer