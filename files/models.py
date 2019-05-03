from django.db import models

# Create your models here.
class Upload_File(models.Model):
    File_Name = models.ImageField(upload_to='upload_files')
