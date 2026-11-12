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


# TODO: write check_accuracy. Run every labeled ticket through a model,
# count the correct answers, and collect the confident wrong ones.

# TODO: check Jev with pick_team, then Kev with pick_team_with_kev.
