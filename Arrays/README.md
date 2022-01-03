# Arrays
**Arrays are useful for storing a collection of data of the same type (ints, floats, strings). 
When deleting an item everything shifts to the left O(n). 
When inserting an item everything is shifted to the right to make room for the new element O(n). 
Appending and popping is O(1) since it adds or removes at the end of the list.** 
|Append| Insertion|Deletion 
|------|-------|------------
O(1)    |O(n)  | O(n)
 

# 🛠️ Examples
|            |Time Complexity (Best) :watch:|Space Complexity:black_large_square:|Description:books:|                                                                                                                    
|------------------|---------------                                 |----------------|--------------------------|
|Array reversal    | O(n) - Where n is number of elements reversed. |  O(1) - No matter how big the array, it requires same space. |We take in n amounts of data within an array and take two pointers which take the start and end of an index. We then swap the starting index with the end index until they reach the two pointers meet. *e.g. [1,2,3,4] -> [4,3,2,1]*                                                                                                                                  
|Integer reversal  | O(log n) - Where n is the number of digits in the integer.| O(1) - No matter how big the array, it requires same space.            | Take in integer values which we use a log n approach as input size grows, we swap the first index with last index. *e.g. 1234 -> 4321*
|Palindrome        | O(n) - Where n is the length of the string. | O(n) - Additional space needed to store the new filtered and reversed string.   | String values that can be read forwards and backwards. Similar to the array reversal, we swap string values to see if they match. *e.g. 'madam'*                                                                                                           
|Anagram           | O(n log n) - Due to the number of string letters sorted within both arrays.                                                | O(1) - Since no extra space is being taken, just prints True or False. | Words that can be rearranged to mean the same thing. Takes two string values and compares the length of the strings within sorted chars. *e.g. 'restful' -> 'fluster'*                                                                                                                
|Duplicate within Int list | O(n) - Due to the use of a for loop to iterate n numbers. | O(n) - Since space requitred is same size of input. | Checking a list to see whether two of the same integers are within it. We traverse through the list converting positive ints into negatives based on the value, array elements must be less than array size. *e.g. [2, 3, 4, 3, 1] -> [2, 3, -4, -3, -1] - > [2, -3, -4, -3, -1] dup = 3*
