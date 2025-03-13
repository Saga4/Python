"""
Sum of all nodes in a binary tree.

Python implementation:
    O(n) time complexity - Recurses through :meth:`depth_first_search`
                            with each element.
    O(n) space complexity - At any point in time maximum number of stack
                            frames that could be in memory is `n`
"""

from __future__ import annotations

from collections.abc import Iterator


class Node:
    """
    A Node has a value variable and pointers to Nodes to its left and right.
    """
    def __init__(self, value: int, left: Node | None = None, right: Node | None = None) -> None:
        self.value = value
        self.left = left
        self.right = right
    def __init__(self, value: int, left: Node | None = None, right: Node | None = None) -> None:
        self.value = value
        self.left = left
        self.right = right


class BinaryTreeNodeSum:
    r"""
    The below tree looks like this
        10
       /  \
      5   -3
     /    / \
    12   8  0

    >>> tree = Node(10)
    >>> sum(BinaryTreeNodeSum(tree))
    10

    >>> tree.left = Node(5)
    >>> sum(BinaryTreeNodeSum(tree))
    15

    >>> tree.right = Node(-3)
    >>> sum(BinaryTreeNodeSum(tree))
    12

    >>> tree.left.left = Node(12)
    >>> sum(BinaryTreeNodeSum(tree))
    24

    >>> tree.right.left = Node(8)
    >>> tree.right.right = Node(0)
    >>> sum(BinaryTreeNodeSum(tree))
    32
    """
    def __init__(self, tree: Node) -> None:
        self.tree = tree

    def depth_first_search(self, node: Node | None) -> int:
        if node is None:
            return 0
        # Directly summing values to avoid additional recursive calls
        node_sum = node.value
        if node.left:
            node_sum += self.depth_first_search(node.left)
        if node.right:
            node_sum += self.depth_first_search(node.right)
        return node_sum

    def __iter__(self) -> Iterator[int]:
        yield self.depth_first_search(self.tree)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
