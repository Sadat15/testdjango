from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def monthly_challenge(request, month):
    challenge_text = None

    if month == "january":
        challenge_text = "January"
    elif month == "february":
        challenge_text = "February"
    elif month == "march":
        challenge_text = "March"
    elif month == "april":
        challenge_text = "April"
    elif month == "may":
        challenge_text = "May"
    elif month == "june":
        challenge_text = "June"
    elif month == "july":
        challenge_text = "July"
    elif month == "august":
        challenge_text = "August"
    elif month == "september":
        challenge_text = "September"
    elif month == "october":
        challenge_text = "October"
    elif month == "november":
        challenge_text = "November"
    elif month == "december":
        challenge_text = "December"
    else:
        return HttpResponseNotFound("This page has not been found")

    return HttpResponse(challenge_text)
