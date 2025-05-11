import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Node:
    def __init__(self, key, color="#87CEEB"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def build_heap_tree(heap_array):
    nodes = [Node(val) for val in heap_array]

    for i in range(len(nodes)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2

        if left_index < len(nodes):
            nodes[i].left = nodes[left_index]
        if right_index < len(nodes):
            nodes[i].right = nodes[right_index]

    return nodes[0] if nodes else None


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree_dynamic(root, visited_nodes, title="Tree Traversal"):
    tree = nx.DiGraph()
    pos = {root.id: (0, 0)}
    add_edges(tree, root, pos)

    plt.ion()
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.set_title(title)

    for step, node in enumerate(visited_nodes):
        highlight_color = "#1296F0"
        node.color = highlight_color
        tree.nodes[node.id]['color'] = highlight_color

        ax.clear()
        labels = {n[0]: n[1]['label'] for n in tree.nodes(data=True)}
        colors = [tree.nodes[n]['color'] for n in tree.nodes]

        nx.draw(tree, pos=pos, labels=labels, arrows=False,
                node_size=2500, node_color=colors, font_size=10, ax=ax)
        plt.pause(0.5)

    plt.ioff()
    plt.show()


def bfs_traversal(root):
    queue = deque([root])
    visited = []
    seen = set()

    while queue:
        node = queue.popleft()
        if node.id in seen:
            continue
        visited.append(node)
        seen.add(node.id)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return visited


def dfs_traversal(root):
    stack = [root]
    visited = []
    seen = set()

    while stack:
        node = stack.pop()
        if node.id in seen:
            continue
        visited.append(node)
        seen.add(node.id)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return visited


if __name__ == "__main__":
    heap_array = [1, 2, 3, 4, 5, 7, 10]
    root = build_heap_tree(heap_array)

    # BFS
    bfs_result = bfs_traversal(root)
    draw_tree_dynamic(root, bfs_result, title="BFS Traversal")

    # DFS
    for node in bfs_result:
        node.color = "#87CEEB"
    dfs_result = dfs_traversal(root)
    draw_tree_dynamic(root, dfs_result, title="DFS Traversal")
