from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField("Phone number of user", validators=[phone_regex], primary_key=True, max_length=20)
    thumbnail_img = models.ImageField("Thumbnail image of user", upload_to="/Tuxiang_dir/user_thumbnail", blank=True)
    barcode_img = models.ImageField("Barcode imsage of user", upload_to="/Tuxiang_dir/user_barcode", blank=True)
    friend_count = models.IntegerField("Number of friends of user", default=0)
    friends = models.ManyToManyField('self')

    def __unicode__(self):
        return self.phone_number

