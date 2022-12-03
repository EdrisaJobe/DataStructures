# merges two linked lists together    
# Time: O(n)
class LinkedList:
    def mergeTwo(self, lst1, lst2):

        # edge case sees first or last value of range not mid
        # we need to see mid vals too so we use dummy node (class Node)
        dummy = Node()
        tail = dummy

        while lst1 and lst2:

            # if the val in l1 is less set tail to lst1 and move on
            # else if lst2 is smaller we set it to the tail and move on
            if lst1.val < lst2.val:

                tail.next = lst1
                lst1 = lst1.next_node
            else:

                tail.next_node = lst2
                lst2 = lst2.next_node
            tail = tail.next_node
        
        # if we have reached end, see which is not pointing at null
        if lst1 is not None:
            tail.next_node = lst1
        elif lst2 is not None:
            tail.next_node = lst2


        return dummy.next_node

# Input: [1,2,3], [1,3,4]
# Output: [1,1,2,3,3,4]