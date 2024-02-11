from django.db import models
from django.contrib.auth.models import User
from PIL import Image

CHOICES = (('undefined', 'undefined'), ('male', 'Male'), ('female', 'Female'), ('other', 'Other'))


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField('Photo', default='profile-default.png', upload_to='user_img')
    sex = models.CharField('Sex', max_length=10, choices=CHOICES, default='undefined')
    send_email = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.img.path)
        if img.height > 256 or img.width > 256:
            resize = (256, 256)
            img.thumbnail(resize)
            img.save(self.img.path)


class Messages(models.Model):
    title = models.CharField('Topic', blank=False, max_length=100)
    sender = models.EmailField('Sender', blank=False, null=False)
    text = models.TextField('Text', blank=False)

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        return self.title
