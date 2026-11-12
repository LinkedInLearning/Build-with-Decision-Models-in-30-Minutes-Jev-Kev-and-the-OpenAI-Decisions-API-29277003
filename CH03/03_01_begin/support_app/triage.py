"""Decision 1: which team should handle this ticket?"""

from dotenv import load_dotenv
from typesafe_sdk import TypeSafeClient

load_dotenv()

jev = TypeSafeClient(model="jev-latest")

# Each team gets a plain-English description. Jev calls these criteria.
TEAMS = {
    "billing": "Payments, charges, invoices, and refunds.",
    "technical": "Bugs, errors, and problems using the product.",
    "shipping": "Delivery and tracking of orders.",
    "other": "Anything that does not fit the teams above.",
}

TEAM_QUESTION = {
    "type": "choice",
    "instructions": "Which team should handle this support ticket?",
    "criteria": TEAMS,
}


def pick_team(ticket_text):
    response = jev.system_one(
        state={"ticket": ticket_text},
        questions={"team": TEAM_QUESTION},
    )
    answer = response.answers["team"]
    return answer.choice, answer.confidence
