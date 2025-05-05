class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def sort(self):
        if self.head is None:
            return
        cur = self.head
        while cur:
            next_node = cur.next
            while next_node:
                if cur.data > next_node.data:
                    cur.data, next_node.data = next_node.data, cur.data
                next_node = next_node.next
            cur = cur.next

    def combine(self, other_list: 'LinkedList'):
        dummy = Node()
        tail = dummy
        l1 = self.head
        l2 = other_list.head

        while l1 and l2:
            if l1.data < l2.data:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        # Attach the remaining nodes from either list
        tail.next = l1 if l1 else l2

        # Update the head of the combined list
        self.head = dummy.next

llist = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

# Вставляємо вузли в кінець
llist.insert_at_end(20)
llist.insert_at_end(25)

# Друк зв'язного списку
print("Зв'язний список:")
llist.print_list()

# Видаляємо вузол
llist.delete_node(10)

print("\nЗв'язний список після видалення вузла з даними 10:")
llist.print_list()

# Пошук елемента у зв'язному списку
print("\nШукаємо елемент 15:")
element = llist.search_element(15)
if element:
    print(element.data)

# Реверс зв'язного списку
llist.reverse() 
print("\nЗв'язний список після реверсу:")
llist.print_list()

# Сортування зв'язного списку
llist.sort()
print("\nЗв'язний список після сортування:")
llist.print_list()

llist_2 = LinkedList()

# Вставляємо вузли в початок
llist_2.insert_at_beginning(100)
llist_2.insert_at_beginning(33)
llist_2.insert_at_beginning(150)
llist_2.insert_at_beginning(19)

llist_2.sort()

llist_2.print_list()

# Комбінування двох зв'язних списків
llist.combine(llist_2)
print("\nКомбінований зв'язний список:")
llist.print_list()
