from instagrapi import Client
import time
from random import randint
from numpy import array

listt=array([]*100)

user=input("enter your username")
pw=input("enter your pw")

client = Client()
client.login(user,pw)

hashtag = input("enter your #")

medias = client.hashtag_medias_top(hashtag , 30)

for i, media in enumerate(medias):
    client.user_follow(media.user.pk)
    print(f"followed user {media.user.username}")

    time.sleep(1.5)