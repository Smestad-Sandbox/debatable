import argparse
from debatable.debate import Debate

# Define the command-line interface
parser = argparse.ArgumentParser(description='CLI to work with Debatable Library')
parser.add_argument('first_debater', help='Requires a hosted api, see example: https://replit.com/@haleysmestad/KlutzyFumblingActiveserverpages')
parser.add_argument('second_debater', help='Requires a hosted api, see example: https://replit.com/@haleysmestad/KlutzyFumblingActiveserverpages')
parser.add_argument('--topic', help='set topic of debate')

# Parse the command-line arguments
args = parser.parse_args()

# Implement the functionality

topic = args.topic or ''
current_debate = Debate(args.first_debater, args.second_debater, topic)
current_debate.run_debate()

def cli():
    pass
