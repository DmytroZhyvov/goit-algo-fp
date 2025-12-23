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
        """Reverse a linked list by changing node links."""
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    def sort_linked_list(self):
        """Sort a linked list using merge sort."""
        self.head = self._merge_sort(self.head)

    def _merge_sort(self, head):
        if not head or not head.next:
            return head

        middle = self._get_middle(head)
        next_to_middle = middle.next
        middle.next = None

        left = self._merge_sort(head)
        right = self._merge_sort(next_to_middle)

        return self._sorted_merge(left, right)

    def _get_middle(self, head):
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def _sorted_merge(self, left, right):
        if not left:
            return right
        if not right:
            return left

        if left.data <= right.data:
            result = left
            result.next = self._sorted_merge(left.next, right)
        else:
            result = right
            result.next = self._sorted_merge(left, right.next)

        return result

    @staticmethod
    def merge_sorted_lists(list1, list2):
        """Merge two sorted linked lists into one sorted list."""
        dummy = Node()
        tail = dummy

        while list1 and list2:
            if list1.data <= list2.data:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 if list1 else list2
        return dummy.next


if __name__ == "__main__":

    linked_list = LinkedList()
    for value in [5, 1, 8, 3, 2]:
        linked_list.insert_at_end(value)

    print("Original list: ")
    linked_list.print_list()

    linked_list.reverse()
    print("\nReversed list: ")
    linked_list.print_list()

    linked_list.sort_linked_list()
    print("\nSorted list: ")
    linked_list.print_list()

    list1 = LinkedList()
    list2 = LinkedList()

    for v in [3, 5, 7]:
        list1.insert_at_end(v)

    for v in [1, 2, 8]:
        list2.insert_at_end(v)

    print("\nFirst sorted list:")
    list1.print_list()

    print("\nSecond sorted list: ")
    list2.print_list()

    merged_head = LinkedList.merge_sorted_lists(list1.head, list2.head)
    merged_list = LinkedList()
    merged_list.head = merged_head

    print("\nMerged sorted list: ")
    merged_list.print_list()
