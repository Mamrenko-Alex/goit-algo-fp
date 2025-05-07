import uuid
import networkx as nx
import matplotlib.pyplot as plt


# Клас вузла дерева
class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


# Допоміжна функція для побудови дерева з масиву (купу)
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

# Рекурсивна функція для додавання вузлів та ребер у граф


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

# Функція для малювання дерева


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=colors, font_size=10)
    plt.show()


# масив - бінарна купа
heap_array = [1, 2, 3, 4, 5, 7, 10]
# heap_array = [1, 3, 5, 7, 9, 11, 13] # Ще один приклад

# Побудова дерева
heap_tree_root = build_heap_tree(heap_array)

# Відображення дерева
draw_tree(heap_tree_root)
