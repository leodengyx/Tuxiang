from rest_framework import serializers
from albums.models import EventAlbum
from albums.models import GroupAlbum

class EventAlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventAlbum
        fields = ('name', 'author', 'create_time','photo_count', 'uploader_count' 'reader_count', 'barcode_img')

class GroupAlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupAlbum
        fields = ('name', 'author', 'create_time', 'barcode_img', 'member_count', 'photo_count')
