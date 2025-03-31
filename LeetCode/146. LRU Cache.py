"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.



Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4


Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.
"""
from functools import cache
from typing import Tuple


class LRUCache:
    class Node:
        def __init__(self,val,prev,next):
            self.val = val
            self.next = next
            self.prev = prev


    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = self.Node(-1,None,None)
        self.tail = self.Node(-1,None,None)

        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove_node(node)
        self.add_to_head(node)
        return self.cache[key].val[1]

    def put(self, key: int, value: int) -> None:

        if key in self.cache :
            self.cache[key].val = key,value
            self.remove_node(self.cache[key])
            self.add_to_head(self.cache[key])
        else:
            newNode = self.Node((key,value),None,None)
            self.cache[key] = newNode
            self.add_to_head(newNode)

            if len(self.cache)  > self.capacity:
                node = self.remove_tail()
                self.cache.pop(node.val[0])


    def remove_node(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev


    def remove_tail(self):
        temp = self.tail.prev
        self.remove_node(temp)
        return temp

    def add_to_head(self,node):

        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head
