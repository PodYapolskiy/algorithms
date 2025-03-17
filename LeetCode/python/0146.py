class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        """
        Time:  O(1)
        Space: O(1)
        """
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # update DLL due to recent access
        self._remove_node(node)
        self._add_to_head(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        """
        Time:  O(1)
        Space: O(1)
        """
        if key in self.cache:
            node = self.cache[key]
            node.value = value

            # move node to head (recent access)
            self._remove_node(node)
            self._add_to_head(node)
        else:
            new_node = Node(key, value)
            if self.size == self.capacity:
                # pop oldest used cache node
                removed_node = self._pop_tail()
                del self.cache[removed_node.key]
                self.size -= 1

            self.cache[key] = new_node  # put element
            self._add_to_head(new_node)  # inserts new node near head
            self.size += 1

    def _add_to_head(self, node: Node) -> None:
        """
        Time:  O(1)
        Space: O(1)
        """
        # set new node's prev and next (insert near head)
        node.prev = self.head
        node.next = self.head.next

        # change pointers that points to new node
        self.head.next.prev = node  # prev next of head is now has prev as new node
        self.head.next = node  # new next of head is new node

    def _remove_node(self, node: Node) -> None:
        """
        Time:  O(1)
        Space: O(1)
        """
        node.prev.next = node.next
        node.next.prev = node.prev

    def _pop_tail(self) -> Node:
        node = self.tail.prev
        self._remove_node(node)
        return node
