from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class WinePal(models.Model):
    # model for creating a profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    img = models.ImageField(
        upload_to='images/', default='../default_user_p5nq8r'
    )

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.user}'s Winerypals profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        WinePal.objects.create(user=instance)


post_save.connect(create_profile, sender=User)
