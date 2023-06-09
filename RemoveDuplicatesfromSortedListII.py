# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return

        dummy = ListNode(next=head)

        curr = head
        prev = dummy
 
        while curr:

            while curr.next and curr.val == curr.next.val:
                # if at the head of list, reset head of list
                if curr == head:
                   

                    # two duplicates, then a non duplicate. remove the 2 dups
                    if curr.next.next and curr.next.val != curr.next.next.val:
                        head = curr.next.next
                        prev = curr.next
                        prev.next = curr.next.next
                        curr = curr.next.next 
                        
                    # two duplicates at the end of the list
                    elif not curr.next.next:
                        head  = None
                        return head
                    else:
                        head = curr.next
                        prev.next = curr.next
                        curr = curr.next

                else:
                    
                    # two duplicates, then a non duplicate. remove the 2 dups
                    if curr.next.next and curr.next.val != curr.next.next.val:
                        prev.next = curr.next.next
                        curr = curr.next.next 

                    # two duplicates at the end of the list
                    elif not curr.next.next:
                        prev.next = None
                        return head
                    else:
                        pass

            prev = curr       
            curr = curr.next
     
        return head
   
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

    # case for duplicates following duplicates in middle of the list
    head = [1,2,3,3,4,4,5]
    list = buildLinkedList(head)   
    res = Solution().deleteDuplicates( list )
    print("before calling printList")
    printList (res)
    print("after calling printList")

    # multiple duplicates at the beginning
    head = [1,1,1,2,3]
    list = buildLinkedList(head)   
    res = Solution().deleteDuplicates( list )
    print("before calling printList")
    printList (res)
    print("after calling printList")

    # more multiple duplicates at the beginning
    head = [1,1,1,2]
    list = buildLinkedList(head)   
    res = Solution().deleteDuplicates( list )
    print("before calling printList")
    printList (res)
    print("after calling printList")

    # case for duplicates at both beginning and end of list 
    head = [ 1,1,2, 3,3]
    list = buildLinkedList( head )
    res = Solution().deleteDuplicates( list )
    print("before calling printList")
    printList (res)
    print("after calling printList")

    # case for list of 1 
    head = [1]
    list = buildLinkedList( head )
    res = Solution().deleteDuplicates( list )
    print("before calling printList")
    printList (res)
    print("after calling printList")

    # case for empty set 
    head = [ ]
    list = buildLinkedList( head )
    res = Solution().deleteDuplicates( head )
    print("before calling printList")
    printList (res)

    # case for no repeating duplicates
    head = [1,2,3,4]
    list = buildLinkedList( head )
    res = Solution().deleteDuplicates( list )
    print("before calling printList")
    printList (res)

    # case for repeating duplicates
    head = [1,1,2,2,2,2,3,4,5,5,6,6,7]
    list = buildLinkedList( head )
    res = Solution().deleteDuplicates( list )
    print("before calling printList")
    printList (res)

if __name__ == '__main__':
    main()
