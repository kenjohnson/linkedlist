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
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # convert input list to linked list

        list1 = SLinkedList()

        for value in head:
            NewNode = ListNode(value)
            if list1.head is None:
                list1.head = NewNode
            else:
                prev.next = NewNode

            prev = NewNode

        # print the new list
        list1.listPrint()

        #delete duplicates

        curr = list1.head
        prev = list1.head

        while curr is not None and curr.next:

            if curr.val == curr.next.val:

                if list1.head == curr:
                    list1.head = curr.next
                prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next


        print ("done removing duplicates")

        list1.listPrint()


        #convert linked list back to list and return
        res = []
        listval = list1.head
        while listval is not None:
            res.append(listval.val)
            listval = listval.next
        return res

def main():
    """
    :main calling program
    :
    """

    head = [ 1,1,2 ]
    res = Solution().deleteDuplicates( head )
    print (res)

    head = [ 1,1,2, 3,3]
    res = Solution().deleteDuplicates( head )
    print (res)

    head = [1 ]
    res = Solution().deleteDuplicates( head )
    print (res)

    head = [ ]
    res = Solution().deleteDuplicates( head )
    print (res)

    head = [1,1,2,2,3,4,5,5,6,7]
    res = Solution().deleteDuplicates( head )
    print (res)

if __name__ == '__main__':
    main()
