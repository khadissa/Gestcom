# eboutique/serializers.py

from rest_framework import serializers
from Gestcom.models import *

class ClientsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Clients
        fields = ('nom', 'prenom', 'adresse', 'telephone','photo')


class CommandeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Commandes
        fields = ('date_add', 'clients')