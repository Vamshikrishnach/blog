from rest_framework import serializers
from .models import *

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__' 
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
    
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__' 

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

# class ImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Image
#         fields = '__all__'
