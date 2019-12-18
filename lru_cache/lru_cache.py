from doubly_linked_list import DoublyLinkedList
import sys

sys.path.append("../doubly_linked_list")


class LRUCache:

    # least recenty used
    # cache eviction policy
    # when you access an item it moves to the front of the list
    # when you remove an item it's the most recently used(tail)
    # cache is something that stores computation to look up later, speed up future requests
    # a chache using the lru cache eviction policy max number of nodes
    # two api functions get and put
    # lru if you go over capacity eviction
    # need to get and put in constant time 0(1)
    # fast lookups and fast removal
    # hashtables are used for fast lookups
    # doubly linked list for fast removals, removal in constant time
    # initialize list with dummy head and dummy tail
    # look up by keys of K,V

    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.cache = {}
        self.order = DoublyLinkedList()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    # cache holds the key/node location of value
    # DLL holds actual value
    # remove from current list and place at the front
    # update the cache with new key location

    def get(self, key):

        # if key exists
        if key in self.cache:
            node = self.cache[key]
            self.order.move_to_front(node)
            return node.value[1]
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        pass
    # if key already esists, overwrite its value in DLL
    # delete old value
    # add new value to tail
    # update cache with new location
    # if key does not exist
    # check to see if there is room
    #
