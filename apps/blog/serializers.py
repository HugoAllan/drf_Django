from rest_framework import serializers


from .models import Post, Category, Headding


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'description',
            'thumbnail',
            'slug',
            'category',
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class HeaddingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Headding
        fields = [
            'title',
            'slug',
            'level',
            'order',
        ]


