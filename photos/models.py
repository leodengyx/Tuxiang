from django.db import models
from users.models import UserProfile

# Create your models here.
class Photo(models.Model):
    name = models.CharField("Name of photo", max_length=100, primary_key=True)
    author = models.ForeignKey(UserProfile, blank=False)
    description = models.TextField("Description of photo", blank=True)
    upload_time = models.DateTimeField("Time of uploading photo", auto_now_add=True)
    take_time = models.DateTimeField("Time of taking photo", blank=True)
    small_img = models.ImageField("Small version of photo", upload_to="/Tuxiang_dir/small_photo", blank=True)
    middle_img = models.ImageField("Normal version of photo", upload_to="/Tuxiang_dir/middle_photo", blank=True)
    origin_img = models.ImageField("Origin version of photo", upload_to="/Tuxiang_dir/origin_photo", blank=False)
    comment_count = models.IntegerField("Number of comment in photo", default=0)
    thumb_count = models.IntegerField("Number of thumb in photo", default=0)
    comments = models.ManyToManyField('Comment', related_name="photo_comment")
    thumbs = models.ManyToManyField('Thumb', related_name="photo_thumb")

    def __unicode__(self):
        return self.name

class Comment(models.Model):
    author = models.ForeignKey(UserProfile, blank=False)
    text = models.TextField("Text of comment", blank=False)
    create_time = models.DateTimeField("Create time of comment", auto_now_add=True)
    photo = models.ForeignKey(Photo)


class Thumb(models.Model):
    author = models.ForeignKey(UserProfile, blank=False)
    create_time = models.DateTimeField("Create time of thumb", auto_now_add=True)
    photo = models.ForeignKey(Photo)

class Photoer(models.Model):
    first_name = models.CharField("First name", max_length=10)
    last_name = models.CharField("Last name", max_length=10)
    photo = models.ForeignKey(Photo)