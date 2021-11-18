from rest_framework import generics
from card.models import IdeaModel
from .serializers import IdeaModelSerializer

class ListView(generics.ListCreateAPIView):
    queryset = IdeaModel.objects.all().order_by('-id')
    serializer_class = IdeaModelSerializer


class DetailView(generics.RetrieveDestroyAPIView):
    queryset = IdeaModel.objects.all()
    serializer_class = IdeaModelSerializer