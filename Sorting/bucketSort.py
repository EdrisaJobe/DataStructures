def bucketSort(arr):
    # Initialize a count array with zeros for each possible value (0, 1, 2)
    count = [0, 0, 0]

    # Count the occurrences of each value in the input array
    for n in arr:
        count[n] += 1  # Increment the count for the current value

    # Reconstruct the sorted array using the counts
    i = 0  # Initialize index for the original array
    for n in range(len(count)):  # Iterate through each possible value (0, 1, 2)
        for j in range(count[n]):  # Repeat each value according to its count
            arr[i] = n  # Place the value in the original array
            i += 1  # Move to the next position in the array
    
    return arr  # Return the sorted array

# Example usage
print(bucketSort([0,1,0,0,2,2,1,2]))  # Should print [0, 0, 0, 1, 1, 2, 2, 2]
'''
Bucket Sort Visualization:
Original array: [0, 1, 0, 0, 2, 2, 1, 2]

Step 1: Initialize count array: [0, 0, 0]
  Count after seeing 0: [1, 0, 0]
  Count after seeing 1: [1, 1, 0]
  Count after seeing 0: [2, 1, 0]
  Count after seeing 0: [3, 1, 0]
  Count after seeing 2: [3, 1, 1]
  Count after seeing 2: [3, 1, 2]
  Count after seeing 1: [3, 2, 2]
  Count after seeing 2: [3, 2, 3]

Final count array: [3, 2, 3]

Step 3: Reconstructing the array:
  Adding 0 to result: [0]
  Adding 0 to result: [0, 0]
  Adding 0 to result: [0, 0, 0]
  Adding 1 to result: [0, 0, 0, 1]
  Adding 1 to result: [0, 0, 0, 1, 1]
  Adding 2 to result: [0, 0, 0, 1, 1, 2]
  Adding 2 to result: [0, 0, 0, 1, 1, 2, 2]
  Adding 2 to result: [0, 0, 0, 1, 1, 2, 2, 2]

Final sorted array: [0, 0, 0, 1, 1, 2, 2, 2]
'''