# dutch flag proplem by Dijkstra, takes in three pointers i,j,k 
# represents the Dutch flag [red=0, white=1, blue=2]

# the pivot is the middle number which we use to compare other values within the list
def dutchflag(nums, pivot=1):
    
    # i and j will both be at the beggining of the list
    i = 0
    j = 0
    # k gets the last item within the list
    k = len(nums)-1
    
    while j <= k:
        
        # check to see if the element is bigger than 1
        if nums[j] < pivot:
            
            # swap the i and j vars and move them to the next index
            swap(nums, i, j)
            i=i+1
            j=j+1
        
        # if item j is bigger than 1
        elif nums[j] > pivot:
            
            #swap j and k vars and move k to the next index backwards
            swap(nums, j, k)
            k=k-1
        
        # if the values jand k are equal, move j over to next index
        else:
            j=j+1

    return nums

# swapping the values based on the above statments
def swap(nums, index1, index2):
    
    nums[index1], nums[index2] = nums[index2], nums[index1]
    
if __name__ == '__main__':
    print(dutchflag([1,0,2,1,2,0,1]))
        
        
            