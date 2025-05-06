from typing import Any


class BiTreeNode:
    def __init__(
        self, data: Any, left: "BiTreeNode" = None, right: "BiTreeNode" = None
    ) -> None:
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"BiTreeNode({self.data!r}, {self.left!r}, {self.right!r})"
