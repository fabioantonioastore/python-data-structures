from typing import Any
from collections.abc import Iterable, Sequence

from ninja_utils.data_structures import BiNode


class Queue(Sequence, Iterable):
    def __init__(
        self, items: Sequence[Any] | Iterable[Any] = None
    ) -> None:
        self.__first = None
        self.__last = None
        self.__size = 0

        if items:
            for item in items:
                self.enqueue(item)

    def enqueue(self, item: Any) -> None:
        if self.is_full():
            raise "The queue is full"
        node = BiNode(item)
        self.__size += 1
        if self.__first is None:
            self.__first = node
            self.__last = node
            return
        self.__last.next = node
        node.prev = self.__last
        self.__last = node

    def dequeue(self) -> Any:
        node = self.__first
        self.__first = self.__first.next
        self.__first.prev = None
        self.__size -= 1
        return node.data

    def front(self) -> Any:
        return self.__first.data

    def rear(self) -> Any:
        return self.__last.data

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

    def remove(self, item: Any) -> Any:
        node = self.__first
        if node.data == item:
            return self.dequeue()
        while node:
            if node.data == item:
                node.prev.next = node.next
                node.next.prev = node.prev
                self.__size -= 1
                return node.data
            node = node.next
        return None

    def insert(self, index: int, item: Any) -> None:
        if self.is_full():
            raise "The queue is full"
        if index == -1:
            self.enqueue(item)
            return
        if index < 0:
            index += len(self)
        if index >= len(self):
            self.enqueue(item)
            return
        node = self.__first
        while index != 0:
            node = node.next
            index -= 1
        new_node = BiNode(item)
        new_node.prev = node.prev
        new_node.next = node
        node.prev.next = new_node
        node.prev = new_node
        self.__size += 1

    def __getitem__(self, index: int) -> Any:
        if index < 0:
            index += len(self)
        node = self.__first
        while index != 0:
            node = node.next
            index -= 1
        return node.data

    def __setitem__(self, index: int, item: Any) -> None:
        if index < 0:
            index += len(self)
        node = self.__first
        while index != 0:
            node = node.next
            index -= 1
        node.data = item

    def __iter__(self) -> Any:
        node = self.__first
        while node:
            yield node.data
            node = node.next

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
        return f"Queue({list(self)!r})"
