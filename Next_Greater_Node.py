class Node:
    #Defining node class
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode

class LinkedList:
    #defining how to insert values into node class
    def __init__(self):
        self.head = None

    #defining data as new node and always set the nextnode as data if not the first node
    def insert(self, data):
        newNode = Node(data)
        if (self.head):
            current = self.head
            while (current.nextNode):
                current = current.nextNode
            current.nextNode = newNode
        else:
            #if its first node set head as node
            self.head = newNode

class NextGreaterNode:

    def nextGreaterNodes(self):
        result = []
        gNode = None
        current1 = self.linkedList.head
        #getting the first node and using two loops : current node and its next nodes
        while (current1):
            current2 = current1
            gNode = current1
            while (current2):
                if (current2.nextNode):
                    #if it has a greater value set this node as a greater and do a break
                    if (current2.nextNode.value > gNode.value):
                        gNode = current2.nextNode
                        break
                current2 = current2.nextNode
            #if there's no next node set greater value as 0
            result.append(0 if gNode.value == current1.value else gNode.value)
            current1 = current1.nextNode
        return result

    def __init__(self, input):
        #we are giving the whole list at the init method, and assign it to a new linkedlist class
        self.linkedList = LinkedList()
        for val in input:
            self.linkedList.insert(val)

list =     [2,1,5]

nextGreaterNode = NextGreaterNode(list)

result = nextGreaterNode.nextGreaterNodes()
print(result)

list =     [2,7,4,3,5]

nextGreaterNode = NextGreaterNode(list)

result = nextGreaterNode.nextGreaterNodes()
print(result)

list =    [1,7,5,1,9,2,5,1]

nextGreaterNode = NextGreaterNode(list)

result = nextGreaterNode.nextGreaterNodes()
print(result)

