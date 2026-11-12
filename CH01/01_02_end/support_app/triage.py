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


def pick_team(ticket_text):
    # TODO (lesson 2.1): ask Jev a choice question about the ticket.
    # Return the team it picks and how confident it is.
    pass
