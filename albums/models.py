from django.db import models
from users.models import UserProfile
from photos.models import Photo

# Create your models here.
class EventAlbum(models.Model):
    name = models.CharField("Name of event album",max_length=100, blank=False)
    author = models.ForeignKey(UserProfile, related_name="eventalbum_author", blank=False)
    create_time = models.DateTimeField("Create time of event album", auto_now_add=True, blank=False)
    photo_count = models.IntegerField("Number of photos in event album", default=0)
    uploader_count = models.IntegerField("Number of uploaders in event album", default=0)
    reader_count = models.IntegerField("Number of readers in event album", default=0)
    barcode_img = models.ImageField("Barcode image of event album", upload_to="/Tuxiang_dir/album_barcode", blank=True)
    photos = models.ManyToManyField(Photo)
    uploaders = models.ManyToManyField(UserProfile, related_name="eventalbum_uploader")
    readers = models.ManyToManyField(UserProfile, related_name="eventalbum_reader")

    def __unicode__(self):
        return self.name

class GroupAlbum(models.Model):
    name = models.CharField("Name of group album", max_length=100, blank=False)
    author = models.ForeignKey(UserProfile, blank=False)
    create_time = models.DateTimeField("Create time of group album", auto_now_add=True, blank=False)
    barcode_img = models.ImageField("Barcode image of group album", upload_to="/Tuxiang_dir/album_barcode")
    member_count = models.IntegerField("Number of members in group album", default=0)
    photo_count = models.IntegerField("Number of photos in group album", default=0)
    members = models.ManyToManyField(UserProfile)
    photos = models.ManyToManyField(Photo)

    def __unicode__(self):
        return self.name