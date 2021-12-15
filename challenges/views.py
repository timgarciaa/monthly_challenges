from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
  "january": "Eat no meat for the entire month!",
  "february": "Walk for at least 20 minutes every day!",
  "march": "Learn Django for at least 20minutes everyday!",
  "april": "april yeah",
  "may": "may ha",
  "june": "just june",
  "july": "July july",
  "august": "going ghost",
  "september": "sept beer",
  "october": "ber ber oct",
  "november": "nov nov",
  "december": "christmas"
}

# Create your views here.

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenge/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
    except:
        return HttpResponseNotFound("This month is not supported!")


    return HttpResponse(challenge_text)