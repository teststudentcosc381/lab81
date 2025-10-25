from adventure.utils import read_events_from_file
from rich import print
from rich.console import Console
import random

default_message = "hello You stand still, unsure what to do. The forest swallows you."

def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "left":
        return left_path(random_event)
    elif choice == "right":
        return right_path(random_event)
    else:
        return default_message + "black"

def left_path(event):
    return "[red]You walk left. " + event + "[/red]"

def right_path(event):
    return "[blue]You walk right. " + event + "[/blue]"

if __name__ == "__main__":
    console = Console()
    events = read_events_from_file('events.txt')

    print("[italic green]You wake up in a dark forest. You can go left or right.[/italic green]")
    while True:
        choice = console.input("[italic bold yellow]Which direction do you choose?[/italic bold yellow] ([red]left[/red]/[blue]right[/blue]/exit): ")
        choice = choice.strip().lower()
        if choice == 'exit':
            print("bonus good bye")
            break

        print(step(choice, events))