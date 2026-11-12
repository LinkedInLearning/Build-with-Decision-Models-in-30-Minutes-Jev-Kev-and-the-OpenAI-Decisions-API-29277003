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

decision = client.decisions.create(
    model="gpt-6-luna",
    input=ticket["customer_message"],
    questions=[
        {
            "type": "predicate",
            "name": "is_urgent",
            "instructions": "Does the customer need help within a day?",
        },
        {
            "type": "choice",
            "name": "team",
            "instructions": "Which team should handle this ticket?",
            "choices": TEAMS,
        },
        {
            "type": "score",
            "name": "severity",
            "instructions": "How severe is the problem for the customer?",
            "levels": SEVERITY_LEVELS,
        },
    ],
)

for answer in decision.answers:
    print()
    print(f"Question: {answer.name}")

    if answer.type == "predicate":
        # One number: the probability that the answer is yes.
        print(f"  Probability of yes: {answer.probability:.2f}")

    elif answer.type == "choice":
        # The pick, how sure the model is, and the odds for every option.
        print(f"  Choice: {answer.choice}")
        print(f"  Confidence: {answer.confidence:.2f}")
        for option in answer.probabilities:
            print(f"    {option.value}: {option.probability:.2f}")

    elif answer.type == "score":
        # The score is a weighted average, so it can land between levels.
        print(f"  Score: {answer.score:.2f}")
        print(f"  Confidence: {answer.confidence:.2f}")
        for level in answer.probabilities:
            print(f"    {level.value} {level.label}: {level.probability:.2f}")

    elif answer.type == "refusal":
        print("  The model declined to answer this question.")
