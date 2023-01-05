from django.db import models


class Banner(models.Model):
    banner = models.TextField(verbose_name='Название банера')

    def __str__(self):
        return self.banner


class About(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    img = models.ImageField(upload_to='about_img')

    def __str__(self):
        return self.title


