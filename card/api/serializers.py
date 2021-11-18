from rest_framework import serializers
from card.models import IdeaModel

class IdeaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdeaModel
        fields = '__all__'