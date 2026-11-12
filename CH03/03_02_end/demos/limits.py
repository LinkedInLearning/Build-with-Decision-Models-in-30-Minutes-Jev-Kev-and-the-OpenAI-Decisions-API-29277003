"""Lesson 3.1: recognize tasks a decision model can't handle.

The refund policy: a faulty product can be refunded within 30 days of delivery.

Part 1 asks Jev to judge the 30-day window on its own.
Part 2 moves the date math into code and keeps Jev for the judgment call.
"""

from datetime import date

from dotenv import load_dotenv
from typesafe_sdk import TypeSafeClient

load_dotenv()

jev = TypeSafeClient(model="jev-latest")

REFUND_WINDOW_DAYS = 30

REFUND_REQUESTS = [
    {
        "message": "The headphones stopped charging. I want a refund.",
        "delivered_on": "2026-10-15",
        "requested_on": "2026-10-20",
    },
    {
        "message": "The zipper broke on the second use. Please refund me.",
        "delivered_on": "2026-09-21",
        "requested_on": "2026-10-20",
    },
    {
        "message": "I changed my mind about the color. Can I return it?",
        "delivered_on": "2026-10-01",
        "requested_on": "2026-10-20",
    },
    {
        "message": "The blender leaks from the base. I want a refund.",
        "delivered_on": "2026-09-19",
        "requested_on": "2026-10-20",
    },
    {
        "message": "The speaker won't turn on anymore. Refund, please.",
        "delivered_on": "2026-08-28",
        "requested_on": "2026-10-05",
    },
    {
        "message": "The kettle works, but I found a cheaper one. Refund?",
        "delivered_on": "2026-07-30",
        "requested_on": "2026-09-29",
    },
]

WINDOW_QUESTION = {
    "type": "noul",
    "instructions": "Is requested_on within 30 days after delivered_on?",
}

FAULTY_QUESTION = {
    "type": "noul",
    "instructions": "Does the customer say the product is broken or faulty?",
}


def ask_jev_about_window(request):
    response = jev.system_one(
        state={
            "delivered_on": request["delivered_on"],
            "requested_on": request["requested_on"],
        },
        questions={"inside_window": WINDOW_QUESTION},
    )
    return response.answers["inside_window"].noul


def ask_jev_about_fault(request):
    response = jev.system_one(
        state={"message": request["message"]},
        questions={"faulty": FAULTY_QUESTION},
    )
    return response.answers["faulty"].noul


def days_between(start, end):
    return (date.fromisoformat(end) - date.fromisoformat(start)).days


def window_label(is_inside):
    if is_inside:
        return "inside"
    return "outside"


print("Part 1: Jev judges the 30-day window on its own")
for request in REFUND_REQUESTS:
    days = days_between(request["delivered_on"], request["requested_on"])
    code_says = window_label(days <= REFUND_WINDOW_DAYS)

    probability = ask_jev_about_window(request)
    jev_says = window_label(probability >= 0.5)

    print(f"{days} days: code {code_says}, Jev {jev_says} ({probability:.2f})")
    if jev_says != code_says:
        print("  Jev got this one wrong.")

print()
print("Part 2: code does the date math, Jev makes the judgment call")
for request in REFUND_REQUESTS:
    days = days_between(request["delivered_on"], request["requested_on"])
    inside_window = days <= REFUND_WINDOW_DAYS

    faulty = ask_jev_about_fault(request)

    if inside_window and faulty >= 0.7:
        outcome = "refund"
    elif inside_window:
        outcome = "no refund, not reported as faulty"
    else:
        outcome = "no refund, outside the window"
    print(f"{days} days, faulty {faulty:.2f}: {outcome}")
