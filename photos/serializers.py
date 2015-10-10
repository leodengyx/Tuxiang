from rest_framework import serializers
from photos.models import Photo
from photos.models import Comment
from photos.models import Thumb

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('name', 'author', 'description', 'upload_time', 'take_time', 'small_img', 'middle_img', 'origin_img', 'comment_count', 'thumb_count')

class CommentSerializer(serializers.ModelSerializer):
    class meta:
        model = Comment
        fields = ('author','text','create_time', 'photo')

class ThumbSerializer(serializers.Serializer):
    class Meta:
        model = Thumb
        fields = ('author', 'create_time', 'photo')


