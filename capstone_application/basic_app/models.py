from django.db import models
from django.core.files.base import File
import os
# SuperUserInformation
# User: Jose
# Email: training@pieriandata.com
# Password: testpassword

# Create your models here.
class ImageInfo(models.Model):

    # Create relationship (don't inherit from User!)

    # Add any additional attributes you want
    image_name = models.CharField(max_length=256)
    # pip install pillow to use this!
    # Optional: pip install pillow --global-option="build_ext" --global-option="--disable-jpeg"
    image = models.ImageField(upload_to= 'images/')
    cc_image = models.ImageField(blank=True, null=True)
    result = models.FileField(blank=True, null=True, upload_to='final/')

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.image_name

    def update_result(self, new_path):
        self.result.save(os.path.basename(new_path), File(open(new_path, "wb+")), save=True)
