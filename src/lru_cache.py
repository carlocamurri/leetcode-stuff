class LRUNode:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.previous = None
        self.next = None

    def __str__(self):
        s = 'key: {}, value: {}'.format(self.key, self.value)
        return s


class DoublyLinkedList:

    def __init__(self):
        self.head = LRUNode(0, 0)
        self.tail = LRUNode(0, 0)
        self.head.next = self.tail
        self.tail.previous = self.head

    def append(self, node):
        old_previous = self.tail.previous
        old_previous.next = node
        node.previous = old_previous
        node.next = self.tail
        self.tail.previous = node

    def remove(self, node):
        p = node.previous
        n = node.next
        p.next = n
        n.previous = p

    def __str__(self):
        s = 'Doubly linked list\n'
        it = self.head.next
        while it != self.tail:
            s += '\t' + str(it) + '\n'
            it = it.next
        return s


class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.store = {}
        self.linked_list = DoublyLinkedList()

    def get(self, key):
        if key not in self.store:
            return -1
        else:
            node = self.store[key]
            self.linked_list.remove(node)
            self.linked_list.append(node)
            return node.value

    def put(self, key, value):
        if key in self.store:
            self.linked_list.remove(self.store[key])
            del self.store[key]
        '''if len(self.store) == self.capacity:
            to_remove = self.linked_list.head.next
            key_to_remove = to_remove.key
            self.linked_list.remove(to_remove)
            del self.store[key_to_remove]'''
        new_node = LRUNode(key, value)
        self.linked_list.append(new_node)
        self.store[key] = new_node


if __name__ == '__main__':
    cache = LRUCache(2)

    print(cache.get(2))
    cache.put(2, 6)
    print(cache.get(1))
    cache.put(1, 5)
    cache.put(1, 2)
    print(cache.get(1))
    print(cache.get(2))
    cache.put(3, 10)
    print(cache.get(2))

    print(cache.store)
    print(cache.linked_list)
