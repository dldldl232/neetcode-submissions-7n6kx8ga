class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    # we need O(1) for both lookup and reordering
    # inorder to acheive this the lookup needs to use hash map
    # while the reordering is done through a doubly linked list
    # -> we have to use both structures to achieve O(1)

    # the linked list will keep the nodes ordered as most recently used(head) to least
    # recently used (tail). 

    # we are using doubly linked list instead of single linked list 
    # because we need both prev and next to stich them together, while
    # single linked list would force to walk from head to find the prev
    # node -> O(n)

    # ORDEREDDICT DOES THIS UNDER THE HOOD, BT HERE'S HOW I'D BUILD IT FROM SCRATCH

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key -> Node

        # Dummy head/tail  to avoid edge-case checks
        self.head = Node()
        self.tail = Node()
        # the two lines below is a classic sentinel node trick
        # head and tail are dummy placeholders - they never hold real
        # key/value data. Exist purely to eliminate edge cases:
        # w/o sentinal inserting into an empty list needs special-case code
        # with sential head and tail always exist 
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        # unlink node from the list
        prev_node, next_node = node.prev, node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    """Cause of sentinal we don't have to check is this the very first node? every time 
    in remove and add_to_front """

    def _add_to_front(self, node):
        """ Insert node right after head cause head is a sential its just a wall"""
        node.prev = self.head # new node's prev = the wall (head)
        node.next = self.head.next # new node's next = old front node
        self.head.next.prev = node # old front node's prev = new node
        self.head.next = node # wall's next = new node

    def get(self, key: int) -> int:
        # we would have to remove it from curr position -> add to front as "used"
        if key not in self.cache:
            return -1
        node = self.cache[key] # retrieve value
        self._remove(node) # remove it at curr position
        self._add_to_front(node) # move to front
        return node.value

    def put(self, key: int, value: int) -> None:
        # exist -> remove
        # new node -> add to front
        # exceed capacity -> evict tail.prev (as it is the LRU node)
        if key in self.cache:
            self._remove(self.cache[key])
        
        node = Node(key, value) # create node
        self.cache[key] = node # put in cache memory 
        self._add_to_front(node) # then add to front

        if len(self.cache) > self.capacity:
            # Evict least recently used (right before tail)
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]

        
