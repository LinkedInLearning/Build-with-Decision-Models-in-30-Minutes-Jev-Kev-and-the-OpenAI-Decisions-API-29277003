"""Run every sample ticket through the support app.

An AI agent already handled these tickets. For each one, it drafted a reply.
For some, it also proposed a refund. Nothing has been sent or refunded yet.

The app makes four judgment calls first. You build one in each lesson of
chapter 2, then add the step that acts on the answer here.
"""

import json

from refund_gate import check_refund
from triage import pick_team

# A refund is hard to undo, so flag anything the model is not sure is safe.
RISK_THRESHOLD = 0.3

# "shadow" warns and lets the refund through. "enforce" blocks it.
REFUND_MODE = "enforce"

with open("data/tickets.json") as file:
    tickets = json.load(file)

for ticket in tickets:
    message = ticket["customer_message"]
    print()
    print(f"{ticket['id']}: {message}")

    # Step 1: pick the team that should handle the ticket.
    team, confidence = pick_team(message)
    print(f"  Team:   {team} (confidence {confidence:.2f})")

    # Step 2: check the agent's refund before it goes through.
    if ticket["proposed_action"] is not None:
        risk = check_refund(ticket)
        if risk < RISK_THRESHOLD:
            print(f"  Refund: allowed (risk {risk:.2f})")
        elif REFUND_MODE == "shadow":
            print(f"  Refund: allowed with a warning (risk {risk:.2f})")
        else:
            print(f"  Refund: blocked (risk {risk:.2f})")

    # Step 3: grade the agent's draft reply before it is sent.

    # Step 4: pick the model tier that should handle the ticket.
