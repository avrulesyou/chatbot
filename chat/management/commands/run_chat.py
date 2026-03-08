import sys
from django.core.management.base import BaseCommand
from chat.bot import create_bot, train_bot, get_response


class Command(BaseCommand):
    help = "Run terminal chat with the bot."

    def add_arguments(self, parser):
        parser.add_argument("--no-train", action="store_true", help="Skip default training.")

    def handle(self, *args, **options):
        bot = create_bot()
        if not options["no_train"]:
            train_bot(bot)
        self.stdout.write("Terminal chat started. Type 'quit' or 'exit' to stop.\n")
        while True:
            try:
                user_input = input("user: ").strip()
            except (EOFError, KeyboardInterrupt):
                break
            if not user_input:
                continue
            if user_input.lower() in ("quit", "exit", "bye"):
                self.stdout.write("Goodbye.\n")
                break
            response = get_response(bot, user_input)
            self.stdout.write(f"bot: {response}\n")
