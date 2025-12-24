import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)

        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)

        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)

    return graph


def draw_tree(tree_root, title=None):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(10, 6))
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )

    if title:
        plt.title(title)

    plt.show()


def build_heap_tree(heap_list):
    """Build a binary tree"""

    if not heap_list:
        return None

    nodes = [Node(value) for value in heap_list]

    for i in range(len(nodes)):
        left_i = 2 * i + 1
        right_i = 2 * i + 2

        if left_i < len(nodes):
            nodes[i].left = nodes[left_i]
        if right_i < len(nodes):
            nodes[i].right = nodes[right_i]

    return nodes[0]


def visualize_heap(data, as_min_heap=True):
    """Visualizes a binary heap by converting the heap array into a binary tree and drawing it"""
    heap_arr = list(data)

    if as_min_heap:
        heapq.heapify(heap_arr)

    root = build_heap_tree(heap_arr)
    if root is None:
        print("Heap is empty.")
        return

    draw_tree(root)


if __name__ == "__main__":
    arr = [10, 4, 7, 1, 3, 9, 2, 8, 6, 5]

    print("Original array:", arr)
    print("Visualizing as MIN-HEAP (after heapify):")
    visualize_heap(arr, as_min_heap=True)
