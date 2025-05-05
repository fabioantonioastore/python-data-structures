from typing import Any

from ninja_utils.data_structures import Node

class BiNode(Node):
    def __init__(self, data: Any, next: 'Node' = None, prev: 'Node' = None) -> None:
        super().__init__(data, next)
        self.prev = prev

    def __repr__(self) -> str:
        return f"BiNode({self.data!r}, {self.next!r}, {self.prev!r})"
