import requests

from bs4 import BeautifulSoup

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from snippets.permissions import IsOwnerOrReadOnly

from django.contrib.auth.models import User


class SnippetList(generics.ListCreateAPIView):

    """
    list all code snippets or create new snippet
    """

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    
    """
    retrieve, update or delete the referenced snippet
    """

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class UserList(generics.ListAPIView):
    """
    List all registered users
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    """
    See User details
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ClassifyNumber(APIView):
    """
    generate a json object given an integer number
    """

    def get(self, request, format=None):

        number = request.GET.get("number", "")

        html_doc = requests.get(f"http://numbersapi.com/{int(number)}/math").text

        soup = BeautifulSoup(html_doc, "lxml")


        properties = {
            'number': number,
            'is_even': int(number)%2==0,
            'fun_fact': soup.get_text(),
            'is_prime': False,
        }

        return Response(properties)