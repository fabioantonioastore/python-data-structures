from typing import Any


class Node:
    def __init__(self, data: Any, next: "Node" = None) -> None:
        self.data = data
        self.next = next

    def __repr__(self) -> str:
        return f"Node({self.data!r}, {self.next!r})"
