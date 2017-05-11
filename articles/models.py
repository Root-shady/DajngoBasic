from django.db import models
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=128)
    body = models.CharField(max_length=400, null=True)

def get_image_filename(instance, filename):
    title = instance.post.title
    slug = slugify(title)
    return "post_images/%s-%s" %(slug, filename)

class Images(models.Model):
    post = models.ForeignKey(Post, default=None)
    image = models.ImageField(upload_to=get_image_filename,
            verbose_name='Image', )
