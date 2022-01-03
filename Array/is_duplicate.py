# we want to find out the duplicates within an array
# linear time best case O(n)
def duplicates(nums):
    
    # traverse the list
    for i in nums:
        
        # check to see if the list elements are > or = to 0, meaning all positives
        if nums[abs(i)] >= 0:
            
            # once it iterates, change the positive value to a negative based of the element stored
            nums[abs(i)] = -nums[abs(i)]
        else:
            # print out the duplicated values once loop completes
            print("Rep is: %s" % str(abs(i)))

if __name__ == '__main__':
    
    # elements must be less than array size
    n = [2, 3, 4, 1, 2]
    duplicates(n)
    print(n)
