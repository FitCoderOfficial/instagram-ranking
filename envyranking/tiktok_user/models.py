from django.db import models
from TikTokApi import TikTokApi

from time import sleep

class tiktok_user_Data(models.Model):
    rank = models.BigIntegerField(blank=True, null=True)
    id_number = models.BigIntegerField(blank=True, null=True)
    secUid_number = models.CharField(max_length=100, blank=True)
    username = models.CharField(max_length=100)
    fullname = models.CharField(max_length=100, blank=True)
    biograghy = models.CharField(max_length=500, blank=True, null=True)
    profilepic_url = models.URLField(max_length=500, blank=True)
    external_url = models.URLField(blank=True, null=True)
    number_videos = models.BigIntegerField(blank=True, null=True)
    number_heart = models.BigIntegerField(blank=True, null=True)
    number_followers = models.BigIntegerField(blank=True, null=True)
    number_follows = models.BigIntegerField(blank=True, null=True)
    is_private = models.BooleanField(blank=True)
    is_verified = models.BooleanField(blank=True)
    is_favorite = models.BooleanField(blank=True)

    class Meta:
        indexes = [
                models.Index(fields=['number_followers'])
                   ]

    def save(self, *args, **kwargs):
        api = TikTokApi()
        all_dic = api.getUser(self.username)

        self.id_number = all_dic['userInfo']['user']['id']
        self.secUid_number = all_dic['userInfo']['user']['secUid']
        self.fullname = all_dic['userInfo']['user']['nickname']
        self.biograghy = all_dic['userInfo']['user']['signature']
        self.profilepic_url = all_dic['userInfo']['user']['avatarThumb']
        if 'bioLink' in all_dic['userInfo']['user']:
            self.external_url = all_dic['userInfo']['user']['bioLink']['link']
        else:
            pass
        self.number_videos = all_dic['userInfo']['stats']['videoCount']
        self.number_heart = all_dic['userInfo']['stats']['heartCount'] 
        self.number_followers = all_dic['userInfo']['stats']['followerCount']
        self.number_follows = all_dic['userInfo']['stats']['followingCount']
        self.is_private = all_dic['userInfo']['user']['secret']
        self.is_verified = all_dic['userInfo']['user']['verified']
        self.is_favorite = all_dic['userInfo']['user']['openFavorite']
        
        super().save(*args, **kwargs)


    def __str__(self):
        return str(self.username)


