from django.shortcuts import render

# Create your views here.
from django.views import generic

from links.models import Link
from links.serializers import LinkSerializer


class PostListApi(generic.ListAPIView):
    queryset = Link.objects.filter(active=True)
    serializerClass = LinkSerializer


class PostCreateApi(generic.CreateAPIView):
    queryset = Link.objects.filter(active=True)
    serializerClass = LinkSerializer


class PostDetailApi(generic.RetrieveAPIView):
    queryset = Link.objects.filter(active=True)
    serializerClass = LinkSerializer


class PostUpdateApi(generic.UpdateAPIView):
    queryset = Link.objects.filter(active=True)
    serializerClass = LinkSerializer


class PostDeleteApi(generic.DestroyAPIView):
    queryset = Link.objects.filter(active=True)
    serializerClass = LinkSerializer



