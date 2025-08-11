import reflex as rx
from rxconfig import config

class State(rx.State):
    target: str = ""
    suggestion: str = ""

    def submit_target(self):
        # call backend to save target & get suggestions
        pass

def index():
    return rx.vstack(
        rx.input(on_blur=State.set_target),
        rx.button("Suggest", on_click=State.submit_target),
        rx.text(State.suggestion),
    )

app = rx.App(state=State)
app.add_page(index)

