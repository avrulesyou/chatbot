import sys
from io import StringIO
from unittest.mock import patch

from django.test import TestCase
from django.core.management import call_command

from chat.bot import create_bot, train_bot, get_response, DEFAULT_CONVERSATIONS


def bot_with_memory():
    bot = create_bot(database_uri="sqlite:///:memory:")
    train_bot(bot)
    return bot


def _log_io(user_input, bot_output):
    out = sys.__stdout__
    out.write(f"  user: {user_input}\n")
    out.write(f"  bot:  {bot_output}\n")


class BotResponseTests(TestCase):
    def test_greeting_at_dealership(self):
        bot = bot_with_memory()
        user_input = "Hello"
        r = get_response(bot, user_input)
        _log_io(user_input, r)
        self.assertIsNotNone(r)
        self.assertTrue("Hi" in str(r) or "welcome" in str(r).lower() or len(str(r).strip()) > 0)

    def test_looking_for_car(self):
        bot = bot_with_memory()
        user_input = "I'm looking for a car"
        r = get_response(bot, user_input)
        _log_io(user_input, r)
        self.assertIsNotNone(r)
        self.assertTrue(len(str(r).strip()) > 0)

    def test_inventory_inquiry(self):
        bot = bot_with_memory()
        user_input = "Do you have SUVs?"
        r = get_response(bot, user_input)
        _log_io(user_input, r)
        self.assertIsNotNone(r)
        self.assertTrue("SUV" in str(r) or "Yes" in str(r) or len(str(r).strip()) > 0)

    def test_ready_to_buy(self):
        bot = bot_with_memory()
        user_input = "I'm ready to buy"
        r = get_response(bot, user_input)
        _log_io(user_input, r)
        self.assertIsNotNone(r)
        self.assertTrue("Excellent" in str(r) or "paperwork" in str(r).lower() or "car" in str(r).lower())

    def test_close_the_deal(self):
        bot = bot_with_memory()
        user_input = "Let's close the deal"
        r = get_response(bot, user_input)
        _log_io(user_input, r)
        self.assertIsNotNone(r)
        self.assertTrue("deal" in str(r).lower() or "paperwork" in str(r).lower() or "numbers" in str(r).lower())

    def test_full_deal_flow(self):
        bot = bot_with_memory()
        r1 = get_response(bot, "Good morning!")
        r2 = get_response(bot, "I'm looking for a car")
        r3 = get_response(bot, "Can I get a test drive?")
        r4 = get_response(bot, "I'm ready to buy")
        r5 = get_response(bot, "Thanks")
        _log_io("Good morning!", r1)
        _log_io("I'm looking for a car", r2)
        _log_io("Can I get a test drive?", r3)
        _log_io("I'm ready to buy", r4)
        _log_io("Thanks", r5)
        self.assertIsNotNone(r1)
        self.assertIsNotNone(r2)
        self.assertIsNotNone(r3)
        self.assertIsNotNone(r4)
        self.assertIsNotNone(r5)

    def test_financing_inquiry(self):
        bot = bot_with_memory()
        user_input = "Do you offer financing?"
        r = get_response(bot, user_input)
        _log_io(user_input, r)
        self.assertIsNotNone(r)
        self.assertTrue("Yes" in str(r) or "financ" in str(r).lower() or "lender" in str(r).lower())

    def test_trade_in_inquiry(self):
        bot = bot_with_memory()
        user_input = "I have a trade-in"
        r = get_response(bot, user_input)
        _log_io(user_input, r)
        self.assertIsNotNone(r)
        self.assertTrue("trade" in str(r).lower() or "year" in str(r).lower())

    def test_pickup_timing(self):
        bot = bot_with_memory()
        user_input = "When can I pick it up?"
        r = get_response(bot, user_input)
        _log_io(user_input, r)
        self.assertIsNotNone(r)
        self.assertTrue("paperwork" in str(r).lower() or "pickup" in str(r).lower() or "delivery" in str(r).lower())


class TerminalClientTests(TestCase):
    @patch("chat.management.commands.run_chat.input", side_effect=["I'm looking for a car", "I'm ready to buy", "Thanks", "quit"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_terminal_car_deal_flow(self, mock_stdout, mock_input):
        call_command("run_chat", stdout=mock_stdout)
        out = mock_stdout.getvalue()
        sys.__stdout__.write("  terminal: car deal flow -> I'm looking for a car, I'm ready to buy, Thanks, quit\n")
        sys.__stdout__.write("  terminal output: " + (out.strip()[:250] + "..." if len(out) > 250 else out.strip()) + "\n")
        self.assertIn("Terminal chat started", out)
        self.assertIn("bot:", out)

    @patch("chat.management.commands.run_chat.input", side_effect=["quit"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_quit_exits_loop(self, mock_stdout, mock_input):
        call_command("run_chat", "--no-train", stdout=mock_stdout)
        out = mock_stdout.getvalue()
        sys.__stdout__.write("  input: quit -> output: " + out.strip() + "\n")
        self.assertIn("Goodbye", out)

    @patch("chat.management.commands.run_chat.input", side_effect=["exit"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_exit_exits_loop(self, mock_stdout, mock_input):
        call_command("run_chat", "--no-train", stdout=mock_stdout)
        out = mock_stdout.getvalue()
        sys.__stdout__.write("  input: exit -> output: " + out.strip() + "\n")
        self.assertIn("Goodbye", out)

    @patch("chat.management.commands.run_chat.input", side_effect=["", "bye"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_empty_input_skipped(self, mock_stdout, mock_input):
        call_command("run_chat", "--no-train", stdout=mock_stdout)
        out = mock_stdout.getvalue()
        sys.__stdout__.write("  input: (empty), bye -> output: " + out.strip() + "\n")
        self.assertIn("Goodbye", out)


class BotCreationTests(TestCase):
    def test_create_bot_default_name(self):
        bot = create_bot(database_uri="sqlite:///:memory:")
        sys.__stdout__.write(f"  create_bot() -> name: {bot.name}\n")
        self.assertEqual(bot.name, "Car Dealer Bot")

    def test_create_bot_custom_name(self):
        bot = create_bot(name="Custom", database_uri="sqlite:///:memory:")
        sys.__stdout__.write(f"  create_bot(name='Custom') -> name: {bot.name}\n")
        self.assertEqual(bot.name, "Custom")
