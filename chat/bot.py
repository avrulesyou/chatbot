"""
Chat bot module for the terminal client.
Uses ChatterBot's SQLStorageAdapter, which stores conversation statements in SQLite
by default. SQLite requires no separate database server, keeps the project portable,
and is sufficient for this assignment's conversation storage.
"""
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Car dealer Q&A: greetings, inventory, pricing, financing, test drives, closing
DEFAULT_CONVERSATIONS = [
    "Hello", "Hi! Welcome to the dealership. How can I help you find your next car?",
    "Good morning!", "Good morning! Are you here to look at new or used vehicles?",
    "Good afternoon", "Good afternoon! What kind of car are you interested in?",
    "Hi there", "Hello! Ready to find a great deal today?",
    "How are you?", "I'm doing great, thanks! Here to help you drive away in the right car.",
    "I'm looking for a car", "Great! Are you interested in new or pre-owned? Any make or budget in mind?",
    "Do you have SUVs?", "Yes. We have several SUVs in stock. Do you need three rows or two?",
    "What cars do you have?", "We have new and used sedans, SUVs, and trucks. What type are you looking for?",
    "Do you have any Hondas?", "We do. I can show you our Honda inventory. New or used?",
    "What's the price?", "Prices vary by model and trim. Which vehicle are you asking about?",
    "How much is that one?", "I’d be happy to get the exact price and any current offers. Which model?",
    "Is there a discount?", "We often have manufacturer and dealer offers. I can check what’s available for you.",
    "Can I get a test drive?", "Absolutely. When would you like to schedule a test drive?",
    "I want to test drive", "Sure. Tell me the model you’re interested in and we’ll set it up.",
    "Do you offer financing?", "Yes. We work with several lenders and can find a payment that fits your budget.",
    "What are the financing options?", "We have loans and lease options. What’s your target monthly payment?",
    "What's the interest rate?", "Rates depend on credit and term. I can have our finance team give you a quote.",
    "I have a trade-in", "We take trade-ins. What year, make, and model? I can get an estimated value.",
    "How much for my trade?", "Share the year, make, model, and condition and we’ll get you a fair estimate.",
    "I'm ready to buy", "Excellent. I’ll walk you through the paperwork and we’ll get you into your new car.",
    "Let's close the deal", "Great. We’ll go over numbers, incentives, and final paperwork.",
    "When can I pick it up?", "Once we finish paperwork and funding, we can schedule pickup or delivery.",
    "Thanks", "You’re welcome. Anything else before you head out?",
    "Thank you", "My pleasure. We’re here if you need anything else.",
    "Bye", "Thanks for visiting. We look forward to seeing you again!",
    "Goodbye", "Goodbye! Drive safe.",
]


def create_bot(name="Car Dealer Bot", storage_adapter="chatterbot.storage.SQLStorageAdapter", database_uri=None):
    """Create a ChatBot instance. SQLStorageAdapter uses SQLite by default (database_uri)."""
    kwargs = {"storage_adapter": storage_adapter}
    if database_uri:
        kwargs["database_uri"] = database_uri
    return ChatBot(name, **kwargs)


def train_bot(chatbot, conversations=None):
    """Train the bot with a list of input/response pairs (alternating strings)."""
    trainer = ListTrainer(chatbot)
    trainer.train(conversations or DEFAULT_CONVERSATIONS)


def get_response(chatbot, text):
    """Return the bot's response for the given user text."""
    return chatbot.get_response(text)
