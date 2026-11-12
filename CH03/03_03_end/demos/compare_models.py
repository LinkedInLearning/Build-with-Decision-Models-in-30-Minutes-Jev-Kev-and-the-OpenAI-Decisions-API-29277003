"""Lesson 3.3: send one ticket and one question to three decision models.

The question is the same each time: which team should handle this ticket?
Compare the pick, the confidence, and how long each call takes.
"""

import os
import time

import requests
from dotenv import load_dotenv
from openai import OpenAI
from typesafe_sdk import TypeSafeClient

load_dotenv()

TICKET = "My package never arrived, and I was still charged for it."

INSTRUCTIONS = "Which team should handle this support ticket?"

TEAMS = {
    "billing": "Payments, charges, invoices, and refunds.",
    "technical": "Bugs, errors, and problems using the product.",
    "shipping": "Delivery and tracking of orders.",
    "other": "Anything that does not fit the teams above.",
}

KEV_URL = "https://openrouter.ai/api/alpha/decisions"


def ask_openai():
    client = OpenAI()

    # OpenAI takes the options as a list. Jev and Kev take a dictionary.
    choices = []
    for name, description in TEAMS.items():
        choices.append({"value": name, "description": description})

    decision = client.decisions.create(
        model="gpt-6-luna",
        input=TICKET,
        questions=[
            {
                "type": "choice",
                "name": "team",
                "instructions": INSTRUCTIONS,
                "choices": choices,
            }
        ],
    )
    answer = decision.answers[0]
    return answer.choice, answer.confidence


def ask_jev():
    jev = TypeSafeClient(model="jev-latest")
    response = jev.system_one(
        state={"ticket": TICKET},
        questions={
            "team": {
                "type": "choice",
                "instructions": INSTRUCTIONS,
                "criteria": TEAMS,
            }
        },
    )
    answer = response.answers["team"]
    return answer.choice, answer.confidence


def ask_kev():
    api_key = os.environ["OPENROUTER_API_KEY"]
    response = requests.post(
        KEV_URL,
        headers={"Authorization": "Bearer " + api_key},
        json={
            "model": "jaredpalmer/kev-4b",
            "state": {"ticket": TICKET},
            "questions": {
                "team": {
                    "type": "choice",
                    "instructions": INSTRUCTIONS,
                    "criteria": TEAMS,
                }
            },
        },
    )
    response.raise_for_status()
    answer = response.json()["answers"]["team"]
    return answer["choice"], answer["confidence"]


def time_one_model(model_name, ask_function):
    # ask_function is one of the three functions above.
    start = time.perf_counter()
    team, confidence = ask_function()
    seconds = time.perf_counter() - start

    print()
    print(f"{model_name}: {team}")
    print(f"  confidence {confidence:.2f}, took {seconds:.2f} seconds")


print(TICKET)
time_one_model("OpenAI Decisions API", ask_openai)
time_one_model("Jev", ask_jev)
time_one_model("Kev 4B", ask_kev)
