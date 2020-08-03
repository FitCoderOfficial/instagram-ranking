from celery import shared_task
from .models import insta_user_Data
from igramscraper.instagram import Instagram

def create_insta_user_data(user_id):
    instagram = Instagram()
    account = instagram.get_account(user_id)
    id_number = account.identifier
    username = account.username
    fullname = account.full_name
    biograghy = account.biography
    profilepic_url = account.get_profile_picture_url()
    external_url = account.external_url
    number_published = account.media_count
    number_followers = account.followed_by_count
    number_follows = account.follows_count
    is_private = account.is_private
    Is_verified = account.is_verified
    print("creating user data ..")

    insta_user_Data.objects.create(
            id_number=id_number,
            username=username,
            fullname=fullname,
            biograghy=biograghy,
            profilepic_url=profilepic_url,
            external_url=external_url,
            number_published=number_published,
            number_followers=number_followers,
            is_private=is_private,
            Is_verified=Is_verified,
            )


