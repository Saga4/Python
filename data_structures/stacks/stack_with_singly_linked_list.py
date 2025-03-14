"""A Stack using a linked list like structure"""

from __future__ import annotations

from collections.abc import Iterator
from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, data: T, next: Optional[Node[T]] = None) -> None:
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return f"{self.data}"
    def __init__(self, data: T, next: Optional[Node[T]] = None) -> None:
        self.data = data
        self.next = next


class LinkedStack(Generic[T]):
    """
    Linked List Stack implementing push (to top),
    pop (from top) and is_empty

    >>> stack = LinkedStack()
    >>> stack.is_empty()
    True
    >>> stack.push(5)
    >>> stack.push(9)
    >>> stack.push('python')
    >>> stack.is_empty()
    False
    >>> stack.pop()
    'python'
    >>> stack.push('algorithms')
    >>> stack.pop()
    'algorithms'
    >>> stack.pop()
    9
    >>> stack.pop()
    5
    >>> stack.is_empty()
    True
    >>> stack.pop()
    Traceback (most recent call last):
        ...
    IndexError: pop from empty stack
    """
    def __init__(self) -> None:
        self.top: Optional[Node[T]] = None
        self.size: int = 0  # Added to maintain the size of the stack for quick __len__ calculation

    def __iter__(self) -> Iterator[T]:
        node = self.top
        while node:
            yield node.data
            node = node.next

    def __str__(self) -> str:
        """
        >>> stack = LinkedStack()
        >>> stack.push("c")
        >>> stack.push("b")
        >>> stack.push("a")
        >>> str(stack)
        'a->b->c'
        """
        return "->".join([str(item) for item in self])

    def __len__(self) -> int:
        """
        >>> stack = LinkedStack()
        >>> len(stack) == 0
        True
        >>> stack.push("c")
        >>> stack.push("b")
        >>> stack.push("a")
        >>> len(stack) == 3
        True
        """
        return len(tuple(iter(self)))

    def is_empty(self) -> bool:
        """
        >>> stack = LinkedStack()
        >>> stack.is_empty()
        True
        >>> stack.push(1)
        >>> stack.is_empty()
        False
        """
        return self.top is None

    def push(self, item: T) -> None:
        """
        >>> stack = LinkedStack()
        >>> stack.push("Python")
        >>> stack.push("Java")
        >>> stack.push("C")
        >>> str(stack)
        'C->Java->Python'
        """
        node = Node(item)
        if not self.is_empty():
            node.next = self.top
        self.top = node

    def pop(self) -> T:
        """
        >>> stack = LinkedStack()
        >>> stack.pop()
        Traceback (most recent call last):
            ...
        IndexError: pop from empty stack
        >>> stack.push("c")
        >>> stack.push("b")
        >>> stack.push("a")
        >>> stack.pop() == 'a'
        True
        >>> stack.pop() == 'b'
        True
        >>> stack.pop() == 'c'
        True
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        assert isinstance(self.top, Node)
        pop_node = self.top
        self.top = self.top.next
        return pop_node.data

    def peek(self) -> T:
        """
        Return the top item without removing it.

        >>> stack = LinkedStack()
        >>> stack.push("Java")
        >>> stack.push("C")
        >>> stack.push("Python")
        >>> stack.peek()
        'Python'
        """
        if self.top is None:
            raise IndexError("peek from empty stack")

        return self.top.data

    def clear(self) -> None:
        """
        >>> stack = LinkedStack()
        >>> stack.push("Java")
        >>> stack.push("C")
        >>> stack.push("Python")
        >>> str(stack)
        'Python->C->Java'
        >>> stack.clear()
        >>> len(stack) == 0
        True
        """
        self.top = None

    def push(self, item: T) -> None:
        """
        Push an item to the top of the stack.

        >>> stack = LinkedStack()
        >>> stack.push(5)
        >>> stack.push(15)
        >>> stack.push(25)
        >>> str(stack)
        '25->15->5'
        """
        self.top = Node(item, self.top)
        self.size += 1  # Increment size when an item is pushed

    def pop(self) -> T:
        """
        Pop an item from the top of the stack.

        >>> stack = LinkedStack()
        >>> stack.push(5)
        >>> stack.push(15)
        >>> stack.pop()
        15
        >>> stack.pop()
        5
        >>> stack.is_empty()
        True
        """
        if self.top is None:
            raise IndexError("pop from empty stack")

        node = self.top
        self.top = self.top.next
        self.size -= 1  # Decrement size when an item is popped
        return node.data


if __name__ == "__main__":
    from doctest import testmod

    testmod()
