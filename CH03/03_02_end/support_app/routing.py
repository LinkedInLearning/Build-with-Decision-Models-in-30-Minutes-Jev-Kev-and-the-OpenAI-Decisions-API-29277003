"""Decision 4: which model tier should handle this ticket?"""

from dotenv import load_dotenv
from typesafe_sdk import TypeSafeClient

load_dotenv()

jev = TypeSafeClient(model="jev-latest")

MODEL_TIERS = {
    "fast": "One clear question or problem with an obvious next step.",
    "reasoning": "Several problems at once, or details that conflict.",
}

TIER_QUESTION = {
    "type": "choice",
    "instructions": "Which model tier should handle this support ticket?",
    "criteria": MODEL_TIERS,
}


def pick_model_tier(ticket_text):
    response = jev.system_one(
        state={"ticket": ticket_text},
        questions={"tier": TIER_QUESTION},
    )
    answer = response.answers["tier"]
    return answer.choice, answer.confidence
