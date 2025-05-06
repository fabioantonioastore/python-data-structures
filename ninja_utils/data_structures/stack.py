from typing import Any, Generator
from collections.abc import Sequence, Iterable

from ninja_utils.data_structures import Node


class Stack(Sequence, Iterable):
    def __init__(self, data: Sequence[Any] | Iterable[Any] = None) -> None:
        self.__size = 0
        self.__top = None

        if data:
            for item in data:
                self.push(item)

    def peek(self) -> Any:
        return self.__top.data

    def push(self, item: Any) -> None:
        self.__size += 1
        node = Node(item)
        if self.__top is None:
            self.__top = node
            return
        node.next = self.__top
        self.__top = node

    def pop(self) -> Any:
        node = self.__top
        self.__top = self.__top.next
        self.__size -= 1
        return node.data

    def is_empty(self) -> bool:
        return len(self) == 0

    def insert(self, index: int, item: Any) -> None:
        if index == 0:
            self.push(item)
        if index < 0:
            index += len(self)
        if index >= len(self):
            node = self.__top
            while node.next:
                node = node.next
            node.next = Node(item)
            self.__size += 1
            return
        node = self.__top
        while index != 1:
            node = node.next
            index -= 1
        new_node = Node(index)
        new_node.next = node.next
        node.next = new_node
        self.__size += 1

    def remove(self, item: Any) -> Any:
        node = self.__top
        if node.data == item:
            return self.pop()
        while node:
            if node.next and node.next.data == item:
                remove_node = node.next
                node.next = remove_node.next
                self.__size -= 1
                return remove_node.data
            node = node.next
        return None

    def find(self, item: Any) -> bool:
        node = self.__top
        while node:
            if node.data == item:
                return True
            node = node.next
        return False

    def count(self, item: Any) -> int:
        total = 0
        node = self.__top
        while node:
            if node.data == item:
                total += 1
            node = node.next
        return total

    def __getitem__(self, index: int) -> Any:
        if index < 0:
            index += len(self)
        node = self.__top
        while index != 0:
            node = node.next
            index -= 1
        return node.data

    def __setitem__(self, index: int, item: Any) -> None:
        if index < 0:
            index += len(self)
        node = self.__top
        while index != 0:
            node = node.next
            index -= 1
        node.data = item

    def __iter__(self) -> Generator:
        node = self.__top
        while node:
            yield node.data
            node = node.next

    def __list__(self) -> list[Any]:
        data_list = []
        node = self.__top
        while node:
            data_list.append(node.data)
            node = node.next
        return data_list

    def __len__(self) -> int:
        return self.__size

    def __repr__(self) -> str:
        return f"Stack({list(self)!r})"
