"""Lesson 1.2: read decision model answers and confidence scores.

Ask three questions about one ticket in a single request:
a yes-or-no question, a pick-one question, and a rating.
"""

import json

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

with open("data/tickets.json") as file:
    tickets = json.load(file)

ticket = tickets[1]
print(ticket["customer_message"])

TEAMS = [
    {"value": "billing", "description": "Payments, charges, and refunds."},
    {"value": "technical", "description": "Bugs and errors in the product."},
    {"value": "shipping", "description": "Delivery and tracking of orders."},
    {"value": "other", "description": "Anything that does not fit above."},
]

# Levels run from least to most severe. The API numbers them 0, 1, and 2.
SEVERITY_LEVELS = [
    {
        "label": "Minor",
        "description": "Annoying, but nothing is blocked.",
    },
    {
        "label": "Workaround",
        "description": "A task fails, but another way works.",
    },
    {
        "label": "Blocked",
        "description": "A task fails and there is no other way.",
    },
]

# TODO: ask three questions in one request: is_urgent, team, and severity.

# TODO: loop over the answers and print what each type gives you.
