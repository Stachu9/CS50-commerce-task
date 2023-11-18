from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Categories(models.Model):
    category = models.CharField(max_length=64)

    def __str__(self):
        return f"this is {self.category}"
    
class Items(models.Model):
    itemName = models.CharField(max_length=64)
    description = models.CharField(max_length=500, null=True, blank=True)
    photoURL = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="auctions")
    initialPrice = models.FloatField()
    item_category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name="items_in_category", null=True, blank=True)

    def __str__(self):
        return f"{self.created_by} listed: {self.itemName} description: {self.description}, category: {self.item_category} added at: {self.created_at.strftime('%d, %b %Y - %HH%Mm')} \n"
    
class Bids(models.Model):
    bid_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_bids")
    bid_item = models.ForeignKey(Items, on_delete=models.CASCADE, related_name="item_bids")
    price = models.FloatField()
    bid_time = models.DateTimeField(auto_now_add=True)

class Comments(models.Model):
    commented_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comments")
    commented_item = models.ForeignKey(Items, on_delete=models.CASCADE, related_name="item_comments")
    comment_text = models.CharField(max_length=500)
    comment_time = models.DateTimeField(auto_now_add=True)

class Watchlist(models.Model):
    watched_item = models.ForeignKey(Items, on_delete=models.CASCADE)
    watched_by = models.ForeignKey(User, on_delete=models.CASCADE)

