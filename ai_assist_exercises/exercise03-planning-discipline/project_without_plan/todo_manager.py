"""A toy to-do list manager used for planning exercises."""

from dataclasses import dataclass, field
from typing import List


default_categories = ["inbox", "in-progress", "done"]


@dataclass
class TodoItem:
    title: str
    category: str = "inbox"
    notes: List[str] = field(default_factory=list)


class TodoManager:
    def __init__(self) -> None:
        self.items: List[TodoItem] = []

    def add(self, title: str, category: str = "inbox") -> TodoItem:
        item = TodoItem(title=title, category=category)
        self.items.append(item)
        return item

    def find_by_category(self, category: str) -> List[TodoItem]:
        return [item for item in self.items if item.category == category]


if __name__ == "__main__":
    manager = TodoManager()
    manager.add("Prototype Cursor exercise")
    print(len(manager.items))
