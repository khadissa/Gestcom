from rest_framework import viewsets
from Gestcom.models import *
from Bakeli.serializers import *

class ClientsViewSet(viewsets.ModelViewSet):

    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer

    def get_serializer_class(self):
	    if self.request.method == 'GET':
	        return ReadClientsSerializer
	    else:
	        return self.serializer_class


class CommandeViewSet(viewsets.ModelViewSet):

    queryset = Commandes.objects.all()
    serializer_class = CommandeSerializer