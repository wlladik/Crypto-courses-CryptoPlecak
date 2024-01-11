from django.db import models
from django.contrib.auth.models import User
from PIL import Image

TYPE_ACCOUNT = (
    ('full', 'All courses'),
    ('free', 'Free courses')
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField('User photo', default='default.png', upload_to='user_images')
    acc_type = models.CharField(choices=TYPE_ACCOUNT, default='free', max_length=30)

    def __str__(self):
        return f'User profile {self.user.username}'

    def save(self, *args, **kwargs):
        super().save()

        image = Image.open(self.img.path)

        if image.height > 256 or image.width > 256:
            resize = (256, 256)
            image.thumbnail(resize)
            image.save(self.img.path)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
