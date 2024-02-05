from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass



class Bid(models.Model):
    bid = models.FloatField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='user_bid')


class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name
    

class Listing(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    image_url = models.CharField(max_length=4000)
    price = models.ForeignKey(Bid,on_delete=models.CASCADE, blank=True, null=True, related_name='price_bid' )
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='listing_owner')
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name='listing_category' )
    watch_list = models.ManyToManyField(User, blank=True, related_name='listing_watchlist')
    

    def __str__(self):
        return self.title



class Comment(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null=True, related_name='user_comment')
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, blank=True, null=True, related_name='listing_comment')
    message = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.author} comment on {self.listing}"
    
