# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition of list
class SLinkedList:
    def __init__(self):
        self.head =None

    # list all the nodes
    def listPrint(self):
        printval = self.head
        print("print list")
        while printval is not None:
            print(printval.val)
            printval = printval.next

    # find node
    def findNode(self, val ):
        findval = self.head
        while findval is not None:
            if findval.val == val:
                return findval
            findval = findval.next
        return None

    # add node at the beginning
    def addAtBeginning(self, newdata):
        NewNode = ListNode(newdata)
        NewNode.next = self.head
        self.head = NewNode

    # add node at the end
    def addAtEnd(self,newdata):
        NewNode = ListNode(newdata)
        if self.head is None:
            self.head = NewNode
            return
        laste = self.head
        while laste.next:
            laste = laste.next
        laste.next = NewNode

    # add node in between
    def addInBetween(self, middle_node, newdata):
        if middle_node is None:
            print("node not in list")
            return
        NewNode = ListNode(newdata)
        NewNode.next = middle_node.next
        middle_node.next = NewNode

    # remove a node
    def removeNode( self, RemoveKey):
        HeadVal = self.head

        if HeadVal is not None:
            if HeadVal.val == RemoveKey:
                self.head = HeadVal.next
                HeadVal = None
                return
            while HeadVal is not None:
                if HeadVal.val == RemoveKey:
                    break
                prev = HeadVal
                HeadVal = HeadVal.next

            if HeadVal is None:
                return

            print (prev.val, HeadVal.next.val)
            prev.next = HeadVal.next
            print (prev.next.val)
            HeadVal = None
     

class Solution(object):
    def testMethods(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        list1 = SLinkedList()

        # build linked list
        for value in head:
            NewNode = ListNode(value)
            if list1.head is None:
                list1.head = NewNode
            else:
                prev.next = NewNode 

            prev = NewNode

        # print the new list
        list1.listPrint()

        list1.addAtEnd(9)
        list1.listPrint()

        list1.addAtBeginning(4)
        list1.listPrint()

        # find node
        foundnode = list1.findNode(7)
        if foundnode:
            print("found node", foundnode.val)
        else:
            print("node not found")

        list1.addInBetween(foundnode,8)
        list1.listPrint()

        list1.removeNode(3)
        list1.listPrint()

def main():
    """
    :main calling program
    :
    """
    head = [1,1,2,2,3,4,5,5,6,7]
    res = Solution().testMethods( head )
    print (res)

if __name__ == '__main__':
    main()
