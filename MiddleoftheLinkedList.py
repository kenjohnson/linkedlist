# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # advance 1 node at a time
        curr = head

        #advance 2 nodes at a time
        curr2 = head
 
        while curr2:

            if not curr2.next:
                return curr
            elif not curr2.next.next:
                return curr.next
            else:
                pass

            curr = curr.next
            curr2 = curr2.next.next

   
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

    # case for odd number of items in the list
    head = [1, 2, 3, 4, 5]
    list = buildLinkedList(head)
    res = Solution().middleNode( list )
    print("before calling printList")
    printList (res)
    print("after calling printList")

    # case for even number of items in the list
    head = [1, 2, 3, 4, 5, 6]
    list = buildLinkedList(head)
    res = Solution().middleNode( list )
    print("before calling printList")
    printList (res)
    print("after calling printList")

if __name__ == '__main__':
    main()
