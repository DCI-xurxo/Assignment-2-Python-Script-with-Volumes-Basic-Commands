import datetime, random

quotes = [
    "Keep going — small progress is still progress.",
    "You are capable of amazing things.",
    "Every day is a new opportunity."
]

with open("/app/logs/log.txt", "a") as f:
    f.write(f"Date/Time: {datetime.datetime.now()}\n")
    f.write(f"Quote: {random.choice(quotes)}\n")
    f.write("Container execution completed\n")
    f.write("-" * 40 + "\n")