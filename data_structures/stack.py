from typing import Any
from collections.abc import Iterable
from wsgiref.util import request_uri

from data_structures import Node


class Stack(Iterable):
    def __init__(self) -> None:
        self.__head = None
        self.__tail = None
        self.__iter_stack = None
        self.__size = 0

    @property
    def head(self) -> Any:
        if self.__head:
            return self.__head.data
        return None

    @property
    def tail(self) -> Any:
        if self.__tail:
            return self.__tail.data
        return None

    def push(self, item: Any) -> None:
        node = Node(item)
        self.__size += 1

        if self.__head is None:
            self.__head = node
            self.__tail = self.__head
            return
        self.__head.prev = node
        node.next = self.__head
        self.__head = node

    def is_empty(self) -> bool:
        return len(self) == 0

    def pop(self) -> Any:
        if self.is_empty():
            raise Exception("The Stack is empty")

        item = self.__head.data
        self.__size -= 1
        if self.__head is self.__tail:
            self.__head = None
            self.__tail = None
            return item
        self.__head = self.__head.next
        self.__head.prev = None
        return item

    def peek(self) -> Any:
        if self.is_empty():
            raise Exception("The Stack is empty")

        return self.__head.data

    def __list__(self) -> list[Any]:
        node = self.__head
        items = []
        while not node is None:
            items.append(node.data)
            node = node.next
        return items

    def remove(self) -> Any:
        pass

    def insert(self) -> None:
        pass

    def __getitem__(self, index: int) -> Any:
        try:
            if index >= 0:
                node = self.__head
                while index >= 0:
                    if index == 0:
                        return node.data
                    node = node.next
                    index -= 1
            node = self.__tail
            while index < 0:
                if index == -1:
                    return node.data
                node = node.prev
                index += 1
        except Exception:
            raise IndexError("Index overflow")

    def __setitem__(self, index, data) -> None:
        try:
            if index >= 0:
                node = self.__head
                while index >= 0:
                    if index == 0:
                        node.data = data
                        return
                    node = node.next
                    index -= 1
            node = self.__tail
            while index < 0:
                if index == -1:
                    node.data = data
                    return
                node = node.prev
                index += 1
        except Exception:
            raise IndexError("Index overflow")

    def __iter__(self) -> "Stack":
        if not self.__iter_stack:
            self.__iter_stack = Stack()
        self.__iter_stack.push(self.__head)
        return self

    def __next__(self) -> Any:
        node = self.__iter_stack.peek()
        if node is None:
            self.__iter_stack.pop()
            raise StopIteration
        self.__iter_stack[0] = node.next
        return node.data

    def __repr__(self) -> str:
        return "Stack()"

    def __len__(self) -> int:
        return self.__size
