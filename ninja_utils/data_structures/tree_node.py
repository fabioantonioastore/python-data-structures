from typing import Any


class TreeNode:
    def __init__(
        self,
        data: Any,
        left: "TreeNode" = None,
        right: "TreeNode" = None,
        prev: "TreeNode" = None,
    ) -> None:
        self.data = data
        self.left = left
        self.right = right
        self.prev = prev

    def __repr__(self) -> str:
        return f"TreeNode({self.data!r}, {self.left!r}, {self.right!r}, {self.prev!r})"
