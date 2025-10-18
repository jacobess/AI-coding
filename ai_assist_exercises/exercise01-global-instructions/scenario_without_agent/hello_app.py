"""Small CLI greeter used for AI-assist practice."""

from datetime import datetime


def greet(name: str) -> str:
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M")
    return f"[{timestamp}] Hello, {name}!"


if __name__ == "__main__":
    print(greet("Cursor"))
