# Problem 21

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        head = ListNode()   # used as a placeholder for the head of the list
        tail = head         # pointer used to start traversing through each node

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next   

        # Insert the remaining nodes in either lists that are left 
        # This is possible because the sorted list after the while loop will always be lower
        # than any remaining node(s) in either list
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return head.next   
