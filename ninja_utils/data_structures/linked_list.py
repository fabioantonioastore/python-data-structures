from typing import Any, Generator
from collections.abc import Sequence, Iterable

from ninja_utils.data_structures import BiNode


class LinkedList(Sequence, Iterable):
    def __init__(self, items: Sequence[Any] | Iterable[Any]) -> None:
        self.__first = None
        self.__last = None
        self.__size = 0

        if items:
            for item in items:
                self.insert_at_end(item)

    def insert_at_end(self, item: Any) -> None:
        node = BiNode(item)
        self.__size += 1
        if self.__first is None:
            self.__first = node
            self.__last = node
            return
        self.__last.next = node
        node.prev = self.__last
        self.__last = node

    def insert_at_begin(self, item: Any) -> None:
        node = BiNode(item)
        self.__size += 1
        if self.__first is None:
            self.__first = node
            self.__last = node
            return
        node.next = self.__first
        self.__first.prev = node
        self.__first = node

    def insert(self, index: int, item: Any) -> None:
        if index == 0:
            self.insert_at_begin(item)
            return
        if index == -1:
            self.insert_at_end(item)
        if index < 0:
            index += len(self)
        if index >= len(self):
            self.insert_at_end(item)
            return
        node = self.__first
        while index != 0:
            node = node.next
            index -= 1
        new_node = BiNode(item)
        new_node.next = node
        new_node.prev = node.prev
        node.prev.next = new_node
        node.prev = new_node
        new_node.next = node
        self.__size += 1

    def remove(self, item: Any) -> Any:
        if self.__first.data == item:
            return self.pop_front()
        if self.__last.data == item:
            return self.pop_end()
        node = self.__first
        while node:
            if node.data == item:
                node.prev.next = node.next
                node.next.prev = node.prev
                self.__size -= 1
                return node.data
            node = node.next
        return None

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

    def pop_front(self) -> Any:
        node = self.__first
        self.__size -= 1
        self.__first = self.__first.next
        if self.__first is None:
            self.__last = None
        else:
            self.__first.prev = None
        return node.data

    def pop_end(self) -> Any:
        node = self.__last
        self.__size -= 1
        self.__last = self.__last.prev
        if self.__last is None:
            self.__first = None
        else:
            self.__last.next = None
        return node.data

    def is_empty(self) -> bool:
        return len(self) == 0

    def __list__(self) -> list[Any]:
        item_list = []
        node = self.__first
        while node:
            item_list.append(node.data)
            node = node.next
        return item_list

    def __iter__(self) -> Generator[Any]:
        node = self.__first
        while node:
            yield node.data
            node = node.next

    def __getitem__(self, index: int) -> Any:
        node = self.__first
        if index < 0:
            index += len(self)
        while index != 0:
            node = node.next
            index -= 1
        return node.data

    def __setitem__(self, index: int, item: Any) -> None:
        node = self.__first
        if index < 0:
            index += len(self)
        while index != 0:
            node = node.next
            index -= 1
        node.data = item

    def __len__(self) -> int:
        return self.__size
