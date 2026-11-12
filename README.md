# Build with Decision Models in 30 Minutes: Jev, Kev, and the OpenAI Decisions API
This is the repository for the LinkedIn Learning course `Build with Decision Models in 30 Minutes: Jev, Kev, and the OpenAI Decisions API`. The full course is available from [LinkedIn Learning][lil-course-url].

![lil-thumbnail-url]

## Course Description

Every AI application makes judgment calls, like which team gets a support ticket or whether an agent should issue a refund. Decision models such as Jev, Kev, and the OpenAI Decisions API answer those questions with a yes or no, a pick from your options, or a score, along with a confidence level your code can act on. In this course, learn how to put decision models to work by building a support application one judgment call at a time. Explore how to sort tickets, approve agent actions, grade replies, and route requests to the right model. Find out which tasks decision models can't handle and how to catch confident wrong answers before they reach production. By the end, you'll be ready to choose the right decision model for your own AI applications.

## What You Build

An AI agent has already handled eight support tickets. For each one, it drafted a reply. For some, it also proposed a refund. Nothing has been sent or refunded yet. The app makes four judgment calls first.

| Step | Judgment call | File | Model |
|---|---|---|---|
| 1 | Which team should handle the ticket? | `support_app/triage.py` | Jev |
| 2 | Is the agent's refund risky? | `support_app/refund_gate.py` | Jev |
| 3 | Is the draft reply good enough to send? | `support_app/grading.py` | OpenAI Decisions API |
| 4 | Which model tier should handle the ticket? | `support_app/routing.py` | Jev |

Each file holds one question and one function. `support_app/app.py` calls the functions and acts on the answers.

Kev, the open model, comes in during chapter 3. You test it against Jev on 30 labeled tickets in `support_app/check_accuracy.py`, then compare all three models on one ticket in `demos/compare_models.py`.

## Instructions
This repository has a folder for each chapter, and each chapter folder has folders for the videos in that chapter. The naming convention is `CHAPTER#_MOVIE#`. As an example, the folder `CH02/02_03_begin` corresponds to the second chapter and the third video in that chapter.

Most videos have a beginning and an end state. A folder that ends in `_begin` contains the code as it is at the beginning of the movie. A folder that ends in `_end` contains the code as it is at the end of the movie. If you get stuck, compare your work to the `_end` folder.

Each folder is a complete copy of the project, so it runs on its own.

| Video | File you work in | Folders |
|---|---|---|
| 1.1 Make your first call to a decision model | `demos/first_call.py` | `CH01/01_01_begin`, `CH01/01_01_end` |
| 1.2 Read decision model answers and confidence scores | `demos/read_answers.py` | `CH01/01_02_begin`, `CH01/01_02_end` |
| 2.1 Sort support tickets with a choice question | `support_app/triage.py` | `CH02/02_01_begin`, `CH02/02_01_end` |
| 2.2 Gate an agent action with a predicate | `support_app/refund_gate.py` | `CH02/02_02_begin`, `CH02/02_02_end` |
| 2.3 Grade an AI response against a rubric | `support_app/grading.py` | `CH02/02_03_begin`, `CH02/02_03_end` |
| 2.4 Route each request to the right model | `support_app/routing.py` | `CH02/02_04_begin`, `CH02/02_04_end` |
| 3.1 Recognize tasks a decision model can't handle | `demos/limits.py` | `CH03/03_01_begin`, `CH03/03_01_end` |
| 3.2 Catch confident wrong answers before production | `support_app/check_accuracy.py` | `CH03/03_02_begin`, `CH03/03_02_end` |
| 3.3 Choose between Jev, Kev, and the Decisions API | `demos/compare_models.py` | `CH03/03_03_end` |

Lesson 3.3 is a text article with one script to run, so it has a single folder with the finished code.

## Installing
1. To use these exercise files, you must have the following:
	- A GitHub account, to run the files in GitHub Codespaces. To work on your own machine instead, you need Python 3.10 or later.
	- An OpenAI API key, for the OpenAI Decisions API (needed from chapter 1). Get one at platform.openai.com.
	- A TypeSafe API key, for Jev (needed from chapter 2). Get one at console.typesafe.ai.
	- An OpenRouter API key, for the hosted Kev model (needed in chapter 3). Get one at openrouter.ai/settings/keys.
2. Open this repository in GitHub Codespaces. The dev container sets up Python 3.12 and installs the packages for you. If you clone the repository to your own machine instead, run `pip install -r requirements.txt`.
3. Add your API keys. You can store them in either place below. The code checks both, and a Codespaces secret wins if a key is in both.

	**Codespaces secrets.** In your GitHub settings, open Codespaces and add a secret for each key: `OPENAI_API_KEY`, `TYPESAFE_API_KEY`, and `OPENROUTER_API_KEY`. Give the secrets access to this repository. A Codespace that is already running won't see a new secret until you stop it and start it again.

	**A `.env` file.** Copy `.env.example` to a new file named `.env` at the top of the repository and add your keys there. Every lesson folder finds it. Keep `.env` out of version control. The `.gitignore` file already skips it.

## Running the Code

Move into the lesson's folder first, then run the script from there, because the scripts read the sample data from that folder's `data/`.

```
cd CH01/01_01_begin
python demos/first_call.py
```

## Sample Data

Every lesson folder has the same two data files.

- `data/tickets.json` holds the eight tickets the app runs. Each ticket has the customer's message, the refund the agent proposed (if any), and the reply the agent drafted.
- `data/labeled_tickets.csv` holds 30 tickets with the correct team already filled in by a person. Lesson 3.2 uses it to test the triage question.

## What It Costs

Every request in this course is small, and all three services bill by input tokens. Two things to know:

- Lesson 3.2 sends 30 requests to Jev and 30 to Kev each time you run it.
- OpenRouter is prepaid, so add a small amount of credit to your account before chapter 3.

Prices change, so check each provider's pricing page.

## Instructor

Kesha Williams

Founder and Head of AI at Keysoft, AWS AI Hero, and AI educator

Check out my other courses on [LinkedIn Learning](https://www.linkedin.com/learning/instructors/kesha-williams).


[0]: # (Replace these placeholder URLs with actual course URLs)

[lil-course-url]: https://www.linkedin.com/learning/
[lil-thumbnail-url]: https://media.licdn.com/dms/image/v2/D4E0DAQG0eDHsyOSqTA/learning-public-crop_675_1200/B4EZVdqqdwHUAY-/0/1741033220778?e=2147483647&v=beta&t=FxUDo6FA8W8CiFROwqfZKL_mzQhYx9loYLfjN-LNjgA