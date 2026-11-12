"""Lesson 3.2: catch confident wrong answers before production.

Test the triage question against 30 tickets a person already labeled.
Run it on Jev first, then send the same question to Kev.
"""

import csv
import os

import requests
from dotenv import load_dotenv

from triage import TEAM_QUESTION, pick_team

load_dotenv()

# At or above this confidence, the app would act without a second look.
CONFIDENT = 0.8

# Kev is an open model. This course calls a copy hosted on OpenRouter.
KEV_URL = "https://openrouter.ai/api/alpha/decisions"
KEV_MODEL = "jaredpalmer/kev-4b"

def pick_team_with_kev(ticket_text):
    # Same state and same question as pick_team. Only the model changes.
    api_key = os.environ["OPENROUTER_API_KEY"]
    response = requests.post(
        KEV_URL,
        headers={"Authorization": "Bearer " + api_key},
        json={
            "model": KEV_MODEL,
            "state": {"ticket": ticket_text},
            "questions": {"team": TEAM_QUESTION},
        },
    )
    response.raise_for_status()
    answer = response.json()["answers"]["team"]
    return answer["choice"], answer["confidence"]

def check_accuracy(model_name, pick_team_function):
    # pick_team_function is whichever function you want to test.
    with open("data/labeled_tickets.csv") as file:
        labeled_tickets = list(csv.DictReader(file))

    correct = 0
    confident_misses = []

    for ticket in labeled_tickets:
        team, confidence = pick_team_function(ticket["text"])
        if team == ticket["team"]:
            correct += 1
        elif confidence >= CONFIDENT:
            confident_misses.append((ticket, team, confidence))

    print()
    print(f"{model_name}: {correct} of {len(labeled_tickets)} correct")
    print(f"Confident misses: {len(confident_misses)}")
    for ticket, team, confidence in confident_misses:
        print(f"  {ticket['text']}")
        print(f"    expected {ticket['team']}, got {team} ({confidence:.2f})")


check_accuracy("Jev", pick_team)
check_accuracy("Kev", pick_team_with_kev)
