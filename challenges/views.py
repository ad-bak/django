from re import S
from django.shortcuts import render
from django.http import (
    HttpResponseNotFound,
    HttpResponseRedirect,
    Http404,
)
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "Don't eat meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Exercise for at least 30 minutes every day!",
    "may": "Read for at least 30 minutes every day!",
    "june": "Sleep for at least 8 hours every day!",
    "july": "Run for at least 20 minutes every day!",
    "august": "Speak to a friend every day!",
    "september": "Learn Python for at least 30 minutes every day!",
    "october": "Learn JavaScript for at least 30 minutes every day!",
    "november": "Ride a bike for at least 30 minutes every day!",
    "december": None,
}


def index(request):
    months = list(monthly_challenges.keys())
    return render(
        request,
        "challenges/index.html",
        {"months": months},
    )


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(
            request,
            "challenges/challenge.html",
            {
                "text": challenge_text,
                "month_name": month.capitalize(),
            },
        )
    except:
        raise Http404()
