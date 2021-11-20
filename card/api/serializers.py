from rest_framework import serializers
from card.models import CommentModel, IdeaModel

class IdeaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdeaModel
        fields = '__all__'

class CommentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = '__all__'