from textual.app import App, ComposeResult
from textual.containers import Middle
from textual.widgets import Header, Footer, Label, Static
from textual.reactive import reactive
from textual.widget import Widget
import sys
import random
import os

def flash(filename):
    with open(filename, "r") as f:
        ctx = f.read()
    ctx = ctx.split(";")
    flashcards = []
    for i in ctx:
        flashcards.append((i.split("-")[0].strip(), i.split("-")[1].strip()))
    return random.choice(flashcards)

class CTX(Widget):
    ctx = reactive("START")
    index = reactive(0)
    
    def render(self) -> str:
        return f"{self.ctx[self.index]}"


class APP(App):

    CSS_PATH = "main.css"

    BINDINGS = [("enter", "next", "Next"), ("q", "exit", "Exit")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield CTX()
        yield Footer()

    def action_next(self) -> None:
        if self.query_one(CTX).index == 0:
            self.query_one(CTX).index = 1
        else:
            self.query_one(CTX).ctx = flash(sys.argv[1])
            self.query_one(CTX).index = 0

    def action_exit(self) -> None:
        sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("HELP: python3 main.py <path_to_file>")
    else:
        app = APP()
        ctx = flash(sys.argv[1])
        app.run()
            
        
