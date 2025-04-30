import sys
from collections import defaultdict


class Heap:
    def __init__(self):
        self.node_position = []  # Initialize the node position list

    def get_position(self, vertex):
        return self.node_position[vertex]  # Get the position of the vertex

    def set_position(self, vertex, pos):
        self.node_position[vertex] = pos  # Set the position of the vertex

    def top_to_bottom(self, heap, start, size, positions):
        smallest_child = start  # Initialize smallest_child with start index

        while start < size // 2:  # Loop until start is greater than half of size
            left_child = 2 * start + 1
            right_child = 2 * start + 2

            if left_child < size and heap[left_child] < heap[smallest_child]:
                smallest_child = left_child
            if right_child < size and heap[right_child] < heap[smallest_child]:
                smallest_child = right_child

            if smallest_child != start:
                # Swap heap elements and their positions
                heap[start], heap[smallest_child] = heap[smallest_child], heap[start]
                positions[start], positions[smallest_child] = positions[smallest_child], positions[start]

                # Update node positions
                self.node_position[positions[start]], self.node_position[positions[smallest_child]] = (
                    self.node_position[positions[smallest_child]], self.node_position[positions[start]]
                )

                # Proceeds to check the next part of the heap
                start = smallest_child
            else:
                break  # If already in correct position, break the loop

    # Update function if value of any node in min-heap decreases
    def bottom_to_top(self, val, index, heap, position):
        temp = position[index]

        while index != 0:
            parent = int((index - 2) / 2) if index % 2 == 0 else int((index - 1) / 2)

            if val < heap[parent]:
                heap[index] = heap[parent]
                position[index] = position[parent]
                self.set_position(position[parent], index)
            else:
                heap[index] = val
                position[index] = temp
                self.set_position(temp, index)
                break
            index = parent
        else:
            heap[0] = val
            position[0] = temp
            self.set_position(temp, 0)

    def heapify(self, heap, positions):
        start = len(heap) // 2 - 1
        for i in range(start, -1, -1):
            self.top_to_bottom(heap, i, len(heap), positions)

    def delete_minimum(self, heap, positions):
        temp = positions[0]
        heap[0] = sys.maxsize
        self.top_to_bottom(heap, 0, len(heap), positions)
        return temp

    def build_heap(self, heap, size, positions):
        # Build heap by calling top_to_bottom for each node
        for i in range(size // 2, -1, -1):
            self.top_to_bottom(heap, i, size, positions)


def prisms_algorithm(adjacency_list):
    """
    >>> adjacency_list = {0: [[1, 1], [3, 3]],
    ...                   1: [[0, 1], [2, 6], [3, 5], [4, 1]],
    ...                   2: [[1, 6], [4, 5], [5, 2]],
    ...                   3: [[0, 3], [1, 5], [4, 1]],
    ...                   4: [[1, 1], [2, 5], [3, 1], [5, 4]],
    ...                   5: [[2, 2], [4, 4]]}
    >>> prisms_algorithm(adjacency_list)
    [(0, 1), (1, 4), (4, 3), (4, 5), (5, 2)]
    """

    heap = Heap()

    visited = [0] * len(adjacency_list)
    nbr_tv = [-1] * len(adjacency_list)  # Neighboring Tree Vertex of selected vertex
    # Minimum Distance of explored vertex with neighboring vertex of partial tree
    # formed in graph
    distance_tv = []  # Heap of Distance of vertices from their neighboring vertex
    positions = []

    for vertex in range(len(adjacency_list)):
        distance_tv.append(sys.maxsize)
        positions.append(vertex)
        heap.node_position.append(vertex)

    tree_edges = []
    visited[0] = 1
    distance_tv[0] = sys.maxsize
    for neighbor, distance in adjacency_list[0]:
        nbr_tv[neighbor] = 0
        distance_tv[neighbor] = distance
    heap.heapify(distance_tv, positions)

    for _ in range(1, len(adjacency_list)):
        vertex = heap.delete_minimum(distance_tv, positions)
        if visited[vertex] == 0:
            tree_edges.append((nbr_tv[vertex], vertex))
            visited[vertex] = 1
            for neighbor, distance in adjacency_list[vertex]:
                if (
                    visited[neighbor] == 0
                    and distance < distance_tv[heap.get_position(neighbor)]
                ):
                    distance_tv[heap.get_position(neighbor)] = distance
                    heap.bottom_to_top(
                        distance, heap.get_position(neighbor), distance_tv, positions
                    )
                    nbr_tv[neighbor] = vertex
    return tree_edges


if __name__ == "__main__":  # pragma: no cover
    # < --------- Prims Algorithm --------- >
    edges_number = int(input("Enter number of edges: ").strip())
    adjacency_list = defaultdict(list)
    for _ in range(edges_number):
        edge = [int(x) for x in input().strip().split()]
        adjacency_list[edge[0]].append([edge[1], edge[2]])
        adjacency_list[edge[1]].append([edge[0], edge[2]])
    print(prisms_algorithm(adjacency_list))
