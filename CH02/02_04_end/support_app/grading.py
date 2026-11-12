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

QUALITY_QUESTION = {
    "type": "score",
    "name": "reply_quality",
    "instructions": "How good is the draft reply to the customer message?",
    "levels": RUBRIC,
}


def grade_reply(customer_message, draft_reply):
    text_to_grade = (
        f"Customer message:\n{customer_message}\n\n"
        f"Draft reply:\n{draft_reply}"
    )
    decision = client.decisions.create(
        model="gpt-6-luna",
        input=text_to_grade,
        questions=[QUALITY_QUESTION],
    )
    # The score is a weighted average, so it can land between levels.
    return decision.answers[0].score
