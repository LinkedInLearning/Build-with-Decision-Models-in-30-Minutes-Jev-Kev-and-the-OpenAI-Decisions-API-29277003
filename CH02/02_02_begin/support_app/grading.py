"""Decision 3: is the agent's draft reply good enough to send?"""

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

# Levels run from worst to best. The API numbers them 0, 1, and 2.
RUBRIC = [
    {
        "label": "Not usable",
        "description": (
            "Ignores the customer's problem, is rude, "
            "or promises something the ticket does not support."
        ),
    },
    {
        "label": "Needs work",
        "description": (
            "Addresses only part of the problem, "
            "or leaves out a clear next step."
        ),
    },
    {
        "label": "Ready to send",
        "description": (
            "Addresses the whole problem politely "
            "and gives a clear next step."
        ),
    },
]


def grade_reply(customer_message, draft_reply):
    # TODO (lesson 2.3): ask the Decisions API a score question.
    # Return the score.
    pass
