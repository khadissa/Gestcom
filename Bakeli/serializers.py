# eboutique/serializers.py

from rest_framework import serializers
from Gestcom.models import *

class ClientsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Clients
        fields = ('nom', 'prenom', 'adresse', 'telephone','photo')

        def create(self, validated_data):
        	return Clients.objects.create(**validated_data)

        def update(self, instance, validated_data):
        	instance.nom = validated_data.get('nom', instance.nom)
        	instance.prenom = validated_data.get('prenom', instance.prenom)
        	instance.adresse = validated_data.get('adresse', instance.adresse)
        	instance.telephone = validated_data.get('telephone', instance.telephone)
        	instance.photo = validated_data.get('photo', instance.photo)

        	instance.save()
        	return instance

        def get(self, request):
        	clients = Clients.objects.all()
        	return Response({"clients": clients})

        	

class LunetteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lunette
        fields = ('types','photo')

        def create(self, validated_data):
        	return Lunette.objects.create(**validated_data)

        def update(self, instance, validated_data):
        	instance.types = validated_data.get('nom', instance.nom)
        	instance.photo = validated_data.get('photo', instance.photo)

        	instance.save()
        	return instance

        def get(self, request):
        	lunette = Lunette.objects.all()
        	return Response({"lunette": lunette})



class CommandeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Commandes
        fields = ('date_add', 'clients', 'lunette')