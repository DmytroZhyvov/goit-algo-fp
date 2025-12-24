from collections import deque
from task_04 import Node, draw_tree


def dfs_order(root):
    stack = [root]
    order = []

    while stack:
        node = stack.pop()
        order.append(node)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return order


def bfs_order(root):
    queue = deque([root])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return order


def gradient_color(step, total):
    dark = (30, 30, 60)
    light = (180, 220, 255)

    t = step / max(total - 1, 1)
    r = int(dark[0] + (light[0] - dark[0]) * t)
    g = int(dark[1] + (light[1] - dark[1]) * t)
    b = int(dark[2] + (light[2] - dark[2]) * t)

    return f"#{r:02x}{g:02x}{b:02x}"


def visualize_traversal(root, mode="dfs"):
    if mode == "dfs":
        order = dfs_order(root)
        title = "DFS"
    elif mode == "bfs":
        order = bfs_order(root)
        title = "BFS"
    else:
        raise ValueError("mode must be 'dfs' or 'bfs'")

    for node in order:
        node.color = "#1a1a1a"

    for i, node in enumerate(order):
        node.color = gradient_color(i, len(order))
        draw_tree(root, f"{title} step {i + 1}: visit {node.val}")


if __name__ == "__main__":
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    visualize_traversal(root, mode="dfs")
    visualize_traversal(root, mode="bfs")
