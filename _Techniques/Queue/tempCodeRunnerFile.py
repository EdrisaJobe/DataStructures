    # O(n) - we keep popping until we find the last item
            item = self.stack.pop()

            # O(n) - recursively call the function until we find the 1ast item inserted
            dequeuedItem = self.dequeue()

            # O(n) - when the item is found we insert them 1by1 again
            self.stack.append(item)

            # return the found item
            return dequeuedItem