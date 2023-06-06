# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
     
        curr1 = list1
        curr2  = list2

        dummy = ListNode()
        res = dummy

        while curr1 and curr2:
            if curr1.val < curr2.val:
                res.next = curr1
                curr1 = curr1.next
            else:
                res.next = curr2
                curr2= curr2.next

            res = res.next


        # If list are different sizes, add remaining list here
        if curr1:
            res.next = curr1

        if curr2:
            res.next = curr2

        return dummy.next


# build a linked list from a list
def buildLinkedList(input):

    if not input:
        return

    for i in range(0,len(input)):
        if i == 0:
            list = curr = ListNode(input[0])
        else:
            curr.next = ListNode(input[i])
            curr = curr.next

    return list

# print list given a linked list
def printList(list):

    if not list:
        print ([])
        return

    printval = list

    while printval is not None:
        print(printval.val)
        printval = printval.next

def main():
    """
    :main calling program
    :
    """

    # case non empty list same size
    list1 = [1,2,4]
    list1 = buildLinkedList( list1)

    list2 = [1,3,4]
    list2 = buildLinkedList( list2)

    res = Solution().mergeTwoLists( list1, list2 )
    print("before calling printList")
    printList (res)
    print("after calling printList")

    # case both empty
    list1 = [ ]
    list1 = buildLinkedList( list1)

    list2 = [ ]
    list2 = buildLinkedList( list2)
    
    res = Solution().mergeTwoLists( list1, list2 )
    print("before calling printList")
    printList (res)
    print("after calling printList")

    # case one empty one not empty
    list1 = [ ]
    list1 = buildLinkedList( list1)

    list2 = [1 ]
    list2 = buildLinkedList( list2)

    res = Solution().mergeTwoLists( list1, list2 )
    print("before calling printList")
    printList (res)
    print("after calling printList")


    # case non empty list different sizes
    list1 = [1,2,4]
    list1 = buildLinkedList( list1)

    list2 = [1,3,4,5,6,7,8]
    list2 = buildLinkedList( list2)

    res = Solution().mergeTwoLists( list1, list2 )
    print("before calling printList")
    printList (res)
    print("after calling printList")

if __name__ == '__main__':
    main()
