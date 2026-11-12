"""Decision 4: which model tier should handle this ticket?"""

from dotenv import load_dotenv
from typesafe_sdk import TypeSafeClient

load_dotenv()

jev = TypeSafeClient(model="jev-latest")

MODEL_TIERS = {
    "fast": "One clear question or problem with an obvious next step.",
    "reasoning": "Several problems at once, or details that conflict.",
}


def pick_model_tier(ticket_text):
    # TODO (lesson 2.4): ask Jev a choice question about the ticket.
    # Return the tier it picks and how confident it is.
    pass
