from django.db import models
from igramscraper.instagram import Instagram


class just_insta_id(models.Model):
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username 


class insta_user_Data(models.Model):
    id_number = models.BigIntegerField(blank=True)
    username = models.CharField(max_length=100)
    #username = models.OneToOneField(just_insta_id, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=100, blank=True)
    biograghy = models.CharField(max_length=500, blank=True, null=True)
    profilepic_url = models.URLField(blank=True)
    external_url = models.URLField(blank=True, null=True)
    number_published = models.BigIntegerField(blank=True)
    number_followers = models.BigIntegerField(blank=True)
    number_follows = models.BigIntegerField(blank=True)
    is_private = models.BooleanField(blank=True)
    is_verified = models.BooleanField(blank=True)

    def save(self, *args, **kwargs):
        instagram = Instagram()
        account = instagram.get_account(self.username)
        self.id_number = account.identifier
        self.fullname = account.full_name
        self.biograghy = account.biography.encode('utf-8')
        self.profilepic_url = account.get_profile_picture_url()
        self.external_url = account.external_url
        self.number_published = account.media_count
        self.number_followers = account.followed_by_count
        self.number_follows = account.follows_count
        self.is_private = account.is_private
        self.is_verified = account.is_verified
        super().save(*args, **kwargs)


    def __str__(self):
        return str(self.username)
