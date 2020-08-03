from django.db import models

class just_insta_id(models.Model):
    username = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username 


class insta_user_Data(models.Model):
    id_number = models.BigIntegerField()
    username = models.ForeignKey(just_insta_id, on_delete=models.CASCADE)
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
        return self.username
