from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache

# Create your models here.
class Redirect(models.Model):

    key = models.CharField(max_length=255,unique=True)
    url = models.CharField(max_length=255,unique=True)
    active = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.key} - {self.url}"

    class Meta:
        verbose_name = 'Redirect'
        verbose_name_plural = 'Redirects'
    
    @staticmethod
    def get_instance_with_key(key:str):
        try:
            instance = Redirect.objects.get(key=key)
            return {"key": instance.key, "url": instance.url}
        except Redirect.DoesNotExist:
            return None

    @staticmethod
    def get_redirect(key:str):
        redirect=cache.get(key)
        if redirect is not None:
            return {"key": redirect.key, "url": redirect.url}
        return Redirect.get_instance_with_key(key)


@receiver(post_save, sender=Redirect)
def caching_instances(sender, instance, **kwargs) -> None:
    if not instance.active:
        cache.delete(instance.key)
    else:
        cache.set(instance.key,instance)