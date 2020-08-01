from django.db import models

class insta_user_Data(models.Model):
    id_number = models.BigIntegerField()
    username = models.CharField(max_length=100)
    fullname = models.CharField(max_length=100)
    biograghy = models.CharField(max_length=500)
    profilepic_url = models.URLField()
    external_url = models.URLField()
    number_published = models.BigIntegerField()
    number_followers = models.BigIntegerField()
    number_follows = models.BigIntegerField()
    is_private = models.BooleanField()
    is_verified = models.BooleanField()

    def __str__(self):
        return self.name
