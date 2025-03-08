from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Post
from .serializers import PostListSerializer, PostSerializer

# Create your views here.
# class PostListView(ListAPIView):
#     queryset = Post.postobjects.all()
#     serializer_class = PostListSerializer

class PostListView(APIView):
    def get(self, request, *arg, **kwargs):
        posts = Post.objects.all() # para poder ver todos los status, en el video pone Post.postobjects.all()
        serialized_posts = PostListSerializer(posts, many=True).data
        return Response(serialized_posts)


class PostDetailView(APIView):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        serialized_post = PostSerializer(post).data
        return Response(serialized_post)


# class PostDetailView(RetrieveAPIView):
#     queryset = Post.postobjects.all()
#     serializer_class = PostSerializer
#     lookup_field = 'slug'