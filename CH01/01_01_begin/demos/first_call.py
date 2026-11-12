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

# TODO: ask the Decisions API whether the customer asks for a refund.

# TODO: read the answer and decide what to do with it.
