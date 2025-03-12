# Visualization of bucket sort
def visualize_bucket_sort(arr):
    original = arr.copy()
    print("\nBucket Sort Visualization:")
    print(f"Original array: {original}")
    
    # Step 1: Initialize count array
    count = [0, 0, 0]
    print(f"\nStep 1: Initialize count array: {count}")
    
    # Step 2: Count occurrences
    for n in original:
        count[n] += 1
        print(f"  Count after seeing {n}: {count}")
    
    print(f"\nFinal count array: {count}")
    
    # Step 3: Reconstruct the array
    result = []
    print("\nStep 3: Reconstructing the array:")
    for n in range(len(count)):
        for j in range(count[n]):
            result.append(n)
            print(f"  Adding {n} to result: {result}")
    
    print(f"\nFinal sorted array: {result}")

# Run the visualization
visualize_bucket_sort([0,1,0,0,2,2,1,2])