"""Lesson 1.1: make your first call to a decision model.

Ask the OpenAI Decisions API one yes-or-no question about a support ticket.
"""

import json

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

with open("data/tickets.json") as file:
    tickets = json.load(file)

ticket = tickets[0]
print(ticket["customer_message"])

decision = client.decisions.create(
    model="gpt-6-luna",
    input=ticket["customer_message"],
    questions=[
        {
            "type": "predicate",
            "name": "asks_for_refund",
            "instructions": "Does the customer ask for a refund?",
        }
    ],
)

# A predicate answer is the probability that the answer is yes, from 0 to 1.
answer = decision.answers[0]
print(f"Probability the customer asks for a refund: {answer.probability:.2f}")

# The model gives you a number. Your code decides what to do with it.
if answer.probability >= 0.5:
    print("Send this ticket to the refunds queue.")
else:
    print("Leave this ticket in the general queue.")
