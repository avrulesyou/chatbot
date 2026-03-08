# Hands-On Assignment 3: Simple Q&A Chatbot with Python

> Terminal chatbot for car dealer sales assistance — built with Django, Python, and ChatterBot.

**Student:** Abhishek Vishwakarma  
**Course:** 2026 Spring – Advance Artificial Intelligence (MSCS-633-M50) – Full Term  
**Assignment:** Hands-On Assignment 3 – Create a Simple Q&A Chatbot with Python

---

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Commands Reference](#commands-reference)
- [Test Results](#test-results)
- [Example Conversation](#example-conversation)
- [Project Structure](#project-structure)
- [Technical Details](#technical-details)
- [Deliverables & Submission](#deliverables--submission)

---

## Overview

This project implements a **terminal chat client** that uses **Django**, **Python**, and **ChatterBot** to simulate a car dealer assistant. ChatterBot is a machine-learning-based conversational engine that responds from collections of known conversations. The bot supports greetings, inventory, pricing, financing, test drives, trade-ins, and closing deals.

---

## Prerequisites

- **Python** 3.10+
- **pip** (Python package manager)

---

## Quick Start

```bash
# 1. Clone the repository
git clone <(https://github.com/avrulesyou/chatbot)>
cd "python chatbot"

# 2. Create and activate a virtual environment (recommended)
python -m venv venv
source venv/bin/activate          # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
python -m spacy download en_core_web_sm

# 4. Run the chatbot
python manage.py run_chat
```

Type `quit`, `exit`, or `bye` to stop the chat.

---

## Commands Reference

| Command | Description |
|---------|-------------|
| `pip install -r requirements.txt` | Install Python dependencies (Django, ChatterBot, spacy) |
| `python -m spacy download en_core_web_sm` | Download spaCy language model (required for ChatterBot) |
| `python manage.py run_chat` | Start the terminal chat (trains bot on first run) |
| `python manage.py run_chat --no-train` | Start chat without training (uses existing DB / may give generic replies) |
| `python manage.py test chat` | Run all tests (default verbosity) |
| `python manage.py test chat -v 2` | Run tests with verbose output (shows sample I/O) |

### Full setup sequence

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python manage.py run_chat
```

### Run tests

```bash
python manage.py test chat
```

### Verbose test output (shows input/output per test)

```bash
python manage.py test chat -v 2
```

---

## Test Results

All **15 tests** pass. Summary:

```
----------------------------------------------------------------------
Ran 15 tests in ~5s

OK
----------------------------------------------------------------------
```

### Test Coverage

| Test Class | Tests | Purpose |
|------------|-------|---------|
| `BotResponseTests` | 9 | Greeting, inventory, ready-to-buy, close deal, full deal flow, financing, trade-in, pickup |
| `TerminalClientTests` | 4 | Car deal flow in terminal, quit/exit/bye, empty input handling |
| `BotCreationTests` | 2 | Default and custom bot name creation |

### Sample test output (verbose)

<details>
<summary>Click to expand sample <code>python manage.py test chat -v 2</code> output</summary>

```
test_close_the_deal ... ok
test_create_bot_custom_name ... ok
test_create_bot_default_name ... ok
test_financing_inquiry ... ok
test_full_deal_flow ... ok
test_greeting_at_dealership ... ok
test_inventory_inquiry ... ok
test_looking_for_car ... ok
test_pickup_timing ... ok
test_ready_to_buy ... ok
test_terminal_car_deal_flow ... ok
test_trade_in_inquiry ... ok
...
----------------------------------------------------------------------
Ran 15 tests in ~5s

OK
----------------------------------------------------------------------
```

</details>

---

## Example Conversation

```
user: Good morning! How are you doing?
bot: Good morning! Are you here to look at new or used vehicles?

user: I'm looking for a car
bot: Great! Are you interested in new or pre-owned? Any make or budget in mind?

user: Do you have SUVs?
bot: Yes. We have several SUVs in stock. Do you need three rows or two?

user: I'm ready to buy
bot: Excellent. I'll walk you through the paperwork and we'll get you into your new car.

user: Thanks
bot: You're welcome. Anything else before you head out?
```

---

## Project Structure

```
python chatbot/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── MANIFEST.in               # Manifest for source distribution
├── README.md                 # This file
├── chatbot_project/          # Django project
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── chat/                     # Chat app
    ├── bot.py                # Bot creation, training, response logic
    ├── tests.py              # Unit and integration tests
    ├── apps.py
    └── management/commands/
        └── run_chat.py       # Terminal chat command
```

---

## Technical Details

### Tech Stack

- **Django** – Project structure and `run_chat` management command  
- **ChatterBot** – ML-based conversational engine  
- **spaCy** – NLP (en_core_web_sm) for ChatterBot  
- **SQLite** – Storage adapter used by ChatterBot

### Why SQLite?

ChatterBot uses **SQLStorageAdapter**, which defaults to SQLite:

- No separate database server
- Portable, easy setup
- Suited to this assignment’s conversation storage

---

## Deliverables & Submission

- [ ] **Python source code** – This repository  
- [ ] **MANIFEST.in** – Included in the repo  
- [ ] **Screenshot** – Add to the Word document (terminal chat Q&A)  
- [ ] **GitHub repository URL** – Add to the Word document  
- [ ] Code follows course coding standards and includes comments

---

**Author:** Abhishek Vishwakarma  
**Term:** 2026 Spring – Advance Artificial Intelligence (MSCS-633-M50)
