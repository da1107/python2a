from typing import Any


class Node:
    """A node of a doubly linked list has a value and two node references"""
    def __init__(self, value: Any) -> None:
        self.value: Any = value
        self.prev: Node = None
        self.next: Node = None


class SimpleQueue:
    """A doubly linked list"""
    def __init__(self) -> None:
        self._head: Node = None
        self._tail: Node = None

    def append(self, value: Any) -> None:
        """Adds node with specified value at end of queue"""
        new_node = Node(value)
        try:                             # Assume queue is not empty
            new_node.next = self._tail
            self._tail.prev = new_node
        except AttributeError:           # Queue is empty
            self._head = new_node
        self._tail = new_node

    def popleft(self) -> Any:
        """Removes node at beginning of queue and returns its value"""
        value = self._head.value
        self._head = self._head.prev
        try:                             # Delete reference to removed node
            self._head.next = None
        except AttributeError:           # Queue became empty
            self._tail = None
        return value

    

