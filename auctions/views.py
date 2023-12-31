from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import *

from .models import User


def index(request):
    return render(request, "auctions/index.html", {"items": Items.objects.all()})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
    
def createListing(request):
    if request.method == "POST":
        user = request.user.id
        itemName = request.POST["itemName"]
        description = request.POST["description"]
        picture = request.POST["picURL"]
        initialPrice = request.POST["initialPrice"]
        category = request.POST["category"]

        # newListing = Items.objects.create(itemName=itemName, description=description, photoURL=picture, created_by_id=1, item_category_id=5, initialPrice=initialPrice)
        # newListing.save()

        print("!!!!!!!!!")
        print(user)
        print(category)
        print("!!!!!!!!!")

        return render(request, "auctions/create_listing.html", {"categories": Categories.objects.all()})

    else:
        return render(request, "auctions/create_listing.html", {"categories": Categories.objects.all()})
