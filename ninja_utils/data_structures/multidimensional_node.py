from typing import Any, Generator


class MultidimensionalNode:
    def __init__(self, data: Any, nodes: list['MultidimensionalNode'] = None) -> None:
        self.data = data
        self.nodes = []
        if nodes:
            self.nodes = nodes

    def __iter__(self) -> Generator:
        for node in self.nodes:
            yield node

    def __getitem__(self, index: int) -> 'MultidimensionalNode':
        return self.nodes[index]

    def __setitem__(self, index: int, node: 'MultidimensionalNode') -> None:
        self.nodes[index] = node

    def __len__(self) -> int:
        return len(self.nodes)

    def __repr__(self) -> str:
        return f"MultidimensionalNodes({self.data!r}, {self.nodes!r})"
