class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.guardNode = Node(None, None)

    def __iter__(self):
        self.currentNode = self.guardNode.next
        return self

    def __next__(self):
        if self.currentNode is None:
            raise StopIteration
        else:
            tmp = self.currentNode
            self.currentNode = self.currentNode.next
            return tmp.value

    def append(self, value):
        end = self.guardNode
        while end.next is not None:
            end = end.next
        end.next = Node(value, None)
        return end.next

    def insertAfter(self, node, value):
        newNode = Node(value, node.next)
        node.next = newNode
        return newNode

    def delete(self, value):
        nodeBeforeDelete = self.guardNode
        while nodeBeforeDelete.next and nodeBeforeDelete.next.value != value:
            nodeBeforeDelete = nodeBeforeDelete.next
        if nodeBeforeDelete.next and nodeBeforeDelete.next.value == value:
            nodeBeforeDelete.next = nodeBeforeDelete.next.next
            return True
        else:
            return False

    def reverse(self):
        node = self.guardNode.next
        preNode = None
        while node:
            nextNode = node.next
            node.next = preNode

            preNode = node
            node = nextNode

        self.guardNode.next = preNode
        return self


if __name__ == "__main__":
    list = LinkedList()
    list.append(1)
    n2 = list.append(3)
    list.append(2)
    list.insertAfter(n2, 4)
    list.delete(2)
    list.delete(1)
    list.delete(5)
    list.delete(4)
    list.append(6)
    list.append(7)
    list.append(8)

    for item in list.reverse():
        print(item)
