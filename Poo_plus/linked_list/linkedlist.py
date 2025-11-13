from node import Node

class LinkedList:
    def __init__(self):
        self.fist = None
        self.last = None

    def  add_first(self,item):
        node_item = Node(item)
        node_item.next = self.add_first
        self.first= node_item

    def add_node_first(self,node:Node):
        node.next