from typing import Any, Generator
from collections.abc import Sequence, Iterable

from ninja_utils.data_structures import Node


class SinglyLinkedList(Sequence, Iterable):
    def __init__(self, items: Sequence[Any] | Iterable[Any]) -> None:
        self.__first = None
        self.__size = 0

        if items:
            for item in items:
                self.insert_at_end(item)

    def insert_at_begin(self, item: Any) -> None:
        node = Node(item)
        self.__size += 1
        if self.__first is None:
            self.__first = node
            return
        node.next = self.__first
        self.__first = node

    def insert_at_end(self, item: Any) -> None:
        new_node = Node(item)
        self.__size += 1
        if self.__first is None:
            self.__first = new_node
            return
        node = self.__first
        while node.next:
            node = node.next
        node.next = new_node

    def is_empty(self) -> bool:
        return len(self) == 0

    def find(self, item: Any) -> bool:
        node = self.__first
        while node:
            if node.data == item:
                return True
            node = node.next
        return False

    def count(self, item: Any) -> int:
        total = 0
        node = self.__first
        while node:
            if node.data == item:
                total += 1
            node = node.next
        return total

    def pop_first(self) -> Any:
        node = self.__first
        self.__first = self.__first.next
        self.__size -= 1
        return node.data

    def pop_end(self) -> Any:
        if len(self) == 1:
            return self.pop_first()
        node = self.__first
        while node.next.next:
            node = node.next
        remove_node = node.next
        node.next = None
        self.__size -= 1
        return remove_node.data

    def insert(self, index: int, item: Any) -> None:
        if index == 0:
            self.insert_at_begin(item)
            return
        if index == -1:
            self.insert_at_end(item)
            return
        if index < 0:
            index += len(self)
        node = self.__first
        while index != 1:
            node = node.next
        new_node = Node(item)
        new_node.next = node.next
        node.next = new_node

    def remove(self, item: Any) -> Any:
        node = self.__first
        if node.data == item:
            return self.pop_first()
        while node.next:
            if node.next.data == item:
                remove_node = node.next
                node.next = remove_node.next
                self.__size -= 1
                return remove_node.data
            node = node.next
        return None

    def __iter__(self) -> Generator[Any]:
        node = self.__first
        while node:
            yield node.data
            node = node.next

    def __getitem__(self, index: int) -> Any:
        if index < 0:
            index += 1
        node = self.__first
        while index != 0:
            node = node.next
            index -= 1
        return node.data

    def __setitem__(self, index: int, item: Any) -> None:
        if index < 0:
            index += 1
        node = self.__first
        while index != 0:
            node = node.next
            index -= 1
        node.data = item

    def __list__(self) -> list[Any]:
        item_list = []
        node = self.__first
        while node:
            item_list.append(node.data)
            node = node.next
        return item_list

    def __len__(self) -> int:
        return self.__size

    def __repr__(self) -> str:
        return f"SinglyLinkedList({list(self)!r})"
