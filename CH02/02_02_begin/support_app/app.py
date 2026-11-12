"""Run every sample ticket through the support app.

An AI agent already handled these tickets. For each one, it drafted a reply.
For some, it also proposed a refund. Nothing has been sent or refunded yet.

The app makes four judgment calls first. You build one in each lesson of
chapter 2, then add the step that acts on the answer here.
"""

import json

from triage import pick_team

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

    # Step 3: grade the agent's draft reply before it is sent.

    # Step 4: pick the model tier that should handle the ticket.
